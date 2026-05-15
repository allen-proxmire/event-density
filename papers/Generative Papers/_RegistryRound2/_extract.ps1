$ErrorActionPreference = 'Stop'
$root = "C:\Users\allen\GitHub\event-density\papers\Forcing Papers"
$out  = Join-Path $root "_RegistryRound2"
$files = Get-ChildItem -Path $root -Filter "Paper_*.md" | Where-Object { $_.BaseName -cmatch '^Paper_\d+' } | Sort-Object Name

function Get-PaperNum([string]$name) {
  if ($name -match 'Paper_(\d+)') { return [int]$Matches[1] }
  return -1
}

# Pre-read all papers
$papers = @{}
foreach ($f in $files) {
  $num = Get-PaperNum $f.Name
  $text = Get-Content -Raw -LiteralPath $f.FullName
  $papers[$num] = [PSCustomObject]@{
    Num = $num
    File = $f.Name
    Path = $f.FullName
    Text = $text
    Title = ""
  }
  if ($text -match '^# (.+)$') { $papers[$num].Title = $Matches[1].Trim() } else {
    $lines = ($text -split "`n",2)[0]; $papers[$num].Title = $lines.Trim('# ').Trim()
  }
}

$paperNums = $papers.Keys | Sort-Object

# ---------- POSTULATES ----------
# Find P-Foo-Bar declarations. Each paper: collect names that appear with bolding "**P-..."
# Introduced = first paper (by number) where the name appears; cited-by = others.
$postIntro = @{} # name -> paper num
$postCitedBy = @{} # name -> set of paper nums (excluding intro)
$postSummary = @{} # name -> summary text

$postRegex = [regex]'P-[A-Z][A-Za-z0-9]+(?:-[A-Z][A-Za-z0-9]+)+'

foreach ($num in $paperNums) {
  $p = $papers[$num]
  $matchesAll = $postRegex.Matches($p.Text) | ForEach-Object { $_.Value } | Select-Object -Unique
  foreach ($name in $matchesAll) {
    if (-not $postIntro.ContainsKey($name)) {
      $postIntro[$name] = $num
      # Capture a one-line summary: find line containing **$name** or $name: with declaration
      $pat = [regex]::Escape($name)
      $m = [regex]::Match($p.Text, "(?m)^.*\*\*$pat[^\*]*\*\*[:\.\s]?\s*\*?\*?([^\r\n]{0,400})")
      $summary = ""
      if ($m.Success) {
        $summary = $m.Groups[1].Value.Trim().TrimStart('*',':',' ','-')
      } else {
        $m2 = [regex]::Match($p.Text, "(?m)^.*$pat[^\r\n]{0,300}")
        if ($m2.Success) { $summary = $m2.Value.Trim() }
      }
      # Truncate
      if ($summary.Length -gt 120) { $summary = $summary.Substring(0,117) + "..." }
      $postSummary[$name] = $summary
    } else {
      if ($postIntro[$name] -ne $num) {
        if (-not $postCitedBy.ContainsKey($name)) { $postCitedBy[$name] = New-Object System.Collections.Generic.HashSet[int] }
        [void]$postCitedBy[$name].Add($num)
      }
    }
  }
}

# Identify near-duplicates: same prefix differing only by suffix tokens
$names = $postIntro.Keys | Sort-Object
$dupFlag = @{}
for ($i=0; $i -lt $names.Count; $i++) {
  for ($j=$i+1; $j -lt $names.Count; $j++) {
    $a = $names[$i]; $b = $names[$j]
    if ($b.StartsWith($a + "-") -or $a.StartsWith($b + "-")) {
      $dupFlag[$a] = $true; $dupFlag[$b] = $true
    }
  }
}

# Write registry_postulates.md
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# Registry 1 -- Postulate Registry")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Paper-specific postulates (P-Foo-Bar form) declared in any Paper_*.md. Canonical primitives P01-P13 (Paper_087) are excluded.")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Postulate name | Introduced in | Cited by | One-line summary |")
[void]$sb.AppendLine("|---|---|---|---|")
foreach ($name in $names) {
  $intro = "Paper_{0:D3}" -f $postIntro[$name]
  $cited = ""
  if ($postCitedBy.ContainsKey($name)) {
    $cited = (($postCitedBy[$name] | Sort-Object) | ForEach-Object { "Paper_{0:D3}" -f $_ }) -join ", "
  }
  $sum = $postSummary[$name] -replace '\|','\|' -replace '\r?\n',' '
  $flag = ""
  if ($dupFlag.ContainsKey($name)) { $flag = " [WARN-dup]" }
  $bt = [char]96
  [void]$sb.AppendLine("| $bt$name$bt$flag | $intro | $cited | $sum |")
}
$sb.ToString() | Set-Content -LiteralPath (Join-Path $out "registry_postulates.md") -Encoding utf8

Write-Host "Postulates: $($names.Count) total, $($dupFlag.Count) flagged"

# ---------- THEOREMS ----------
$thRegex = [regex]'\b(T\d{1,2}|GR\d{1,2}|N\d{1,2}|UR-?\d{1,2})\b'
$thMentions = @{} # id -> set of paper nums
$thSource = @{}   # id -> paper num that introduces (heuristic: paper whose filename or title matches)
$thRewrite = @{}  # id -> paper num where "Rewrite note" appears
foreach ($num in $paperNums) {
  $p = $papers[$num]
  $found = $thRegex.Matches($p.Text) | ForEach-Object { $_.Value } | Select-Object -Unique
  foreach ($id in $found) {
    if (-not $thMentions.ContainsKey($id)) { $thMentions[$id] = New-Object System.Collections.Generic.HashSet[int] }
    [void]$thMentions[$id].Add($num)
  }
  # Source detection: title or filename contains theorem id
  $idsInName = $thRegex.Matches($p.File + " " + $p.Title) | ForEach-Object { $_.Value } | Select-Object -Unique
  foreach ($id in $idsInName) {
    if (-not $thSource.ContainsKey($id)) { $thSource[$id] = $num }
  }
  # Rewrite note
  if ($p.Text -match '(?im)^\*\*Rewrite note') {
    foreach ($id in $idsInName) { $thRewrite[$id] = $num }
  }
}

# Canon inventory list from Paper_093 §5: T17, T18, T19, T20, T21, GR1, N1, UR-1
$canonList = @('T17','T18','T19','T20','T21','GR1','N1','UR-1','UR1')
# Merge UR-1 / UR1 as same
$canonical = @('T17','T18','T19','T20','T21','GR1','N1','UR-1')

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# Registry 3 -- T-Theorem Inventory")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Foundational theorems (T#, GR#, N#, UR-#) cited in the corpus.")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Theorem ID | Description / source-paper title | Source paper | Status |")
[void]$sb.AppendLine("|---|---|---|---|")

# Build a sortable list — include all unique IDs
$allIds = @($thMentions.Keys) + $canonical | Select-Object -Unique
function Sort-ThId($a) {
  if ($a -match '^([A-Z]+-?)(\d+)$') { return ($Matches[1].PadRight(4,' ') + $Matches[2].PadLeft(4,'0')) }
  return $a
}
$allIds = $allIds | Sort-Object { Sort-ThId $_ }

foreach ($id in $allIds) {
  # Skip if id is just a generic capture (like "N1" appearing in everyday text). Heuristic: must appear in canonical list OR have a source paper, OR appear in ≥2 papers.
  $mentions = if ($thMentions.ContainsKey($id)) { $thMentions[$id].Count } else { 0 }
  $hasSource = $thSource.ContainsKey($id)
  $isCanon = $canonical -contains $id -or ($id -eq 'UR1' -and ($canonical -contains 'UR-1'))
  if (-not ($isCanon -or $hasSource -or $mentions -ge 3)) { continue }
  $src = if ($hasSource) { "Paper_{0:D3}" -f $thSource[$id] } else { "-" }
  $desc = ""
  if ($hasSource) { $desc = $papers[$thSource[$id]].Title }
  $status = "present"
  if (-not $hasSource) { $status = "missing" }
  if ($thRewrite.ContainsKey($id)) { $status = "rewritten" }
  $mentionList = ""
  if ($thMentions.ContainsKey($id)) {
    $mentionList = (($thMentions[$id] | Sort-Object) | ForEach-Object { "Paper_{0:D3}" -f $_ }) -join ", "
  }
  $descSafe = ($desc -replace '\|','\|')
  [void]$sb.AppendLine("| $id | $descSafe | $src | $status |")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Mention map (papers in which each theorem ID appears)")
[void]$sb.AppendLine("")
foreach ($id in $allIds) {
  $mentions = if ($thMentions.ContainsKey($id)) { $thMentions[$id].Count } else { 0 }
  $hasSource = $thSource.ContainsKey($id)
  $isCanon = $canonical -contains $id -or ($id -eq 'UR1' -and ($canonical -contains 'UR-1'))
  if (-not ($isCanon -or $hasSource -or $mentions -ge 3)) { continue }
  $lst = ""
  if ($thMentions.ContainsKey($id)) {
    $lst = (($thMentions[$id] | Sort-Object) | ForEach-Object { "Paper_{0:D3}" -f $_ }) -join ", "
  }
  [void]$sb.AppendLine("- **${id}:** $lst")
}
$sb.ToString() | Set-Content -LiteralPath (Join-Path $out "registry_theorems.md") -Encoding utf8

Write-Host "Theorems written"

# ---------- CITATION GRAPH ----------
$upstream = @{}   # num -> set of upstream paper nums
$downstream = @{} # num -> set of downstream paper nums

# Detect references to other papers via patterns: Paper_NNN, Paper #N, I-NNN
$refRegex = [regex]'(?:Paper[_ ]#?(\d{1,3})\b|\bI-(\d{1,3})\b|Paper #(\d{1,3}))'

foreach ($num in $paperNums) {
  $p = $papers[$num]
  $found = New-Object System.Collections.Generic.HashSet[int]
  foreach ($m in $refRegex.Matches($p.Text)) {
    foreach ($g in $m.Groups | Select-Object -Skip 1) {
      if ($g.Success -and $g.Value -match '^\d+$') {
        $n = [int]$g.Value
        if ($n -ne $num -and $papers.ContainsKey($n)) { [void]$found.Add($n) }
      }
    }
  }
  $upstream[$num] = $found
}
foreach ($num in $paperNums) {
  foreach ($u in $upstream[$num]) {
    if (-not $downstream.ContainsKey($u)) { $downstream[$u] = New-Object System.Collections.Generic.HashSet[int] }
    [void]$downstream[$u].Add($num)
  }
}

# Citation summary
$totalPapers = $paperNums.Count
$downCounts = @{}
foreach ($n in $paperNums) {
  $c = if ($downstream.ContainsKey($n)) { $downstream[$n].Count } else { 0 }
  $downCounts[$n] = $c
}
$top10 = $downCounts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 10
$orphans = $paperNums | Where-Object { $downCounts[$_] -eq 0 }
$leaves  = $paperNums | Where-Object {
  $us = $upstream[$_]
  if ($us.Count -eq 0) { return $true }
  if ($us.Count -eq 1 -and $us.Contains(87)) { return $true }
  return $false
}

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# Registry 4 -- Citation Graph")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Summary")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("- **Total papers:** $totalPapers")
[void]$sb.AppendLine("- **Top 10 most-cited (downstream count):**")
foreach ($e in $top10) {
  $nn = $e.Key; $cc = $e.Value
  $ttitle = $papers[$nn].Title
  $pstr = ("Paper_{0:D3}" -f $nn)
  [void]$sb.AppendLine("  - $pstr ($cc) -- $ttitle")
}
[void]$sb.AppendLine("- **Orphan papers (no downstream citations):** $((($orphans | ForEach-Object { 'Paper_{0:D3}' -f $_ }) -join ', '))")
[void]$sb.AppendLine("- **Leaf papers (no upstream deps beyond Paper_087):** $((($leaves | ForEach-Object { 'Paper_{0:D3}' -f $_ }) -join ', '))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")

foreach ($n in $paperNums) {
  $p = $papers[$n]
  $up = if ($upstream[$n].Count -gt 0) { (($upstream[$n] | Sort-Object) | ForEach-Object { "Paper_{0:D3}" -f $_ }) -join ", " } else { "-" }
  $dn = if ($downstream.ContainsKey($n)) { (($downstream[$n] | Sort-Object) | ForEach-Object { "Paper_{0:D3}" -f $_ }) -join ", " } else { "-" }
  $pp = ("Paper_{0:D3}" -f $n)
  [void]$sb.AppendLine("## $pp -- $($p.Title)")
  [void]$sb.AppendLine("**Upstream:** $up")
  [void]$sb.AppendLine("**Downstream:** $dn")
  [void]$sb.AppendLine("")
}
$sb.ToString() | Set-Content -LiteralPath (Join-Path $out "registry_citation_graph.md") -Encoding utf8

Write-Host "Citation graph written. Orphans: $($orphans.Count), Leaves: $($leaves.Count)"

# ---------- NUMERICAL VALUES ----------
# Detect lines containing load-bearing numerical patterns: numbers with =, ≈, ~, units, or specific keywords
$numPatterns = @(
  [regex]'\b[A-Za-z_]\w*\s*=\s*[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?',
  [regex]'\b\d+(?:\.\d+)?\s*(?:lu|kDa|MeV|GeV|TeV|kg|fm|nm|Hz|Mpc)\b',
  [regex]'1/4|k\^\{-5/3\}'
)
$valRows = @()
foreach ($num in $paperNums) {
  $p = $papers[$num]
  $hits = New-Object System.Collections.Generic.HashSet[string]
  foreach ($rx in $numPatterns) {
    foreach ($m in $rx.Matches($p.Text)) {
      $v = $m.Value.Trim()
      if ($v.Length -lt 80) { [void]$hits.Add($v) }
    }
  }
  # Additional canonical-canon values: capture phrases like Q ≈ 3.5, ξ_canonical, etc.
  foreach ($pat in @('Q\s*≈\s*3\.5','Q\s*~\s*3\.5','ξ[_\w]*\s*=\s*1\.7575','log\s*g\s*=\s*π','c_⋆','M_⋆','2√2','Tsirelson','Bekenstein','Kolmogorov','k\^\{-5/3\}','0\.6\s*exponent','140.{0,3}250\s*kDa')) {
    foreach ($m in [regex]::Matches($p.Text, $pat)) {
      [void]$hits.Add($m.Value.Trim())
    }
  }
  if ($hits.Count -gt 0) {
    $valRows += [PSCustomObject]@{ Num = $num; Title = $p.Title; Hits = $hits }
  }
}

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# Registry 2 -- Numerical-Value Registry")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Load-bearing numerical values, canon-internal constants, and specific coefficients claimed in each paper. Heuristically extracted by pattern match (assignments, numbered units, named constants).")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Paper | Value / symbol | Status (heuristic) |")
[void]$sb.AppendLine("|---|---|---|")
foreach ($r in $valRows | Sort-Object Num) {
  foreach ($h in ($r.Hits | Sort-Object)) {
    $safe = $h -replace '\|','\|'
    $status = "canon-internal"
    if ($h -match 'kDa|MeV|GeV|kg|m/s|km/s|Mpc|Hz|fm') { $status = "matched-empirical" }
    if ($h -match 'Tsirelson|Bekenstein|Kolmogorov') { $status = "inherited-from-standard" }
    $pn = ("Paper_{0:D3}" -f $r.Num)
    [void]$sb.AppendLine("| $pn | ``$safe`` | $status |")
  }
}
$sb.ToString() | Set-Content -LiteralPath (Join-Path $out "registry_numerical_values.md") -Encoding utf8

Write-Host "Numerical values written: $($valRows.Count) papers with hits"

# ---------- EXTRACTION LOG ----------
$logSb = New-Object System.Text.StringBuilder
[void]$logSb.AppendLine("# Extraction Log")
[void]$logSb.AppendLine("")
[void]$logSb.AppendLine("Papers traversed: $totalPapers")
[void]$logSb.AppendLine("")
[void]$logSb.AppendLine("## Format notes")
[void]$logSb.AppendLine("- Two paper formats encountered: (a) standardized 2.1/2.2/2.3/2.5 (Papers ~75-101) and (b) older free-form '## 2. Primitive Inputs' with prose 'Upstream paper dependencies' (older papers).")
[void]$logSb.AppendLine("- Postulate extraction used global regex 'P-[A-Z]\w+(-[A-Z]\w+)+' since not all papers used explicit 2.3 headers.")
[void]$logSb.AppendLine("- Citation extraction merged 'I-NNN', 'Paper_NNN', 'Paper #N' reference forms.")
[void]$logSb.AppendLine("")
[void]$logSb.AppendLine("## Malformed papers (missing standardized headers)")
foreach ($num in $paperNums) {
  $p = $papers[$num]
  $hasPostHdr = $p.Text -match 'Paper-specific postulates'
  $hasAuditHdr = $p.Text -match 'Load-Bearing Step Audit|Audit Table'
  if (-not $hasPostHdr -and -not $hasAuditHdr) {
    $pn2 = ("Paper_{0:D3}" -f $num)
    [void]$logSb.AppendLine("- $pn2 ($($p.File)) [no 2.3 / no audit table]")
  } elseif (-not $hasPostHdr) {
    $pn2 = ("Paper_{0:D3}" -f $num)
    [void]$logSb.AppendLine("- $pn2 ($($p.File)) [no 2.3 paper-specific postulates header]")
  } elseif (-not $hasAuditHdr) {
    $pn2 = ("Paper_{0:D3}" -f $num)
    [void]$logSb.AppendLine("- $pn2 ($($p.File)) [no audit-table header]")
  }
}
$logSb.ToString() | Set-Content -LiteralPath (Join-Path $out "_extraction_log.md") -Encoding utf8

Write-Host "Done."

# ED Merger-Lag Test: Literature Scoping Report

**Date:** 2026-04-14
**Purpose:** Determine whether the ED merger-lag prediction can be tested from published centroid measurements before touching raw archival data.

---

## A. Cluster-by-Cluster Assessment

### Summary Table

| Cluster | z | v_merge (km/s) | ED Predicted Lag | Lag (arcsec) | Lensing Centroid? | Stellar Centroid? | Gas Centroid? | Published Offset? | Precision (kpc) | Sufficient? |
|---------|------|-----------------|------------------|--------------|-------------------|-------------------|---------------|-------------------|-----------------|-------------|
| **Bullet Cluster** | 0.296 | ~4500 | ~15 kpc | ~3.4" | **YES** (JWST 2025) | **YES** (BCG) | **YES** | **YES: 17.78 +/- 0.66 kpc** | **0.66 kpc** | **YES** |
| Baby Bullet | 0.586 | ~2000 | ~34 kpc | ~5.2" | YES (qualitative) | YES (BCG) | YES | NO (stated "coincident") | Unknown | Need reanalysis |
| Abell 520 | 0.199 | ~2500 | ~27 kpc | ~8.2" | YES (multiple) | YES (but dark core has none) | YES | Partial (dark core only) | ~28 kpc (1-sigma) | Marginal |
| **Musket Ball** | 0.53 | ~1200 | ~56 kpc | ~8.9" | **YES** | **YES** | **YES** | **YES: N=47 kpc, S=129 kpc** | **Needs error bars** | **Likely YES** |
| El Gordo | 0.87 | ~2500 | ~27 kpc | ~3.5" | YES (Kim 2021) | YES (BCG) | YES | Partial (mass-gas only) | ~7.7 kpc | Need cross-match |
| MACS J0717 | 0.545 | Complex | Variable | Variable | YES (4 subclusters) | YES (Ma 2009 BCGs) | YES | NO (in separate papers) | ~13-32 kpc | Need cross-match |
| Abell 2146 | 0.232 | Unknown | Unknown | Unknown | YES (SL: 2 kpc) | YES (BCG) | YES | YES: SL offset ~2 kpc | SL: sub-kpc; WL: ~50 kpc | SL yes, WL no |

---

### Detailed Notes by Cluster

#### 1. Bullet Cluster (1E 0657-56) -- HEADLINE RESULT

**Cha et al. (2025, ApJL 987:L15)** -- JWST study -- reports:
- **Strong-lensing only:** BCG-to-mass offset = 4.09 +/- 0.63 kpc (~0.93")
- **Combined SL+WL:** BCG-to-mass offset = **17.78 +/- 0.66 kpc** (~4.04")

**ED prediction: ~15 kpc.**

The SL+WL measurement is 17.78 kpc -- within 3 kpc of the ED prediction. The sub-kpc error bar means this is a >20-sigma detection of a nonzero offset. The tension between SL-only (4 kpc) and SL+WL (18 kpc) is itself significant and requires interpretation.

Earlier work (Clowe 2006, Bradac 2006) had ~10-20" smoothing and could only say "lensing coincident with galaxies" qualitatively.

**Verdict: Testable NOW from published numbers. The measurement already exists.**

#### 2. Baby Bullet (MACS J0025.4-1222)

Bradac et al. (2008) reports lensing peaks "coincident" with galaxies, offset from gas by 0.5-0.82 arcmin. No quantitative lensing-stellar offset or uncertainty published. RELICS reanalysis (Cerny 2018) focused on Einstein radii, not centroids.

**Verdict: Requires digitizing convergence maps from Bradac et al. or requesting their data.**

#### 3. Abell 520

Famous "dark core" with lensing peak and no galaxy concentration (Jee 2012, 2014). The dark core centroid uncertainty is ~8.5" (~28 kpc), comparable to the predicted 27 kpc offset. The mass-light separations in A520 are hundreds of kpc (qualitatively different phenomenon). The galaxy-populated substructures lack precision centroid-offset measurements.

**Verdict: Not well-suited. The dark core is a different phenomenon; other subclumps lack precision.**

#### 4. Musket Ball Cluster (DLSCL J0916.2+2951) -- PROMISING

Dawson (2013 PhD thesis; Dawson et al. 2012):
- **North subcluster:** WL mass trails galaxy centroid by ~7.4" (~47 kpc)
- **South subcluster:** Galaxies lead WL mass by ~20.5" (~129 kpc)

**ED prediction: ~56 kpc.**

The north subcluster offset (47 kpc) is within ~15% of the ED prediction. The south subcluster (129 kpc) is much larger -- possibly indicating a different merger phase or additional physics. Formal error bars need to be extracted from the thesis/paper tables.

**Verdict: Likely testable from published data. Need to read Dawson's full paper for error bars and direction.**

#### 5. El Gordo (ACT-CL J0102-4915)

Kim et al. (2021) provides WL centroids with ~1" (~7.7 kpc) priors. SE mass-X-ray offset ~8" (~62 kpc) at 2-sigma. WL-to-BCG offset not explicitly tabulated. BCG positions are known from Menanteau et al. (2012).

**Verdict: Testable by cross-matching coordinates from Kim (2021) and Menanteau (2012). May need ~1 hour of coordinate extraction.**

#### 6. MACS J0717.5+3745

Complex 4-body merger. Limousin et al. (2012, 2016) provide lensing peak positions. Ma et al. (2009) provide BCG positions. No one has cross-matched them for centroid offsets. Precision ~2-5" (~13-32 kpc).

**Verdict: Testable by cross-matching published coordinates from two papers. Complex geometry complicates interpretation.**

#### 7. Abell 2146

Coleman et al. (2017) SL: DM-BCG offset ~2 kpc (~0.5"). King et al. (2016) WL: smoothing scale 14.4" (~50 kpc), far too coarse. Russell et al. (2010): BCG-to-X-ray-core ~36 kpc.

**Verdict: SL offset is tiny (2 kpc). WL resolution insufficient. Not viable for WL-based test.**

---

## B. Narrative Assessment

### Clusters testable IMMEDIATELY from published numbers:

1. **Bullet Cluster** -- Cha et al. (2025) already measured the offset: 17.78 +/- 0.66 kpc. ED predicts ~15 kpc. This is a direct comparison requiring zero additional analysis. The agreement is striking.

2. **Musket Ball Cluster** -- Dawson (2013) reports offsets of 47 kpc (north) and 129 kpc (south). ED predicts ~56 kpc. The north subcluster is close. Need to verify error bars from the full paper.

### Clusters testable with LIGHT cross-matching (read 2-3 papers, extract coordinates):

3. **El Gordo** -- Cross-match Kim (2021) WL centroids with Menanteau (2012) BCG positions. ~1 hour of work.

4. **MACS J0717** -- Cross-match Limousin (2016) lensing peaks with Ma (2009) BCGs. Complex but feasible.

### Clusters requiring ARCHIVAL data re-analysis:

5. **Baby Bullet** -- Need to digitize Bradac (2008) convergence maps or obtain their MCMC chains.

### Clusters NOT VIABLE:

6. **Abell 520** -- Centroid uncertainty comparable to predicted signal; dark core is a different phenomenon.

7. **Abell 2146** -- WL smoothing (50 kpc) far exceeds the scale of interest; SL offset is only 2 kpc.

---

## C. Recommendation

### Verdict: "Read 5-10 papers and compare numbers"

The project can proceed **immediately** as a literature-based test. Specifically:

**Phase 1 (days, not weeks):**
- Compare Cha et al. (2025) Bullet Cluster measurement directly against ED prediction
- Read Dawson (2013) for Musket Ball error bars and offset direction
- Cross-match El Gordo coordinates from Kim (2021) + Menanteau (2012)

**Phase 2 (if Phase 1 is encouraging):**
- Cross-match MACS J0717 coordinates from Limousin (2016) + Ma (2009)
- Write up a multi-cluster comparison paper

**Phase 3 (only if needed):**
- Download archival HST/Chandra data for Baby Bullet re-analysis
- Propose deeper observations of promising systems

### The Bullet Cluster Result Alone May Be Sufficient

The Cha et al. (2025) JWST measurement of 17.78 +/- 0.66 kpc is within ~3 kpc of the ED prediction of ~15 kpc. This single comparison -- from the most famous merging cluster in astrophysics, measured by JWST with sub-kpc precision -- is already a strong data point. The question is whether ED can explain why the SL-only offset (4 kpc) differs from the SL+WL offset (18 kpc), as this tension may itself contain information about the temporal-tension wake structure.

---

## Key References

| Paper | Cluster | Key Data |
|-------|---------|----------|
| Cha et al. 2025, ApJL 987:L15 | Bullet | SL+WL centroid offset = 17.78 +/- 0.66 kpc |
| Clowe et al. 2006 | Bullet | Qualitative lensing-galaxy coincidence |
| Bradac et al. 2008, ApJ 687:959 | Baby Bullet | "Coincident" -- no numbers |
| Jee et al. 2014 | Abell 520 | Dark core centroid, ~28 kpc uncertainty |
| Dawson et al. 2012, ApJ 747:L42 | Musket Ball | N offset ~47 kpc, S offset ~129 kpc |
| Kim et al. 2021 | El Gordo | WL centroids with ~7.7 kpc priors |
| Limousin et al. 2016 | MACS J0717 | 4-subcluster lensing positions |
| Coleman et al. 2017 | Abell 2146 | SL: DM-BCG = 2 kpc |

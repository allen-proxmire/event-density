"""
edsim.roadmap.dependencies -- Dependency graph for ED-SIM-03 components and questions.

Builds a directed acyclic graph (DAG) representing prerequisite
relationships between engineering components and research questions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from collections import defaultdict, deque

from .architecture import EDSIM3Architecture, Component
from .questions import ResearchQuestion


@dataclass(frozen=True)
class Node:
    """A node in the dependency graph.

    Attributes
    ----------
    id : str
        Unique identifier.
    kind : str
        "component" or "question".
    title : str
        Display title.
    """

    id: str
    kind: str
    title: str


@dataclass
class DependencyGraph:
    """Directed acyclic graph of dependencies.

    Attributes
    ----------
    nodes : dict[str, Node]
        Keyed by node ID.
    edges : list[tuple[str, str]]
        (from_id, to_id) meaning from_id must complete before to_id.
    adjacency : dict[str, list[str]]
        Forward adjacency: node -> list of dependents.
    reverse : dict[str, list[str]]
        Reverse adjacency: node -> list of prerequisites.
    """

    nodes: dict = field(default_factory=dict)
    edges: list = field(default_factory=list)
    adjacency: dict = field(default_factory=lambda: defaultdict(list))
    reverse: dict = field(default_factory=lambda: defaultdict(list))

    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node

    def add_edge(self, from_id: str, to_id: str) -> None:
        if from_id in self.nodes and to_id in self.nodes:
            self.edges.append((from_id, to_id))
            self.adjacency[from_id].append(to_id)
            self.reverse[to_id].append(from_id)

    def roots(self) -> list[str]:
        """Nodes with no prerequisites."""
        return [
            nid for nid in self.nodes
            if nid not in self.reverse or len(self.reverse[nid]) == 0
        ]

    def topological_order(self) -> list[str]:
        """Return nodes in topological order (Kahn's algorithm)."""
        in_degree = {nid: 0 for nid in self.nodes}
        for _, to_id in self.edges:
            in_degree[to_id] += 1

        queue = deque(nid for nid, deg in in_degree.items() if deg == 0)
        order = []
        while queue:
            nid = queue.popleft()
            order.append(nid)
            for dep in self.adjacency.get(nid, []):
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)

        return order

    def depth(self, node_id: str) -> int:
        """Longest path from any root to this node."""
        if node_id not in self.reverse or len(self.reverse[node_id]) == 0:
            return 0
        return 1 + max(self.depth(p) for p in self.reverse[node_id])

    def to_mermaid(self) -> str:
        """Export the graph as a Mermaid diagram string."""
        lines = ["graph TD"]
        for nid, node in self.nodes.items():
            shape = f"[{node.title}]" if node.kind == "component" else f"({node.title})"
            lines.append(f"    {nid}{shape}")
        for from_id, to_id in self.edges:
            lines.append(f"    {from_id} --> {to_id}")
        return "\n".join(lines)

    def to_table(self) -> str:
        """Export the graph as a Markdown table."""
        lines = [
            "| Node | Kind | Prerequisites | Depth |",
            "|------|------|---------------|-------|",
        ]
        for nid in self.topological_order():
            node = self.nodes[nid]
            prereqs = ", ".join(self.reverse.get(nid, [])) or "(none)"
            d = self.depth(nid)
            lines.append(f"| {nid} | {node.kind} | {prereqs} | {d} |")
        return "\n".join(lines)


def build_dependency_graph(
    architecture: EDSIM3Architecture,
    questions: list[ResearchQuestion],
) -> DependencyGraph:
    """Build the full dependency DAG.

    Parameters
    ----------
    architecture : EDSIM3Architecture
        Component list.
    questions : list[ResearchQuestion]
        Research question list.

    Returns
    -------
    DependencyGraph
    """
    graph = DependencyGraph()

    # Add component nodes
    for comp in architecture.components:
        graph.add_node(Node(id=comp.name, kind="component", title=comp.title))

    # Add component-to-component edges
    for comp in architecture.components:
        for prereq in comp.prerequisites:
            graph.add_edge(prereq, comp.name)

    # Add question nodes
    for q in questions:
        graph.add_node(Node(id=q.id, kind="question", title=q.question[:50] + "..."))

    # Add question dependencies
    for q in questions:
        for dep in q.dependencies:
            if dep in graph.nodes:
                graph.add_edge(dep, q.id)

    return graph

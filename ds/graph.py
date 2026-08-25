"""An adjacency list graph with the common traversal algorithms."""

from ds.heap import PriorityQueue
from ds.union_find import UnionFind


class Graph:
    """A weighted graph that can be directed or undirected."""

    def __init__(self, directed=False):
        self.directed = directed
        self._adjacency = {}

    def __len__(self):
        return len(self._adjacency)

    def __contains__(self, node):
        return node in self._adjacency

    def __iter__(self):
        return iter(self._adjacency)

    def __repr__(self):
        kind = "directed" if self.directed else "undirected"
        return "Graph({}, {} nodes)".format(kind, len(self._adjacency))

    def add_node(self, node):
        if node in self._adjacency:
            return False
        self._adjacency[node] = {}
        return True

    def add_edge(self, source, target, weight=1):
        self.add_node(source)
        self.add_node(target)
        self._adjacency[source][target] = weight
        if not self.directed:
            self._adjacency[target][source] = weight

    def remove_edge(self, source, target):
        removed = self._adjacency.get(source, {}).pop(target, None) is not None
        if not self.directed:
            self._adjacency.get(target, {}).pop(source, None)
        return removed

    def neighbours(self, node):
        return dict(self._adjacency.get(node, {}))

    def degree(self, node):
        return len(self._adjacency.get(node, {}))

    def edges(self):
        result = []
        seen = set()
        for source, targets in self._adjacency.items():
            for target, weight in targets.items():
                if not self.directed:
                    key = frozenset((source, target))
                    if key in seen:
                        continue
                    seen.add(key)
                result.append((source, target, weight))
        return result

    def breadth_first(self, start):
        if start not in self._adjacency:
            raise KeyError(start)
        order = []
        visited = {start}
        queue = [start]
        index = 0
        while index < len(queue):
            node = queue[index]
            index += 1
            order.append(node)
            for neighbour in self._adjacency[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return order

    def depth_first(self, start):
        if start not in self._adjacency:
            raise KeyError(start)
        order = []
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for neighbour in sorted(self._adjacency[node], reverse=True, key=repr):
                if neighbour not in visited:
                    stack.append(neighbour)
        return order

    def shortest_path(self, start, goal):
        """Dijkstra; returns (path, cost) or ([], inf) when unreachable."""
        if start not in self._adjacency or goal not in self._adjacency:
            raise KeyError("unknown node")
        distances = {start: 0}
        previous = {}
        settled = set()
        queue = PriorityQueue()
        queue.push(start, 0)
        while queue:
            node = queue.pop()
            if node in settled:
                continue
            settled.add(node)
            if node == goal:
                break
            for neighbour, weight in self._adjacency[node].items():
                candidate = distances[node] + weight
                if candidate < distances.get(neighbour, float("inf")):
                    distances[neighbour] = candidate
                    previous[neighbour] = node
                    queue.push(neighbour, candidate)
        if goal not in distances:
            return [], float("inf")
        path = [goal]
        while path[-1] != start:
            path.append(previous[path[-1]])
        path.reverse()
        return path, distances[goal]

    def connected_components(self):
        union = UnionFind(self._adjacency)
        for source, target, _ in self.edges():
            union.union(source, target)
        return union.to_groups()

    def minimum_spanning_tree(self):
        """Kruskal; only meaningful for undirected graphs."""
        if self.directed:
            raise ValueError("spanning tree requires an undirected graph")
        union = UnionFind(self._adjacency)
        tree = []
        for source, target, weight in sorted(self.edges(), key=lambda edge: edge[2]):
            if union.union(source, target):
                tree.append((source, target, weight))
        return tree

    def topological_order(self):
        """Kahn's algorithm; raises when the graph has a cycle."""
        if not self.directed:
            raise ValueError("topological order requires a directed graph")
        incoming = {node: 0 for node in self._adjacency}
        for targets in self._adjacency.values():
            for target in targets:
                incoming[target] += 1
        queue = [node for node, count in incoming.items() if count == 0]
        order = []
        index = 0
        while index < len(queue):
            node = queue[index]
            index += 1
            order.append(node)
            for neighbour in self._adjacency[node]:
                incoming[neighbour] -= 1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        if len(order) != len(self._adjacency):
            raise ValueError("graph contains a cycle")
        return order

    def has_cycle(self):
        try:
            self.topological_order()
        except ValueError:
            return True
        return False

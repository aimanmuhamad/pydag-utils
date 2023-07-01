import networkx as nx
import matplotlib.pyplot as plt

class DAGNode:
    def __init__(self, function):
        self.function = function
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
class DAG:
    def __init__(self):
        self.nodes = []

    def add_node(self, function):
        node = DAGNode(function)
        self.nodes.append(node)
        return node

    def add_edge(self, parent, child):
        parent.add_child(child)

    def execute(self):
        sorted_nodes = self.topological_sort()

        for node in sorted_nodes:
            node.function()

    def visualize(self):
        G = nx.DiGraph()

        for node in self.nodes:
            G.add_node(node.function.__name__)

        for node in self.nodes:
            for child in node.children:
                G.add_edge(node.function.__name__, child.function.__name__)

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, arrows=True)
        plt.show()

    def topological_sort(self):
        sorted_nodes = []
        visited = set()

        def dfs(node):
            visited.add(node)
            for child in node.children:
                if child not in visited:
                    dfs(child)
            sorted_nodes.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)

        return sorted_nodes
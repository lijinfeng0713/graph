"""
    Undirected Graph
    Author:  lijinfeng
    Date:    207-07-14
    Version: 1.0
"""


class Graph(object):

    # init member variables
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    # add node to the graph
    def add_node(self, i):
        if self.nodes.get(i) is not None:
            return
        self.nodes[i] = set()

    def add_edge(self, i, j, weight=1.0):
        """Add edge to the graph.
        the edge(j, i) is seem to be equal to edge(i, j) in an undirected graph
        
        Parameters
        -----------
        i:      node i
        j:      node j
        weight: the weight of edge(i, j), the default value is 1.0
        
        """
        if self.edges.get((i, j)) is not None or self.edges.get((j, i)) is not None:
            return
        self.nodes.get(i).add(j)
        self.nodes.get(j).add(i)
        self.edges[(i, j)] = weight

    def size(self):
        return len(self.nodes.keys())

    def degree(self, i):
        """Get the degree of node i.
        
        Parameters
        -----------
        i:      node i
        
        Return
        -----------
        the degree of node i
         
        """
        return len(self.nodes.get(i))

    def neighbors(self, i):
        """Get the neighbors of node i.

        Parameters
        -----------
        i: node i

        Return
        -----------
        a set contains the neighbors of node i

        """
        return self.nodes.get(i)

    def common_neighbors(self, i, j):
        """Get the common neighbors of node i, j.

        Parameters
        -----------
        i: node i
        j: node j

        Return
        -----------
        a set contains the common neighbors of node i, j

        """
        neighbors_i = self.nodes.get(i)
        neighbors_j = self.nodes.get(j)
        common_neighbors = set()

        for element in neighbors_i:
            if element in neighbors_j:
                common_neighbors.add(element)

        return common_neighbors

    def get_nodes(self):
        return list(self.nodes.keys())

    def get_edges(self):
        return list(self.edges)

    def add_weight(self, i, j, weight):
        self.edges[(i, j)] = weight

    def get_weight(self, i, j):
        return float(self.edges.get((i, j)) or self.edges.get((j, i)))

    def get_weights_from(self, i):
        """Calculate the sum of weights of edges linked to node i.
        
        Parameters
        -----------
        i: node i

        Return
        -----------
        the sum of weight
        
        """
        weights = 0.0
        for n in self.neighbors(i):
            weights += self.get_weight(i, n)
        return weights


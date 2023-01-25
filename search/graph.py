import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        
        # check graph is not empty
        if nx.is_empty(self.graph):
            raise Exception('Graph is empty')
        
        # check graph is not unconnected
        if not nx.is_weakly_connected(self.graph):
            return None
        
        # check start node is in graph
        if not self.graph.has_node(start):
            raise Exception(f'Graph does not have node {start}')
        
        # check end node is in graph
        if (end != None) and not self.graph.has_node(end):
            raise Exception(f'Graph does not have node {end}')
        
        
        queue = []
        visited = []
        
        queue.append(start)
        visited.append(start)        
        
        while queue:
            v = queue.pop(0)
            neighbors = [n for n in self.graph.neighbors(v)]
            for n in neighbors:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                    if n == end:
                        return visited

        if (end != None) and (end not in visited):
            return None
       
        return visited

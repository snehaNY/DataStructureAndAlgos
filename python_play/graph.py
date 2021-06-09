from abc import ABC
import numpy as np

class Graph(ABC):
    def __init__(self,numVertices,directed= False):
        self.numVertices = numVertices
        self.directed = directed

    @abstractmethod
    def add_edges(self,v1,v2,weight):
        pass
    
    @abstractmethod
    def get_adjecent_matrix(self,v):
        pass

    @abstractmethod
    def get_indegree(self,v):
        pass

    @abstractmethod
    def get_edge_weight(self,v1,v2):
        pass

    @abstractmethod
    def display(self):
        pass





from queue import *

"""
Class       : Graph
Description : implementación de Grafo
"""
class Graph:
    graph = dict()
    
    """
    Builder
    """
    def __init__(self, N, M):
        i = 1
        while i <= N:
            j = 1
            while j <= M:
                point = (i,j)
                self.graph[point] = list()
                j += 1
            i += 1

    """
    Method      : fillGraphs
    Parameters  : int N, int M
    Description : rellena el grafo conectando todos
                  puntos "L" adjacentes y conectando
                  todos los puntos "W" adyacentes.
    """
    def fillGraph(self, N, M, case):
        i = 1
        while i <= N:
            j = 1
            while j <= M:
                point = (i,j)
                mark = case[i-1][j-1]

                adj1 = (i-1,j-1)
                adj2 = (i-1,j+1)
                adj3 = (i+1,j+1)
                adj4 = (i+1,j-1)
                adj5 = (i-1,j)
                adj6 = (i+1,j)
                adj7 = (i,j-1)
                adj8 = (i,j+1)
                
                if i==1 and j==1:
                    if case[i][j]     == mark:
                        self.graph[point].append(adj3)
                    if case[i][j-1]   == mark:
                        self.graph[point].append(adj6)
                    if case[i-1][j]   == mark:
                        self.graph[point].append(adj8)
                elif i==1 and j==M:
                    if case[i][j-2]   == mark:
                        self.graph[point].append(adj4)
                    if case[i][j-1]   == mark:
                        self.graph[point].append(adj6)
                    if case[i-1][j-2] == mark:    
                        self.graph[point].append(adj7)
                elif i==N and j==1:
                    if case[i-2][j]   == mark:
                        self.graph[point].append(adj2)
                    if case[i-2][j-1] == mark:    
                        self.graph[point].append(adj5)
                    if case[i-1][j]   == mark:    
                        self.graph[point].append(adj8)
                elif i==N and j==M:
                    if case[i-2][j-2] == mark:
                        self.graph[point].append(adj1)
                    if case[i-2][j-1] == mark:    
                        self.graph[point].append(adj5)
                    if case[i-1][j-2] == mark:    
                        self.graph[point].append(adj7)
                elif i==1:
                    if case[i][j]     == mark:
                        self.graph[point].append(adj3)
                    if case[i][j-2]   == mark:    
                        self.graph[point].append(adj4)
                    if case[i][j-1]   == mark:    
                        self.graph[point].append(adj6)
                    if case[i-1][j-2] == mark:    
                        self.graph[point].append(adj7)
                    if case[i-1][j]   == mark:    
                        self.graph[point].append(adj8)
                elif i==N:
                    if case[i-2][j-2] == mark:
                        self.graph[point].append(adj1)
                    if case[i-2][j]   == mark:
                        self.graph[point].append(adj2)
                    if case[i-2][j-1] == mark:
                        self.graph[point].append(adj5)
                    if case[i-1][j-2] == mark:
                        self.graph[point].append(adj7)
                    if case[i-1][j]   == mark:
                        self.graph[point].append(adj8)
                elif j==1:
                    if case[i-2][j]   == mark:
                        self.graph[point].append(adj2)
                    if case[i][j]     == mark:
                        self.graph[point].append(adj3)
                    if case[i-2][j-1] == mark:
                        self.graph[point].append(adj5)
                    if case[i][j-1]   == mark:
                        self.graph[point].append(adj6)
                    if case[i-1][j]   == mark:
                        self.graph[point].append(adj8)
                elif j==M:
                    if case[i-2][j-2] == mark:
                        self.graph[point].append(adj1)
                    if case[i][j-2]   == mark:
                        self.graph[point].append(adj4)
                    if case[i-2][j-1] == mark:
                        self.graph[point].append(adj5)
                    if case[i][j-1]   == mark:
                        self.graph[point].append(adj6)
                    if case[i-1][j-2] == mark:
                        self.graph[point].append(adj7)
                else:
                    if case[i-2][j-2] == mark:
                        self.graph[point].append(adj1)
                    if case[i-2][j]   == mark:
                        self.graph[point].append(adj2)
                    if case[i][j]     == mark:
                        self.graph[point].append(adj3)
                    if case[i][j-2]   == mark:
                        self.graph[point].append(adj4)
                    if case[i-2][j-1] == mark:
                        self.graph[point].append(adj5)
                    if case[i][j-1]   == mark:
                        self.graph[point].append(adj6)
                    if case[i-1][j-2] == mark:
                        self.graph[point].append(adj7)
                    if case[i-1][j]   == mark:
                        self.graph[point].append(adj8)
                j += 1
            i += 1

    """
    Method      : getAdjacents
    Parameters  : tuple point
    return      : todos los puntos adjacentes a point
    """
    def getAdjacents(self,point):
        return self.graph[point]

    """
    Method      : BFS
    Parameters  : tuple point
    Description : realiza un recorrido BFS
    Return      : el path realizado
    """
    def BFS(self,point):
        #lista a retornar
        path = list()

        # cola auxiliar
        Q = Queue()
        Q.enqueue(point)
        
        #lista para marcar puntos visitados
        L = list()
        

        while Q.size() != 0:
            coordenate = Q.dequeue()
            if coordenate not in L:
                L.append(coordenate)
                path.append(coordenate)
                adj = self.getAdjacents(coordenate)
                for tupla in adj:
                    if Q.hasPoint(tupla) == 0:
                        Q.enqueue(tupla)
        return path

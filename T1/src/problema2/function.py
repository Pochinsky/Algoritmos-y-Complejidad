from graph import *

"""
Function    : getArea
Parameters  : tuple point
Description : obtiene el area del lago que
              contiene el punto point
Return      : area del lago             
"""
def getArea(graph, point):
    path = graph.BFS(point)
    return len(path)

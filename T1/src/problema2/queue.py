"""
Class       : Queue
Description : implementación de Cola
"""
class Queue:

    """
    Builder
    """
    def __init__(self):
        self.queue = list()
    
    """
    Method      : enqueue
    Parameters  : tuple point
    Description : implementacion de operacion ENQUEUE
    """
    def enqueue(self,point):
        self.queue.insert(0,point)
    
    """
    Method      : dequeue
    Parameters  : no recibe parámetros
    Description : implementacion de opracion DEQUEUE
    Return      : la primera tupla que entró
    """
    def dequeue(self):
        return self.queue.pop()

    """
    Method      : size
    Parameters  : no recibe parametros
    Description : obtiene el tamaño de Queue
    Return      : el tamaño de Queue
    """
    def size(self):
        return len(self.queue)

    """
    Method      : hasPoint
    Parameters  : tuple point
    Description : corrobora si la tupla point esta en Queue
    Return      : si la tupla contiene a point, entonces retorna 1,
                  si no, retorna 0.
    """
    def hasPoint(self,point):
        if point in self.queue:
            return 1
        else:
            return 0

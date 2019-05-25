import heapq

class priorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):    
        return heapq.heappop(self.elements)[1] #porque en un heap el elem 0 no existe? 


def heuristic(a, b): #La funcion de la heuristica es calcular el precio del punto actual al goal mas el costo actual
    (x1, y1) = a 
    (x2, y2) = b
    return abs(x2 - x1) + abs (y2 - y1)
def aStar(graph, initial, goal):
    frontier = priorityQueue() #se crea la cola de prioridad
    frontier.put(initial, 0) #ingreso el elmento a la cola
    vengo_de = {}
    costo_hasta_ahora = {}
    vengo_de[initial] = None #en el diccionario initial= none
    costo_hasta_ahora[initial] = 0

    #camino = []

    while not frontier.empty():

        #print("camino: "+str(contruirCamino(vengo_de,initial,goal))) 

        current = frontier.get() #obtego el 1ero de la cola
        print("current: "+str(current))
        if current[0] == goal:
            break

        vecinos = graph[current[0]]
        for next in vecinos:
            print(current, 12)
            new_cost = next[1] + costo_hasta_ahora[current]
            if next[0] not in costo_hasta_ahora or new_cost < costo_hasta_ahora[next[0]]:
                costo_hasta_ahora[next[0]] = new_cost
                priority = new_cost 
                frontier.put(next[0], priority)
                vengo_de[next[0]] = current

    return vengo_de, costo_hasta_ahora



graph = {
        'A' : [('B', 1), ('C', 2)],
        'B' : [('D', 1), ('E', 4)],
        'C' : [('E', 1)],
        'D' : [('E', 2)]
}



a, b = aStar(graph, 'A', 'E')

print(a)

"""
def contruirCamino(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) 
    path.reverse() 
    return path
"""


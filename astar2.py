import heapq

class priorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):    
        return heapq.heappop(self.elements)[1]


def heuristic(a, b): #La funcion de la heuristica es calcular el precio del punto actual al goal mas el costo actual
    (x1, y1) = a 
    (x2, y2) = b
    return abs(x2 - x1) + abs (y2 - y1)

def aStar(graph, initial, goal):
    dequeue = []
    frontier = priorityQueue()
    frontier.put(initial,0)
    vengo_de = {}
    costo_hasta_ahora = {}
    vengo_de[initial] = None
    costo_hasta_ahora[initial] = 0
    while not frontier.empty():
        current = frontier.get()
        dequeue.append(current)
        if current == goal:
            break

        vecinos = graph[current]
        for next in vecinos:
            new_cost = next[1] + costo_hasta_ahora[current]
            if next[0] not in costo_hasta_ahora or new_cost < costo_hasta_ahora[next[0]]:
                costo_hasta_ahora[next[0]] = new_cost
                priority = new_cost 
                frontier.put(next[0], priority)
                vengo_de[next[0]] = current

    return vengo_de, costo_hasta_ahora, dequeue

graph = {
        0 : [(2, 6), (4, 6), (5, 17)],
        1 : [(3, 17)],
        2 : [(5, 11), (7, 6)],
        3 : [(0, 1), (10, 3), (1, 25), (6, 13), (8, 9)],
        4 : [(5, 3), (6, 4), (7, 3), (8, 1), (9, 15)],
        5 : [(1, 12), (2, 1), (4, 3), (7, 10), (8, 4)],
        6 : [(0, 12), (1, 5), (2, 1), (4, 9), (9, 4)],
        7 : [(1, 7), (5, 11), (9, 6)],
        8 : [],
        9 : [],
        10 : [(1, 15), (5, 2), (8, 7)],

}


a, b, c = aStar(graph, 0, 10)

def contruirCamino(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) 
    path.reverse() 
    return path

path = contruirCamino(a, 0, 10)
print( "Ruta mas corta" , "----->", path, "con un costo de ----->", b[10], 
" \n con un orden de decolado de los primeros 5 de ---> ",a[2]) 
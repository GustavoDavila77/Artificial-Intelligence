graph = {
    0 : [1, 6, 7],
	1 : [4, 6],
	2 : [0, 1, 8],
	3 : [4, 5],
	4 : [],
	5 : [4],
	6 : [3, 4],
	7 : [3, 6],
	8 : [0, 7]
}

class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def enqueve(self, item):
        self.items.insert(0,item)

    def dequeve(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

def BFS(nodo):
    cola = Cola()
    cola.enqueve(nodo)
    visitados = []

    while not cola.estaVacia():
        v = cola.dequeve()
        print("decolados: "+str(v))

        for key in graph[v]:
            if key not in visitados:
                visitados.append(key)
                #print("visitados: "+str(key))
                cola.enqueve(key)

BFS(2)



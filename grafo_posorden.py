graph = {
    0 : [7, 6, 1],
	1 : [6, 4],
	2 : [8, 1, 0],
	3 : [5, 4],
	4 : [],
	5 : [4],
	6 : [4, 3],
	7 : [6, 3],
	8 : [7, 0]
}

def DFSGraph(v):
    visitados = []
    stack = []
    stackPostOrden = []
    stack.append(v)
    while stack:

        v = stack.pop()
        if v not in visitados:
            print("nodo actual ---", v)
            visitados.append(v)

        for key in graph[v]:
            if key not in visitados:

                stack.append(key)

    print("Lista de visitados --->", visitados)
    postOrden(visitados)

def postOrden(lista):
    post = []
    i = 0
    index = 0
    while lista:
        listValue = graph[lista[i]]
        index = i
        if i+1 != len(lista):
            index+=1

        if lista[index] in listValue:
            i+=1
        else:
            post.append(lista[i])
            lista.pop(i)
            i-=1
    print("lista en postOrden --->", post)





DFSGraph(2)
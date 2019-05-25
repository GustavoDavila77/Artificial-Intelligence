
import pants
from time import time #importamos la función time para capturar tiempos

#Nodes 1,   2,    3,  4,   5,    6 , 7
lenght = [
      [0  , 0  , 0, 98  , 0  ,0  ], #1  hirsova
      [0 , 0  , 0, 0  , 92 , 0 ], #2 lasi
      [0, 0, 0  , 0  , 0  , 0], #3 lugo
      [98  , 0  , 0  , 0  , 142, 0 ], #4 ursiceni
      [0  , 92  , 0  , 142, 0  , 0], #5 vaslui
      [0, 0  , 0, 0  , 0, 0 ], #6 zerin
      ]

def length_function(a, b):
    res = lenght[a-1][b-1]
    if res == 0:
        res = 100000
    #print("Distance from", a, "to", b, "=", res)
    return res

def main():
    nodes = [1, 2, 3, 4, 5, 6]
    world = pants.World(nodes, length_function)
    tiempo_inicial = time()
    solver = pants.Solver()
    solution = solver.solve(world)
    tiempo_final = time() 
 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
 
    print ('El tiempo de ejecucion fue:',tiempo_ejecucion) #En segundos

    print(solution.distance)
    print(solution.tour)    # Nodes visited in order
    #print(solution.path)    # Edges taken in order


if __name__ == '__main__':
    main()
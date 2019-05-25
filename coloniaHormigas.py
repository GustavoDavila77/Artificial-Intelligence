
import pants

#Nodes 1,   2,    3,  4,   5,    6 , 7
lenght = [
      [0  , 5  , 3.1, 0  , 0  , 5.2, 0  ], #1  costos para ir de 1 al nodo 1,2,3,4,5,6
      [5  , 0  , 4.9, 0  , 0  , 0  , 5.2], #2
      [3.1, 4.9, 0  , 0  , 6  , 3.2, 3  ], #3
      [0  , 0  , 0  , 0  , 5.5, 0  , 4.8], #4
      [0  , 0  , 6  , 5.5, 0  , 4.7, 0  ], #5
      [5.2, 0  , 3.2, 0  , 4.7, 0  , 0  ], #6
      [0  , 5.2, 3  , 4.8, 0  , 0  , 0  ]  #7
      ]

def length_function(a, b):
    res = lenght[a-1][b-1]
    if res == 0:
        res = 100000
    #print("Distance from", a, "to", b, "=", res)
    return res

def main():
    nodes = [1, 2, 3, 4, 5, 6, 7]
    world = pants.World(nodes, length_function)
    solver = pants.Solver()
    solution = solver.solve(world)
    print(solution.distance)
    print(solution.tour)    # Nodes visited in order
    #print(solution.path)    # Edges taken in order


if __name__ == '__main__':
    main()

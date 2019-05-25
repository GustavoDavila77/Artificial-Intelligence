#coding: utf-8
import pygame
import random

"""
falta

* guardar posición de recorrido y luego mostrar recorrido con sprite
* identificar en que pared se choco y hacer el llamado recursivo
"""
ancho=400
alto=400
verde= [0,255,0]
blanco = [255,255,255]
negro = [0,0,0]
rojo =[255,0,0]
azul = [0,0,255]
morado =[255,0,255]
azulclaro = [0,255,255]
amarillo = [255,255,0]
centro=[350,250]
pos =[0,0]

class Mapa():
    """docstring for Mapa"""
    def __init__(self,visitado=None,meta=None,posx=None,posy= None):
        self.visitado = visitado
        self.meta= meta #para identificar donde esta la galleta
        self.posx= posx
        self.posy= posy

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.head = False 
        self.body = False 

    def update(self):
        pass

class Cookie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(azulclaro)
        self.rect = self.image.get_rect()
        self.vel_x=0
        self.vel_y=0

#función que hace la busqueda en profundidad 
def busqueda(head,cookie,nodo,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla):

    reloj = pygame.time.Clock()

    pantalla.fill(negro)
    pantalla.blit(head.image,(nodo.posx,nodo.posy))
    pantalla.blit(cookie.image,(280,280))
    pygame.display.flip()
    reloj.tick(1)

    print("nodo en x: "+str(nodo.posx/40))
    print("nodo en y: "+str(nodo.posy/40))
    print("\n")
    
    if nodo.meta == True:
        print("encontre la solucion")
    else:
        nodo.visitado= True

        #mientras el nodo este dentro de la matriz 
        if (nodo.posy/tam_cuadrito)-1 >= 0 and (nodo.posy/tam_cuadrito)+1 < 10 and (nodo.posx/tam_cuadrito)-1 >= 0 and (nodo.posx/tam_cuadrito)+1 < 10:

            #el posy me indica en que fila esta
            #el posx me indica la columna
            nododer =  list_map[(nodo.posy/tam_cuadrito)][(nodo.posx/tam_cuadrito)+1] #se desplaza la columna en 1               
            nododown =  list_map[(nodo.posy/tam_cuadrito)+1][nodo.posx/tam_cuadrito]
            #print("nodo down en x: "+str(nododown.posx/40))
            #print("nodo down en y: "+str(nododown.posy/40))
            #print("\n")
            print("visitado?: "+str(nododown.visitado))
            print("\n")
            nodoizq =  list_map[nodo.posy/tam_cuadrito][(nodo.posx/tam_cuadrito)-1]
            nodoup =  list_map[(nodo.posy/tam_cuadrito)-1][nodo.posx/tam_cuadrito]
            

            #derecha
            if nododer.visitado != True:
                #print("der_inx: "+str(nododer.posx/40))
                #print("der_iny: "+str(nododer.posy/40))
                #print("\n")

                busqueda(head,cookie,nododer,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)

            #abajo
            
            elif nododown.visitado != True:
                #print("down_inx: "+str(nododown.posx/tam_cuadrito))
                #print("down_iny: "+str(nododown.posy/tam_cuadrito))
                #print("\n")

                busqueda(head,cookie,nododown,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)

            #izquierda
            
            elif nodoizq.visitado != True:
                print("izq_inx: "+str(nodoizq.posx/40))
                print("izq_iny: "+str(nodoizq.posy/40))
                print("\n")

                busqueda(head,cookie,nodoizq,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
            #arriba
            
            elif nodoup.visitado != True:
                print("up_inx: "+str(nodoup.posx/40))
                print("up_iny: "+str(nodoup.posy/40))
                print("\n")
                #sol.append([nodoup.posx,nodoup.posy])
                busqueda(head,cookie,nodoup,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
            
            #reloj.tick(2)

        else:
            print("se sale del rango")
            #print("nodo al salirse x: "+str(nodo.posx/40))
            #print("nodo al salirse y: "+str(nodo.posy/40))
            #nodo.meta = True #cambiarla por otra variable
            #mientras el nodo este dentro de la matriz 
            if (nodo.posy/tam_cuadrito)+1 < 10 :
                nododown =  list_map[(nodo.posy/tam_cuadrito)+1][nodo.posx/tam_cuadrito]
                busqueda(head,cookie,nododown,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
            elif (nodo.posx/tam_cuadrito)-1 >= 0:
                nodoizq =  list_map[nodo.posy/tam_cuadrito][(nodo.posx/tam_cuadrito)-1]
                busqueda(head,cookie,nodoizq,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
            elif (nodo.posy/tam_cuadrito)-1 >= 0:
                nodoup =  list_map[(nodo.posy/tam_cuadrito)-1][nodo.posx/tam_cuadrito]
                busqueda(head,cookie,nodoup,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    tam_cuadrito= ancho/10
    sol= []
    #matriz de objetos
    list_map=[]
    for i in range(10):
        list_pos=[]
        for j in range(10):
            mapa= Mapa()
            mapa.posx = j*tam_cuadrito
            mapa.posy = i*tam_cuadrito
            mapa.visitado = False
            mapa.meta = False
            list_pos.append(mapa)
        list_map.append(list_pos)

    #posición de la galleta
    list_map[7][7].meta = True

    #posición inicial
    pos_inx= 2
    pos_iny= 4
    #creación del grupo culebras
    snakes = pygame.sprite.Group()
    head = Snake()
    head.rect.x= list_map[pos_inx][pos_iny].posx
    head.rect.y= list_map[pos_inx][pos_iny].posy
    snakes.add(head)

    #creación del grupo galletas
    cookies = pygame.sprite.Group()
    cookie = Cookie()
    cookie.rect.x = list_map[1][4].posx
    cookie.rect.y = list_map[1][4].posy
    cookies.add(cookie)

    #fuente = pygame.font.Font(None,30) #none, se especifica el tipo de fuente y tamaño
    reloj = pygame.time.Clock()
    busqueda(head,cookie,list_map[pos_inx][pos_iny],list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla) #que retorne la pos
    
"""
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
"""
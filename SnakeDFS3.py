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

def movDer(nodo,tam_cuadrito):
    con = 0
    if (nodo.posx/tam_cuadrito)+1 < 10 :
        con +=1
        nododer =  list_map[(nodo.posy/tam_cuadrito)][(nodo.posx/tam_cuadrito)+1] #se desplaza la columna en 1
        if nododer.visitado != True:
            con += 1

    return con 

def movDown(nodo,tam_cuadrito):
    con = 0
    if (nodo.posy/tam_cuadrito)+1 < 10 :
        con +=1
        nododown =  list_map[(nodo.posy/tam_cuadrito)+1][nodo.posx/tam_cuadrito]
        if nododown.visitado != True:
            con += 1

    return con

def movIzq(nodo,tam_cuadrito):
    con = 0
    if (nodo.posx/tam_cuadrito)-1 >= 0 :
        con +=1
        nodoizq =  list_map[nodo.posy/tam_cuadrito][(nodo.posx/tam_cuadrito)-1]
        if nodoizq.visitado != True:
            con += 1

    return con

def movUp(nodo,tam_cuadrito):
    con = 0
    if (nodo.posy/tam_cuadrito)-1 >= 0 :
        con +=1
        nodoup =  list_map[(nodo.posy/tam_cuadrito)-1][nodo.posx/tam_cuadrito]
        if nodoup.visitado != True:
            con += 1
    return con

#función que hace la busqueda en profundidad 
def busqueda(head,cookie,nodo,list_map,tam_cuadrito,pantalla):

    reloj = pygame.time.Clock()

    pantalla.fill(negro)
    pantalla.blit(head.image,(nodo.posx,nodo.posy))
    pantalla.blit(cookie.image,(cookie.rect.x,cookie.rect.y))
    pygame.display.flip()
    reloj.tick(10)

    print("nodo en x: "+str(nodo.posx/40))
    print("nodo en y: "+str(nodo.posy/40))
    print("\n")
    
    if nodo.meta == True:
        print("Encontre solucion")
    else:
        nodo.visitado= True

        #el posy me indica en que fila esta
        #el posx me indica la columna

        #moverse a la derecha
        if movDer(nodo,tam_cuadrito) == 2:
            nododer =  list_map[(nodo.posy/tam_cuadrito)][(nodo.posx/tam_cuadrito)+1] #se desplaza la columna en 1
            busqueda(head,cookie,nododer,list_map,tam_cuadrito,pantalla)

        #moverse abajo
        elif movDown(nodo,tam_cuadrito) == 2:
            nododown =  list_map[(nodo.posy/tam_cuadrito)+1][nodo.posx/tam_cuadrito]
            busqueda(head,cookie,nododown,list_map,tam_cuadrito,pantalla)

        #moverse a la izquierda
        elif movIzq(nodo,tam_cuadrito) == 2:
            nodoizq =  list_map[nodo.posy/tam_cuadrito][(nodo.posx/tam_cuadrito)-1]
            busqueda(head,cookie,nodoizq,list_map,tam_cuadrito,pantalla)

        #moverse arriba
        elif movUp(nodo,tam_cuadrito) == 2:
            nodoup =  list_map[(nodo.posy/tam_cuadrito)-1][nodo.posx/tam_cuadrito]
            busqueda(head,cookie,nodoup,list_map,tam_cuadrito,pantalla)

        else:
            print("no se pudo ningun movimiento")

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
    poscook_fila = 7
    poscook_columna = 3
    list_map[poscook_fila][poscook_columna].meta = True

    #posición inicial snake
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
    cookie.rect.x = poscook_columna*40
    cookie.rect.y = poscook_fila*40
    cookies.add(cookie)

    #fuente = pygame.font.Font(None,30) #none, se especifica el tipo de fuente y tamaño
    reloj = pygame.time.Clock()
    busqueda(head,cookie,list_map[pos_inx][pos_iny],list_map,tam_cuadrito,pantalla) #que retorne la pos
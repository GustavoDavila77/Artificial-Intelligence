#coding: utf-8
import pygame
import random

"""
falta

* guardar posición de recorrido y luego mostrar recorrido con sprite
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

    #pygame.draw.line(pantalla,blanco,[40,0],[40,alto])
    #pygame.display.flip()
    """
    for i in range(1,10):
        for j in range(1,10):
            pygame.draw.line(pantalla,blanco,[40*j,0],[40*j,alto])
            pygame.display.flip()
        pygame.draw.line(pantalla,blanco,[0,40*i],[ancho,40*i])
        pygame.display.flip()
    """ 
    reloj = pygame.time.Clock()

    pantalla.fill(negro)
    pantalla.blit(head.image,(nodo.posx,nodo.posy))
    pantalla.blit(cookie.image,(280,280))
    pygame.display.flip()
    reloj.tick(1)
    
    if nodo.meta == True:
        print("encontre la solucion")
    else:
        while nodo.meta != True:
            nodo.visitado= True

            #mientras el nodo este dentro de la matriz 
            if (nodo.posy/tam_cuadrito)-1 >= 0 and (nodo.posy/tam_cuadrito)+1 < 10 and (nodo.posx/tam_cuadrito)-1 >= 0 and (nodo.posx/tam_cuadrito)+1 < 10:

                #derecha
                nododer =  list_map[(nodo.posx/tam_cuadrito)][(nodo.posy/tam_cuadrito)+1] #se desplaza la columna en 1
                if nododer.visitado != True:
                    print("der_inx: "+str(nododer.posx/40))
                    print("der_iny: "+str(nododer.posy/40))
                    print("\n")
                    #head.rect.x = nododer.posx
                    #head.rect.y = nododer.posy
                    """
                    pantalla.fill(negro)
                    pantalla.blit(head.image,(nododer.posx,nododer.posy))
                    pygame.display.flip()
                    reloj.tick(1)
                    """
                    busqueda(head,cookie,nododer,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)

                #izquierda
                nodoizq =  list_map[nodo.posx/tam_cuadrito][(nodo.posy/tam_cuadrito)-1]
                if nodoizq.visitado != True:
                    print("izq_inx: "+str(nodoizq.posx/40))
                    print("izq_iny: "+str(nodoizq.posy/40))
                    print("\n")
                    #head.rect.x = nodoizq.posx
                    #head.rect.y = nodoizq.posy
                    """
                    pantalla.fill(negro)
                    pantalla.blit(head.image,(nodoizq.posx,nodoizq.posy))
                    pygame.display.flip()
                    reloj.tick(1)
                    """
                    busqueda(head,cookie,nodoizq,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
                #arriba
                nodoup =  list_map[(nodo.posx/tam_cuadrito)-1][nodo.posy/tam_cuadrito]
                if nodoup.visitado != True:
                    print("up_inx: "+str(nodoup.posx/40))
                    print("up_iny: "+str(nodoup.posy/40))
                    print("\n")
                    #sol.append([nodoup.posx,nodoup.posy])
                    #head.rect.x = nodoup.posx
                    #head.rect.y = nodoup.posy
                    """
                    pantalla.fill(negro)
                    pantalla.blit(head.image,(nodoup.posx,nodoup.posy))
                    pygame.display.flip()
                    reloj.tick(1)
                    """
                    busqueda(head,cookie,nodoup,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
                #abajo
                nododown =  list_map[(nodo.posx/tam_cuadrito)+1][nodo.posy/tam_cuadrito]
                if nododown.visitado != True:
                    print("down_inx: "+str(nododown.posx/tam_cuadrito))
                    print("down_iny: "+str(nododown.posy/tam_cuadrito))
                    print("\n")
                    #head.rect.x = nododown.posx
                    #head.rect.y = nododown.posy
                    """
                    pantalla.fill(negro)
                    pantalla.blit(head.image,(nododown.posx,nododown.posy))
                    pygame.display.flip()
                    reloj.tick(1)
                    """
                    busqueda(head,cookie,nododown,list_map,pos_inx,pos_iny,sol,tam_cuadrito,pantalla)
                reloj.tick(2)

            if nodo.meta == True:
                print ("solucion up")
                #print("esta en x = "+str(nodo.posx/40))
                #print("esta en y = "+str(nodo.posy/40))
            else:
                print("por aqui no es")
                nodo.meta = True

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
    puntos = 0
    reloj = pygame.time.Clock()
    fin=False



    while not fin:
        for event in pygame.event.get():          #Eventos que pasan cada que...
            if event.type == pygame.QUIT:
                fin=True

        #snakes.update()
        head.busqueda(list_map[pos_inx][pos_iny],list_map,pos_inx,pos_iny) #que retorne la pos
        cookies.update()
        pantalla.fill(negro)
        head.draw(pantalla)
        cookies.draw(pantalla) 

        texto = fuente.render("puntos: "+str(puntos),True,morado)     
        pantalla.blit(texto,(50,20))

        pygame.display.flip()
        reloj.tick(20)
    """

    #imprimir matriz de nodos del mapa
    """
    for i in range(10):
        for j in range(10):
            print("meta: "+str(list_map[i][j].meta))
            print("posx: "+str(list_map[i][j].posx))
            print("posy: "+str(list_map[i][j].posy))
        print("\n")
    """
    #prueba
    """
        con = 0
        while(con < 10):
            nododer =  list_map[pos_inx][con]
            print("nodox: "+str(nododer.posx))
            print("nodoy: "+str(nododer.posy))
            if nododer.visitado != True:
                head.rect.x = nododer.posx
                head.rect.y = nododer.posy
                pantalla.fill(negro)
                pantalla.blit(head.image,(nododer.posx,nododer.posy))
                pygame.display.flip()
            con += 1
            reloj.tick(2)
    """
#coding: utf-8
import pygame
import random

ancho=700
alto=500
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


class Jugadores(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.vel_x=0
        self.vel_y=0

    def update(self):

        if self.rect.x >= 200:
            self.rect.x = 200
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > alto-self.rect.height:
            self.rect.y = alto-self.rect.height
        self.rect.y+=self.vel_y
        self.rect.x += self.vel_x

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    p1 = [200,100]
    p2 = [400,100]
    p3 = [200,400]
    p4 = [400,400]

    objeto = Objetos(pantalla)

    jugadores = pygame.sprite.Group()
    j1 = Jugadores()
    j1.rect.x=100
    j1.rect.y=100
    jugadores.add(j1)
    fuente = pygame.font.Font(None,30) #none, se especifica el tipo de fuente y tamaño
    fuente2 = pygame.font.Font(None,80) #none, se especifica el tipo de fuente y tamaño

    n=10
    salud = 200
    puntos = 0
    congan = 0

    reloj = pygame.time.Clock()

    fin=False
    while not fin:
        for event in pygame.event.get():          #Eventos que pasan cada que...
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    j1.vel_y= 4
                    j1.vel_x = 0
                if event.key == pygame.K_UP:
                    j1.vel_y = -4
                    j1.vel_x= 0
                if event.key == pygame.K_LEFT:
                    j1.vel_x = -4
                    j1.vel_y = 0
                if event.key == pygame.K_RIGHT:
                    j1.vel_x = 4
                    j1.vel_y = 0
                #cada vez que se oprima b, se crea una bala
                if event.key == pygame.K_b:
                    b=bala()
                    b.rect.x=j1.rect.x + j1.rect.width
                    b.rect.y=j1.rect.y + j1.rect.height/2
                    balas.add(b) #se añade b al grupo de balas

            if event.type == pygame.KEYUP:
                j1.vel_y=0
                j1.vel_x =0

        jugadores.update()
        pantalla.fill(negro)
        if puntos == 10:
            texto2 = fuente2.render("Ganaste",True,verde)
            pantalla.blit(texto2,(250,200))
            congan += 1
        else:
            objeto.dib_rect(pantalla,salud)
            jugadores.draw(pantalla)
            texto = fuente.render("puntos: "+str(puntos),True,morado)
            texto3 = fuente.render("salud: ",True,morado)
            pantalla.blit(texto,(50,20))
            pantalla.blit(texto3,(50,50))

        if congan >= 100 or salud <= 0:
            fin = True
        pygame.display.flip()
        reloj.tick(50)

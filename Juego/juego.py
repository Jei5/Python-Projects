import pygame
import random 
from math import *
# Inicializa pygame
pygame.init()
#Creo La Pantalla
ventana = pygame.display.set_mode((800,600))
#Coloco Titulo A La Ventana
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("espacio.png")

#variables Para El Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_cambio = 0

#Variables Para El Enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 1
enemigo_y_cambio = 50

#Variable Para Las Balas
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#Puntaje
puntaje = 0

#Funcion para colocar las imagenes dentro del escenario

def jugador(x,y):
    ventana.blit(img_jugador,(x,y))

def enemigo(x,y):
    ventana.blit(img_enemigo,(x,y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    ventana.blit(img_bala, (x+26,y+10))

def detectar_colision(x1,y1,x2,y2):
    distancia = sqrt(pow(x1-x2,2) + pow(y2-y1,2))
    if distancia < 27:
        return True
    else:
        return False

#Ejecucion Del Juego
se_ejecuta = True
while se_ejecuta:
    ventana.blit(fondo,(0,0))
    # Ciclo Para Movimiento Y Fin De Juego
    for evento in pygame.event.get():
        #Evento Cierre
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #Evento Presionar Tecla
        if evento.type == pygame.KEYDOWN: 
            if evento.key == pygame.K_LEFT:
                jugador_cambio = -2
            if evento.key == pygame.K_RIGHT:
                jugador_cambio = +2
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_cambio = 0

    #Modifico Posicion Del Jugador
    jugador_x += jugador_cambio
    #Mantener jugador dentro de los bordes
    if jugador_x <=0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736    

    #Modifico Ubicacion Del Enemigo
    enemigo_x += enemigo_x_cambio

    if enemigo_x <=0:
        enemigo_x_cambio = 1
        enemigo_y_cambio += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio 
    #Movimiento De La Bala
    if bala_y <= -32:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio
    #colision
    colision = detectar_colision(enemigo_x,enemigo_y,bala_x,bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigo_x = random.randint(0,736)
        enemigo_y = random.randint(20,200)

    #Llamo La Funcion Jugador
    jugador(jugador_x,jugador_y)

    #Llamo La Funcion Enemigo
    enemigo(enemigo_x,enemigo_y)

    #Actualizar
    pygame.display.update()
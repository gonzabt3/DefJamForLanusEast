import pygame

from personajes import Fonte
from personajes import Licha
from personajes import Pablo

import seleccion

from Fondo import Fondo
# importo clases
from LifeBar import LifeBar
from Peleador import Peleador
from Time import Time
from codigo.personajes import Enzo
from menu import Menu
import controles
import menuRetry

contadorMuerto=0
# def Pelea(a,b):
def Pelea(a, b):
    pygame.init()
    pantalla = pygame.display.set_mode((750, 500))
    salir = False
    reloj1 = pygame.time.Clock()

    #musica
    pygame.mixer.music.load("sonidos/musica.mp3")

    (Jugador1,Jugador2)=selectorPersonaje(a,b)



    lifeBar1 = LifeBar(Jugador1.texto,Jugador1.cabeza,1)
    player1 = Peleador(Jugador1.nombre,Jugador1.imagenParadoArray,Jugador1.imagenMovimientoArray,Jugador1.imagenPunioArray,
                       Jugador1.imagenPatadaArray,Jugador1.imagenDefensa1Array,Jugador1.imagenHeridoArray,Jugador1.imagenMuertoArray,Jugador1.imagenMuertoSinCabezaArray,lifeBar1,1,Jugador1.imagenFestejo)

    lifeBar2=LifeBar(Jugador2.texto,Jugador2.cabeza,2)
    player2 = Peleador(Jugador2.nombre,Jugador2.imagenParadoArray, Jugador2.imagenMovimientoArray, Jugador2.imagenPunioArray,
                       Jugador2.imagenPatadaArray, Jugador2.imagenDefensa1Array,Jugador2.imagenHeridoArray,Jugador2.imagenMuertoArray,Jugador2.imagenMuertoSinCabezaArray,lifeBar2,2,Jugador2.imagenFestejo)
    fondo1=Fondo()
    vx1, vy1 = 0, 0
    vx2, vy2 = 0, 0
    velocidad = 7
    t = 0

    #BOTONES PLAYER 1
    c_apretada, v_apretada, upsigueapretada, downsigueapretada,q_apretada,w_apretada,e_apretada = False, False, False, False,False,False,False
    fightMove1 = False
    defenseMove1 = False

    #BOTONES PLAYER 2
    left_apretada,right_apretada,cuatro_apretada,cinco_apretada,seis_apretada=False,False,False,False,False
    fightMove2 = False
    defenseMove2 = False

    #menu de retry
    opciones = [
        ("Elegir Personaje", selectPersonaje),
        ("Salir", salir_del_programa)
    ]
    menuReinicio = menuRetry.MenuRetry(opciones)


    # pygame.mixer.music.play(2)
    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

            if event.type == pygame.KEYDOWN:
                #///////PLAYER1
                if event.key == pygame.K_c:
                    c_apretada = True
                    vx1 = -velocidad
                if event.key == pygame.K_v:
                    v_apretada = True
                    vx1 = velocidad
                # if event.key == pygame.K_UP:
                #     upsigueapretada = True
                #     vy1 = -velocidad
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = True
                #     vy1 = velocidad
                if event.key == pygame.K_q:
                    q_apretada = True
                    fightMove1=True
                if event.key == pygame.K_w:
                    w_apretada = True
                    fightMove1=True
                if event.key == pygame.K_e:
                    e_apretada = True
                    defenseMove1=True
                #////PLAYER2 DOWN
                if event.key == pygame.K_LEFT:
                    left_apretada = True
                    vx2 = -velocidad
                if event.key == pygame.K_RIGHT:
                    right_apretada = True
                    vx2 = velocidad
                # if event.key == pygame.K_UP:
                #     upsigueapretada = True
                #     vy1 = -velocidad
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = True
                #     vy1 = velocidad
                if event.key == pygame.K_KP4:
                    cuatro_apretada = True
                    fightMove2=True
                if event.key == pygame.K_KP5:
                    cinco_apretada = True
                    fightMove2=True
                if event.key == pygame.K_KP6:
                    seis_apretada = True
                    defenseMove2=True
            # ///////player1 UP
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    c_apretada = False
                    if v_apretada:
                        vx1 = velocidad
                    else:
                        vx1 = 0
                if event.key == pygame.K_v:
                    v_apretada = False
                    if c_apretada:
                        vx1 = -velocidad
                    else:
                        vx1 = 0
                # if event.key == pygame.K_UP:
                #     upsigueapretada = False
                #     if downsigueapretada:
                #         vy1 = velocidad
                #     else:
                #         vy1 = -0
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = False
                #     if upsigueapretada:
                #         vy1 = -velocidad
                #     else:
                #         vy1 = 0
                if event.key == pygame.K_q:
                    q_apretada=False
                    fightMove1 = False
                if event.key == pygame.K_w:
                    w_apretada=False
                    fightMove1=False
                if event.key == pygame.K_e:
                    e_apretada=False
                    defenseMove1=False
                #/////////////player 2 down
                if event.key == pygame.K_LEFT:
                    left_apretada = False
                    if right_apretada:
                        vx2 = velocidad
                    else:
                        vx2 = 0
                if event.key == pygame.K_RIGHT:
                    right_apretada = False
                    if left_apretada:
                        vx2 = -velocidad
                    else:
                        vx2 = 0
                # if event.key == pygame.K_UP:
                #     upsigueapretada = False
                #     if downsigueapretada:
                #         vy1 = velocidad
                #     else:
                #         vy1 = -0
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = False
                #     if upsigueapretada:
                #         vy1 = -velocidad
                #     else:
                #         vy1 = 0
                if event.key == pygame.K_KP4:
                    cuatro_apretada=False
                    fightMove2 = False
                if event.key == pygame.K_KP5:
                    cinco_apretada=False
                    fightMove2=False
                if event.key == pygame.K_KP6:
                    seis_apretada=False
                    defenseMove2=False

        tiempo2=Time()


        reloj1.tick(12) #reloj
        # pantalla.fill((200, 200, 200)) #pantalla blanca

        fondo1.update(pantalla)

        lifeBar1.update(pantalla)
        lifeBar2.update(pantalla)
        player1.update(pantalla, vx1, vy1,fightMove1,q_apretada,w_apretada,defenseMove1,e_apretada,lifeBar1,player2)
        player2.update(pantalla, vx2, vy2, fightMove2, cuatro_apretada, cinco_apretada, defenseMove2, seis_apretada, lifeBar2,player1)
        fondo1.pintarFinishHim(pantalla,player1,player2)
        tiempo2.update(pantalla)
        fondo1.pintarFight(pantalla)

        if(player1.estado==6 or player2.estado==6):
            global contadorMuerto
            contadorMuerto += 1

            if (contadorMuerto >= 75):  # este if esta para para la pelea y lanzar el menu para volver para atras
                menuReinicio.actualizar()
                menuReinicio.imprimir(pantalla)

        pygame.display.update()

    pygame.quit()


def salir_del_programa():
    import sys
    sys.exit(0)

def selectPersonaje():

    a,b=seleccion.main()
    Pelea(a,b)

def Pass():
    pass

def selectorPersonaje(a,b):
    if(a==0):
        player1 = Enzo
    if(a==1):
        player1=Pablo
    if(a==2):
        player1=Fonte
    if(a==3):
        player1=Licha
    if(b==0):
        player2 = Enzo
    if (b == 1):
        player2 = Pablo
    if (b == 2):
        player2 = Fonte
    if (b == 3):
        player2 = Licha

    return (player1,player2)

def llamadorControl():
    controles.menuControles()


def main():



    salir = False
    opciones = [
        ("Jugar", selectPersonaje),
        ("Controles",llamadorControl),
        ("Salir", salir_del_programa)
    ]

    pygame.font.init()
    screen = pygame.display.set_mode((600, 500))
    fondo = pygame.image.load("imagenes/defjam.jpg").convert()
    fondoEstudio = pygame.image.load("imagenes/studio.png").convert()
    menu = Menu(opciones)
    fondoFlag=True

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True

        if(fondoFlag==True):
            screen.blit(fondoEstudio, (0, 0))
            pygame.display.flip()
            pygame.time.delay(3000)
            fondoFlag=False

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)



main()
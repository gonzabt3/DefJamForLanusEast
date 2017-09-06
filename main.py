import pygame

#importo clases
from LifeBar import LifeBar
from Fondo import Fondo
from Peleador import Peleador
import Fonte
from threading import Timer


def main():

    pygame.init()
    pantalla = pygame.display.set_mode((750, 500))
    salir = False
    reloj1 = pygame.time.Clock()

    lifeBar1 = LifeBar(Fonte.texto,Fonte.cabeza,1)
    player1 = Peleador(Fonte.imagenParadoArray,Fonte.imagenMovimientoArray,Fonte.imagenPunioArray,Fonte.imagenPatadaArray,Fonte.imagenDefensa1Array,lifeBar1)
    fondo1=Fondo()
    vx, vy = 0, 0
    velocidad = 7
    t = 0
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada,q_apretada,w_apretada,e_apretada = False, False, False, False,False,False,False
    fightMove=False
    defenseMove=False
    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = True
                    vx = -velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = True
                    vx = velocidad
                # if event.key == pygame.K_UP:
                #     upsigueapretada = True
                #     vy = -velocidad
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = True
                #     vy = velocidad
                if event.key == pygame.K_q:
                    q_apretada = True
                    fightMove=True
                if event.key == pygame.K_w:
                    w_apretada = True
                    fightMove=True
                if event.key == pygame.K_e:
                    e_apretada = True
                    defenseMove=True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = False
                    if rightsigueapretada:
                        vx = velocidad
                    else:
                        vx = 0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = False
                    if leftsigueapretada:
                        vx = -velocidad
                    else:
                        vx = 0
                # if event.key == pygame.K_UP:
                #     upsigueapretada = False
                #     if downsigueapretada:
                #         vy = velocidad
                #     else:
                #         vy = -0
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = False
                #     if upsigueapretada:
                #         vy = -velocidad
                #     else:
                #         vy = 0
                if event.key == pygame.K_q:
                    q_apretada=False
                    fightMove = False
                if event.key == pygame.K_w:
                    w_apretada=False
                    fightMove=False
                if event.key == pygame.K_e:
                    e_apretada=False
                    defenseMove=False

        reloj1.tick(12) #relog
        pantalla.fill((200, 200, 200)) #pantalla blanca
        fondo1.update(pantalla)
        lifeBar1.update(pantalla)
        player1.update(pantalla, vx, vy,fightMove,q_apretada,w_apretada,defenseMove,e_apretada,lifeBar1)
        pygame.display.update()

    pygame.quit()

main()



import pygame
from pygame.locals import *

def menuControles():


    pygame.font.init()
    screen = pygame.display.set_mode((600, 500))
    imagenControles = pygame.image.load("imagenes/controles.png").convert()

    salir=False
    while not salir:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True
        k = pygame.key.get_pressed()
        if k[K_SPACE]:
            salir=True

        screen.blit(imagenControles, (0, 0))

        pygame.display.flip()
        pygame.time.delay(10)



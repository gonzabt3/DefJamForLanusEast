import pygame

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("imagenes/fondo/enzoHause.gif").convert_alpha()
        self.rect=self.imagen.get_rect()

    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)

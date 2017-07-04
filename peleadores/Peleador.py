import pygame

class Peleador(pygame.sprite.Sprite):
    def __init__(self,imagen,nombre,vida,golpe):
        self.nombre=nombre
        self.vida=vida
        self.golpe=golpe
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)
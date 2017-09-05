import pygame

class LifeBar(pygame.sprite.Sprite):
    def __init__(self,texto,cabeza):
        self.marco=pygame.image.load("imagenes/lifebar/life_bar_marco.png").convert_alpha()
        self.relleno=pygame.image.load("imagenes/lifebar/life_bar_relleno.png").convert_alpha()
        self.pixelesBarra=228

        self.rect = self.marco.get_rect()
        self.rect.top, self.rect.left = (10, 10)

        self.rectRelleno=self.relleno.get_rect()
        self.rectRelleno.top,self.rectRelleno.left=(54,76)

        self.texto=texto
        self.textRect = self.texto.get_rect()
        self.textRect.top, self.textRect.left = (60, 70)

        self.cabeza=cabeza
        self.cabezaRect=self.cabeza.get_rect()
        self.cabezaRect.top, self.cabezaRect.left = (3, -5)

    def update(self,pantalla):
        pantalla.blit(self.marco, self.rect)
        pantalla.blit(self.relleno, self.rectRelleno)
        pantalla.blit(self.texto,self.textRect)
        pantalla.blit(self.cabeza, self.cabezaRect)

    def actualizarBar(self,damage):
        damagePixeles = (damage * self.pixelesBarra) / 100
        self.pixelesBarra = self.pixelesBarra - damagePixeles
        self.relleno = pygame.transform.smoothscale(self.relleno, (self.pixelesBarra, 5))
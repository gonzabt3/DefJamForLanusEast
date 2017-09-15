import pygame

class LifeBar(pygame.sprite.Sprite):
    def __init__(self,texto,cabeza,player):
        self.marco=pygame.image.load("imagenes/lifebar/life_bar_marco.png").convert_alpha()
        self.relleno=pygame.image.load("imagenes/lifebar/life_bar_relleno.png").convert_alpha()
        self.pixelesBarra=228

        if(player==1):

            marcoPosicion=[10,10]
            rellenoPosicion = [54,76]
            textoPosicion = [60,70]
            cabezaPosicion=[3,-5]

            self.cabeza = cabeza
        if (player == 2):

            self.marco=pygame.transform.flip(self.marco,True,False)
            self.relleno=pygame.transform.flip(self.relleno,True,False)
            self.cabeza=pygame.transform.flip(cabeza,True,False)

            marcoPosicion = [10, 425]
            rellenoPosicion = [54, 440]
            textoPosicion = [60, 575]
            cabezaPosicion = [5, 649]

        self.rect = self.marco.get_rect()
        self.rect.top, self.rect.left = (marcoPosicion[0], marcoPosicion[1])

        self.rectRelleno=self.relleno.get_rect()
        self.rectRelleno.top,self.rectRelleno.left=(rellenoPosicion[0], rellenoPosicion[1])

        self.texto=texto
        self.textRect = self.texto.get_rect()
        self.textRect.top, self.textRect.left = (textoPosicion[0], textoPosicion[1])


        self.cabezaRect=self.cabeza.get_rect()
        self.cabezaRect.top, self.cabezaRect.left = (cabezaPosicion[0], cabezaPosicion[1])

    def update(self,pantalla):
        pantalla.blit(self.marco,self.rect)
        pantalla.blit(self.relleno,self.rectRelleno)
        pantalla.blit(self.texto,self.textRect)
        pantalla.blit(self.cabeza, self.cabezaRect)

    def actualizarBar(self,damage):
        damagePixeles = (damage * self.pixelesBarra) / 100
        self.pixelesBarra = self.pixelesBarra - damagePixeles
        self.relleno = pygame.transform.smoothscale(self.relleno, (self.pixelesBarra, 5))
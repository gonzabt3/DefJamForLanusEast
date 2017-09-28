import pygame

class select:
    def __init__(self):

        self.posicion
        self.select1=pygame.image.load("selectScreen/select1.jpg").convert_alpha()
        self.select2 = pygame.image.load("selectScreen/select2.jpg").convert_alpha()
        self.selectScreen = pygame.image.load("selectScreen/selectScreen.jpg").convert_alpha()


    def pantalla(self):
        salir = False


        pygame.font.init()
        screen = pygame.display.set_mode((600, 500))
        fondo = self.selectScreen


        while not salir:

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    salir = True

            screen.blit(fondo, (0, 0))


            pygame.display.flip()
            pygame.time.delay(10)
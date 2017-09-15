import pygame

class Time(str):
    def __init__(self):
        self.fuente=pygame.font.SysFont("Super Mario Bros.",50,True,False)
        self.tiempo="asd",
        # self.reloj=pygame.time.Clock()


    def update(self,pantalla):
        # pygame.init()
        # info=self.fuente.render(self.tiempo,0,(0,0,230))
        #
        # pantalla.blit(info,(340,30))
        # for i in range(100):
        #     cadena=str(i)
        #     info = self.fuente.render(cadena, 0, (0, 0, 230))
        #     pantalla.blit(info, (340, 30))
        # for i in range(1000):
            contador=self.fuente.render(str(pygame.time.get_ticks()/1000),0,(0,0,0))
            # contador = self.fuente.render("asd", 0, (0, 0, 230))
            pantalla.blit(contador,(340,30))

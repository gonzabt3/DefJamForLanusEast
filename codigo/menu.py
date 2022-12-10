# -*- coding: utf-8 -*-
#
# autor: Hugo Ruscitti
# web: www.losersjuegos.com.ar
# licencia: GPL 2

import pygame
from pygame.locals import *
pygame.init()
opcion=pygame.mixer.Sound("sonidos/opcion.wav")
click=pygame.mixer.Sound("sonidos/click.wav")


class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = opciones

        self.font = pygame.font.Font("fuentesMK/mk2.ttf", 50)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
                opcion.play()
            elif k[K_DOWN]:
                self.seleccionado += 1
                opcion.play()
            elif k[K_m]:
                click.play()
                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print ("Selecciona la opción '%s'." %(titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_m]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 30
        x = 230
        y = 275
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (200, 0, 0)
            else:
                color = (250, 244, 227)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


def comenzar_nuevo_juego():
    print ("Función que muestra un nuevo juego.")

def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print ("Función que muestra los creditos del programa.")

def salir_del_programa():
    import sys
    print ("Gracias por utilizar este programa.")
    sys.exit(0)


    if __name__ == '__main__':

     salir = False
     opciones = [
         ("Jugar", comenzar_nuevo_juego),
         ("Salir", salir_del_programa)
         ]

     pygame.font.init()
     screen = pygame.display.set_mode((600, 500))
     fondo = pygame.image.load("defjam.jpg").convert()
     menu = Menu(opciones)

     while not salir:

         for e in pygame.event.get():
             if e.type == QUIT:
                 salir = True

         screen.blit(fondo, (0, 0))
         menu.actualizar()
         menu.imprimir(screen)

         pygame.display.flip()
         pygame.time.delay(10)

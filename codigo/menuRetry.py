# -*- coding: utf-8 -*-
#
# autor: Hugo Ruscitti
# web: www.losersjuegos.com.ar
# licencia: GPL 2

import pygame
from pygame.locals import *

opcion = pygame.mixer.Sound("sonidos/opcion.wav")
click = pygame.mixer.Sound("sonidos/click.wav")


class MenuRetry:
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
            elif k[K_RETURN]:
                click.play()
                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

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




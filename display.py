import piso  # Importamos el módulo que contiene la clase Celdas
import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_chessboard(matriz_celdas, tamCelda):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Ajustar la cámara para vista 3D en perspectiva
    M, N = len(matriz_celdas), len(matriz_celdas[0])  # Dimensiones de la matriz de celdas
    gluLookAt(M * tamCelda / 2, -N * tamCelda / 2, M * tamCelda,   # Posición de la cámara
              M * tamCelda / 2, N * tamCelda / 2, 0,               # Centro de la escena
              0, 0, 1)                                             # Dirección "arriba"

    # Dibujar el tablero en 3D usando la matriz de celdas
    for fila in matriz_celdas:
        for celda in fila:
            # Determinar el color de cada celda según sus atributos
            if celda.inicial:
                color = (1.0, 0.5, 0.0)  # Celda inicial con color especial
            elif celda.agente:
                color = (0.0, 0.0, 1.0)  # Celdas con agente en azul
            elif celda.basura:
                color = (1.0, 0.0, 0.0)  # Celdas con basura en rojo
            elif (celda.posicion[0] + celda.posicion[1]) % 2 == 0:
                color = (1.0, 1.0, 1.0)  # Celdas blancas
            else:
                color = (0.0, 0.0, 0.0)  # Celdas negras

            glColor3f(*color)
            x, y = celda.posicion[1] * tamCelda, celda.posicion[0] * tamCelda

            # Dibujar un cubo en lugar de un cuadrado para una vista 3D
            glBegin(GL_QUADS)
            # Cara superior
            glVertex3f(x, y, 0)
            glVertex3f(x + tamCelda, y, 0)
            glVertex3f(x + tamCelda, y + tamCelda, 0)
            glVertex3f(x, y + tamCelda, 0)
            
            # Cara inferior
            glVertex3f(x, y, -tamCelda/10)
            glVertex3f(x + tamCelda, y, -tamCelda/10)
            glVertex3f(x + tamCelda, y + tamCelda, -tamCelda/10)
            glVertex3f(x, y + tamCelda, -tamCelda/10)
            
            # Lado frontal
            glVertex3f(x, y, 0)
            glVertex3f(x + tamCelda, y, 0)
            glVertex3f(x + tamCelda, y, -tamCelda/10)
            glVertex3f(x, y, -tamCelda/10)
            
            # Lado trasero
            glVertex3f(x, y + tamCelda, 0)
            glVertex3f(x + tamCelda, y + tamCelda, 0)
            glVertex3f(x + tamCelda, y + tamCelda, -tamCelda/10)
            glVertex3f(x, y + tamCelda, -tamCelda/10)
            
            # Lado izquierdo
            glVertex3f(x, y, 0)
            glVertex3f(x, y + tamCelda, 0)
            glVertex3f(x, y + tamCelda, -tamCelda/10)
            glVertex3f(x, y, -tamCelda/10)
            
            # Lado derecho
            glVertex3f(x + tamCelda, y, 0)
            glVertex3f(x + tamCelda, y + tamCelda, 0)
            glVertex3f(x + tamCelda, y + tamCelda, -tamCelda/10)
            glVertex3f(x + tamCelda, y, -tamCelda/10)
            
            glEnd()

    pygame.display.flip()

def main(Options):
    pygame.init()
    global tamCelda 
    tamCelda = min(800 // Options.M, 800 // Options.N)
    pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)
    
    # Configurar la perspectiva 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, Options.M * tamCelda * 4)
    glMatrixMode(GL_MODELVIEW)

    # Crear la matriz de celdas con `piso.Celdas`
    matriz_celdas = piso.Celdas.matrizPosiciones(Options)
    # Configurar la celda inicial
    for fila in matriz_celdas:
        for celda in fila:
            celda.celdaInicial(celda.indice, Options)
            # Agregar condiciones para agentes y basuras si es necesario
            # e.g., celda.agente = True o celda.basura = True en función de índices específicos

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_chessboard(matriz_celdas, tamCelda)
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()

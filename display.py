import piso  # Importamos el módulo que contiene la clase Celdas
import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_trash(x, y, tamCelda):
    """Dibuja un cubo pequeño en gris que representa basura sobre una celda."""
    glColor3f(0.5, 0.5, 0.5)  # Color gris para la basura
    basura_size = tamCelda / 4  # Tamaño de la basura (pequeño cubo)
    basura_x = x + tamCelda / 2 - basura_size / 2
    basura_y = y + tamCelda / 2 - basura_size / 2
    basura_z = tamCelda / 10  # Elevado ligeramente sobre la celda

    glBegin(GL_QUADS)
    # Cara superior de la basura
    glVertex3f(basura_x, basura_y, basura_z)
    glVertex3f(basura_x + basura_size, basura_y, basura_z)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z)
    glVertex3f(basura_x, basura_y + basura_size, basura_z)
    
    # Cara inferior de la basura
    glVertex3f(basura_x, basura_y, basura_z - basura_size)
    glVertex3f(basura_x + basura_size, basura_y, basura_z - basura_size)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z - basura_size)
    glVertex3f(basura_x, basura_y + basura_size, basura_z - basura_size)
    
    # Lado frontal
    glVertex3f(basura_x, basura_y, basura_z)
    glVertex3f(basura_x + basura_size, basura_y, basura_z)
    glVertex3f(basura_x + basura_size, basura_y, basura_z - basura_size)
    glVertex3f(basura_x, basura_y, basura_z - basura_size)
    
    # Lado trasero
    glVertex3f(basura_x, basura_y + basura_size, basura_z)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z - basura_size)
    glVertex3f(basura_x, basura_y + basura_size, basura_z - basura_size)
    
    # Lado izquierdo
    glVertex3f(basura_x, basura_y, basura_z)
    glVertex3f(basura_x, basura_y + basura_size, basura_z)
    glVertex3f(basura_x, basura_y + basura_size, basura_z - basura_size)
    glVertex3f(basura_x, basura_y, basura_z - basura_size)
    
    # Lado derecho
    glVertex3f(basura_x + basura_size, basura_y, basura_z)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z)
    glVertex3f(basura_x + basura_size, basura_y + basura_size, basura_z - basura_size)
    glVertex3f(basura_x + basura_size, basura_y, basura_z - basura_size)
    
    glEnd()

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

            # Dibujar basura si celda.basura es True
            if celda.basura:
                draw_trash(x, y, tamCelda)

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

    # Generar basuras aleatorias
    piso.Celdas.generarBasurasAleatorias(matriz_celdas, Options.Basuras)

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

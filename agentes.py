# Agentes.py

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (1.0, 1, 0.0)  # Color naranja (RGB en OpenGL) (1.0, 0.5, 0.0)
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.5)  # Posición del agente en el plano
        glScalef(0.2, 0.2, 0.2)  # Tamaño del agente

        # Dibujar un cubo simple para representar el agente
        glBegin(GL_QUADS)
        glColor3f(*self.color)
        for vertex in [(0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5)]:
            glVertex3f(*vertex)
        glEnd()
        glPopMatrix()

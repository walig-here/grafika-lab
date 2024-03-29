from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from Shapes import ColorRgb, Triangle, Vertex, Line


class Renderer:
    def __init__(self, frame, backgorund_color: ColorRgb):
        # Lista kształtów do wyrenderowania
        self.shapes_to_render = []

        # Ustalenie koloru ramki (który ma ona po wyczyszczeniu jej bufora). Parametry:
        # * nasycenie czerwonym
        # * nasycenie zielonym
        # * nasycenie niebieskim
        # * przeźroczystość
        glClearColor(backgorund_color.red/255, backgorund_color.green/255, backgorund_color.blue/255, 1.0)

        # Włączenie bufora głębi
        glEnable(GL_DEPTH_TEST)

    def drawTriangle(self, triangle : Triangle):
        # Rozpoczęce rysowania trójkąta
        glBegin(GL_TRIANGLES)
        for vertex in triangle.verticies:
            glColor3ub(vertex.color.red, vertex.color.green, vertex.color.blue)
            glVertex3f(vertex.dx, vertex.dy, vertex.dz)
        glEnd()

    def drawPoint(self, vertex: Vertex):
        glBegin(GL_POINTS)
        glColor3ub(vertex.color.red, vertex.color.green, vertex.color.blue)
        glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

    def drawLine(self, line : Line):
        glBegin(GL_LINES)
        for vertex in line.verticies:
            glColor3ub(vertex.color.red, vertex.color.green, vertex.color.blue)
            glVertex3f(vertex.dx, vertex.dy, vertex.dz)
        glEnd()

    def render(self, time):
        # Wyczyszczenie buforów kolorów oraz głębi
        glClear(GL_COLOR_BUFFER_BIT)
        glClear(GL_DEPTH_BUFFER_BIT)

        # Renderowanie zleconych primitywów
        for shape in self.shapes_to_render:
            if isinstance(shape, Triangle):
                self.drawTriangle(shape)
            elif isinstance(shape, Vertex):
                self.drawPoint(shape)
            elif isinstance(shape, Line):
                self.drawLine(shape)
        self.shapes_to_render.clear()

        # Wyświetlenie ramki
        glFlush()
        pygame.display.flip()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500

raindrops = []
rain_direction = [0, -5]

background_color = [0.0, 0.0, 0.0]

class Raindrop:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, W_Width)
        self.y = W_Height
        self.speed = random.uniform(1.0, 3.0)

    def fall(self):
        self.x += rain_direction[0]
        self.y += rain_direction[1] * self.speed
        if self.y < 0:
            self.reset()

def init_rain(num_drops):
    global raindrops
    raindrops = [Raindrop() for i in range(num_drops)]

def draw_house():
    glColor3f(0.1, 0.5, 0.4)
    glBegin(GL_QUADS)
    glVertex2f(150, 100)
    glVertex2f(350, 100)
    glVertex2f(350, 300)
    glVertex2f(150, 300)
    glEnd()

    glColor3f(0.9, 0.1, 0.6)
    glBegin(GL_TRIANGLES)
    glVertex2f(130, 300)
    glVertex2f(370, 300)
    glVertex2f(250, 400)
    glEnd()

    glColor3f(0.0, 0.1, 0.2)
    glBegin(GL_QUADS)
    glVertex2f(200, 100)
    glVertex2f(250, 100)
    glVertex2f(250, 200)
    glVertex2f(200, 200)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(275, 225)
    glVertex2f(325, 225)
    glVertex2f(325, 275)
    glVertex2f(275, 275)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(300, 225)
    glVertex2f(300, 275)
    glVertex2f(275, 250)
    glVertex2f(325, 250)
    glEnd()

def draw_rain():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for drop in raindrops:
        glVertex2f(drop.x, drop.y)
        glVertex2f(drop.x + rain_direction[0], drop.y + rain_direction[1] * drop.speed)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_house()
    draw_rain()

    glutSwapBuffers()

def animate():
    for drop in raindrops:
        drop.fall()
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global background_color
    if key == b'd':
        background_color = [min(c + 0.05, 1.0) for c in background_color]
    elif key == b'a':
        background_color = [max(c - 0.05, 0.0) for c in background_color]
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction[0] -= 1
    elif key == GLUT_KEY_RIGHT:
        rain_direction[0] += 1
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, W_Width, 0.0, W_Height)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL House in Rainfall")

init()
init_rain(100)

glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()

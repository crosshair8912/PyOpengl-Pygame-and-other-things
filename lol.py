import pygame
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
import sys

def draw():
	GL.glClear(GL.GL_COLOR_BUFFER_BIT)
	#GL.OpenGL.GLUT.glutWireTeapot(0.5)
	GLUT.glutSolidCube(1)
	GL.glFlush() 
	
GLUT.glutInit(sys.argv)
GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
GLUT.glutInitWindowSize(100, 100)
GLUT.glutInitWindowPosition(584, 100)
GLUT.glutCreateWindow("My First OGL Program")
GLUT.glutDisplayFunc(draw)
GLUT.glutMainLoop()
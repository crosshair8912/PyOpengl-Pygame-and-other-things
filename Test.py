import pygame,sys
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
import obj_parser

tmp = obj_parser.parse("crate.obj","v")
tmp_1 = obj_parser.parse("untitled.obj","v")
lol = 0

vertex_x_array = []
vertex_y_array = []
vertex_z_array = []
cnt = 0
for i in tmp:
	cnt += 1
	for j in i:
		if cnt == 1:
			vertex_x_array.append(j)
		elif cnt == 2:
			vertex_y_array.append(j)
		elif cnt == 3:
			vertex_z_array.append(j)

def init():
	GL.glClearColor(0.25,0.25,0.25,1)
	GLU.gluOrtho2D(-5.0,5.0,-5.0,5.0)
	
	
def plotpoints():
	GL.glClear(GL.GL_COLOR_BUFFER_BIT)
	GL.glColor3f(1.0, 1.0, 1.0)
	
	GL.glBegin(GL.GL_LINE_LOOP)
	for i,j,k in zip(vertex_x_array,vertex_y_array,vertex_z_array):
		GL.glVertex3f(i,j,k)
	GL.glEnd()
	GL.glBegin(GL.GL_LINE_LOOP)
	for i,j,k in zip(vertex_y_array,vertex_x_array,vertex_z_array):
		GL.glVertex3f(i,j,k)
	GL.glEnd()
	GLU.gluLookAt(0.0,0.0,0.0,vertex_x_array[0]+lol,vertex_y_array[0]+lol,vertex_z_array[0]+lol,1,1,1)
	GL.glFlush() 
def keyPressed(a,b,c):
	global lol
	if a == '\xf4':
		lol +=1
		GLUT.glutPostRedisplay()
		lol = 0
	if a == '\xe2':
		lol -=1
		GLUT.glutPostRedisplay()
		lol = 0
	print(lol)
def main():
	
	GLUT.glutInit(sys.argv)
	GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE|GLUT.GLUT_RGB)
	GLUT.glutInitWindowSize(500,500)
	GLUT.glutInitWindowPosition(50,50)
	GLUT.glutCreateWindow("Plot points")
	
	init()
	GLUT.glutKeyboardFunc(keyPressed)
	GLUT.glutDisplayFunc(plotpoints)
	GLUT.glutMainLoop()
main()
import pygame,sys
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
import obj_parser
def init():
	GL.glClearColor(0.25,0.25,0.25,1)
	#GL.glClearColor(0.7, 0.8, 0.7, 1.0)
	GLU.gluOrtho2D(-10.0,10.0,-10.0,10.0)
	
# def plotpoints():
	# GL.glClear(GL.GL_COLOR_BUFFER_BIT)
	# GL.glColor3f(1.0,1.0,1.0)
	# #GL.glLineWidth(3.0)
	# #GL.glPointSize(1.0)
	# GL.glBegin(GL.GL_LINE_LOOP)
	# GL.glVertex3f(0.0,1.0,0.0)
	# GL.glVertex3f(1.0,0.0,0.0)
	# GL.glVertex3f(-1.0,0.0,0.0)
	# GL.glVertex3f(0.0,-1.0,0.0)
	# GL.glEnd()
	# GL.glFlush()
def plotpoints():
	GL.glClear(GL.GL_COLOR_BUFFER_BIT)
	GL.glColor3f(0.0, 0.0, 0.0)
	GL.glBegin(GL.GL_LINE_LOOP)
	tmp = obj_parser.parse("crate.obj","v")
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
	for i,j,k in zip(vertex_x_array,vertex_y_array,vertex_z_array):
		GL.glVertex3f(i,j,k)
	GL.glEnd()
	GL.glFlush() 
def main():
	
	GLUT.glutInit(sys.argv)
	GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE|GLUT.GLUT_RGB)
	GLUT.glutInitWindowSize(500,500)
	GLUT.glutInitWindowPosition(50,50)
	GLUT.glutCreateWindow("Plot points")
	GLUT.glutDisplayFunc(plotpoints)
	
	init()
	GLUT.glutMainLoop()
main(main())
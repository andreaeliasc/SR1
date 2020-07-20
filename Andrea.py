#Andrea Estefania Elias Cobar
#17048
#Graficas por computadora


import struct


def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

def color(r,g,b):
	return bytes([b,g,r])

class Bitmap(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.clearColor = color(0,0,0)
        self.vertexColor = color(255,255,0)
        self.glClear()

    def glInit(self):
            pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    def glViewPort(self,x,y,width,height):
        self.x = x
        self.y = y
        self.vpx = width
        self.vpy = height

    def glClear(self):
        self.framebuffer = [
            [
                self.clearColor	for x in range(self.width)
                ]
            for y in range(self.height)
            ]

    def glClearColor(self,r,g,b):
        try:
                self.rc = round(255*r)
                self.gc = round(255*g)
                self.bc = round(255*b)
                self.clearColor = color(self.rc,self.gc,self.bc)
        except ValueError:
                print("No puede ingresar un numero mayor a 1 ni menor que 0 en el color")

    def glVertex(self,x,y):
        if x <= 1 and x>= -1 and y >= -1 and y <= 1:
                if x > 0:
                        self.vx = self.x + round(round(self.vpx/2)*x) - 1
                if y > 0:
                        self.vy = self.y + round(round(self.vpy/2)*y) - 1
                if x <= 0:
                        self.vx = self.x + round(round(self.vpx/2)*x)
                if y <= 0:
                        self.vy = self.y + round(round(self.vpy/2)*y)
                
                self.point(self.vx,self.vy, self.vertexColor)
        else:
                pass
        
    def glColor(self,r,g,b):
        try:
                self.rv = round(255*r)
                self.gv = round(255*g)
                self.bv = round(255*b)
                self.vertexColor = color(self.rv,self.gv,self.bv)
        except ValueError:
                print("No puede ingresar un numero mayor a 1 ni menor que 0 en el color")

    def point(self,x,y,color):
        try:
                self.framebuffer[y][x] = color
        except IndexError:
                print("No fue imposible imprimir el punto dado que esta fuera de los limites de la imagen")

    def glFinish(self, filename):
        f = open(filename, 'wb')
        #file header 14
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(54 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(54))

        #image headear 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

objeto = Bitmap(600,400)

def glInit():
        objeto = Bitmap(600,400)
        
def glCreateWindow(width,height):
        objeto.glCreateWindow(width,height)

def glViewPort(x,y,width,height):
        objeto.glViewPort(x,y,width,height)
        
def glClear():
        objeto.glClear()

def glClearColor(r,g,b):
        objeto.glClearColor(r,g,b)

def glVertex(x,y):
        objeto.glVertex(x,y)

def glColor(r,g,b):
        objeto.glColor(r,g,b)

def glFinish(filename):
        objeto.glFinish(filename)

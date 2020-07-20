#Andrea Estefania Elias Cobar
#17048
#Graficas por computadora


import struct


def char(c):
    return struct.pack('=c', c.encode('ascii'))


def word(c):
    return struct.pack('=h', c)


def dword(c):
    return struct.pack('=l', c)


def color(r, g, b):
    return bytes([b, g, r])


class Bitmap(object):
    def __init__(self):
        self.framebuffer = []

   

    def glInit(self):
        pass
    
    def point(self, x, y):
        self.framebuffer[y][x] = self.color

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    def glViewport(self, x, y, width, height):
        self.xViewPort = x
        self.yViewPort = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def glClear(self):
        self.framebuffer = [
            [
                color(0, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glClearColor(self, r=1, g=1, b=1):
        r = round(r * 255)
        g = round(g * 255)
        b = round(b * 255)

        self.framebuffer = [
            [color(r, g, b) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glColor(self, r=1, g=0, b=1):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        self.color = color(r, g, b)

    def glVertex(self, x, y):
        X = round((x+1)*(self.viewPortWidth/2)+self.xViewPort)
        Y = round((y+1)*(self.viewPortHeight/2)+self.yViewPort)
        self.point(X, Y)

    def glFinish(self, filename='Andrea.bmp'):
        f = open(filename, 'wb')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        #header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel
        for x in range(self.width):
            for y in range(self.height):
                f.write(self.framebuffer[x][y])

        f.close()


bitmap = Bitmap()

bitmap.glCreateWindow(400, 400)
bitmap.glClearColor(0.5, 0, 0.5)
bitmap.glViewport(200,200 , 200, 200)
bitmap.glColor(1, 1, 0)
bitmap.glVertex(-1, -1)
bitmap.glFinish()

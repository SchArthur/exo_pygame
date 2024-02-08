import pygame

class newImage:
    def __init__(self, file) -> None:
        content = open(file, 'r')
        setting = nextLine(content)
        if setting == 'P1':
            self.read_p1(content)
        content.close()

    def read_p1(self, content):
        size_tuple = nextLine(content)
        size_tuple = size_tuple.split(' ')
        self.img_x = int(size_tuple[0])
        self.img_y = int(size_tuple[1])
        self.img =[]
        for y in range(0, self.img_y):
            self.img.append(nextLine(content))
    
    def read_p2(self, content):
        return
    
    def drawImg(self, screen):
        for y in range(len(self.img)):
            ligne = self.img[y]
            for x in range(len(ligne)):
                pixel = ligne[x]
                if pixel == '1' :
                    screen.set_at((x,y),'black')

def nextLine(file):
    line = file.readline()
    while line[0] == '#':
        line = file.readline()
    return line.strip()
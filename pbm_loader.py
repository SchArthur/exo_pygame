import pygame
import compression

class newImage:
    def __init__(self, file) -> None:
        content = open(file, 'r')
        self.format = file.split('.')[1]
        setting = nextLine(content)
        if setting == 'P1':
            self.read_P1(content)
        elif setting == 'MNS':
            self.read_mns(content)
        elif setting == 'MNSL':
            self.read_mnsl(content)
        content.close()

    def read_mns(self, content):
        size_tuple = nextLine(content)
        size_tuple = size_tuple.split(' ')
        self.img_x = int(size_tuple[0])
        self.img_y = int(size_tuple[1])
        self.img =[]
        self.img = nextLine(content)
        self.img = compression.decompressData(self.img)

    def read_mnsl(self, content):
        size_tuple = nextLine(content)
        size_tuple = size_tuple.split(' ')
        self.img_x = int(size_tuple[0])
        self.img_y = int(size_tuple[1])
        self.color_counts = int(size_tuple[2])
        self.color_dict = {}
        for i in range(self.color_counts):
            color_line = content.readline()[:-1]
            color = color_line.split(' ')
            self.color_dict[color[0]] = color[1]

        self.img =[]
        self.img = nextLine(content)
        self.img = compression.decompressData(self.img) 

    def read_P1(self, content):
        size_tuple = nextLine(content)
        size_tuple = size_tuple.split(' ')
        self.img_x = int(size_tuple[0])
        self.img_y = int(size_tuple[1])
        
        for y in range(0, self.img_y):
            self.img.append(nextLine(content))
    
    def read_p2_pbm(self, content):
        return
    
    def drawImg(self, screen):
        if self.format == 'bpm':
            for y in range(len(self.img)):
                ligne = self.img[y]
                for x in range(len(ligne)):
                    pixel = ligne[x]
                    if pixel == '1' :
                        screen.set_at((x,y),'black')
        elif self.format == 'mns':
            for i in range(len(self.img)):
                x = i % self.img_x
                y = i // self.img_x
                if self.img[i] == '1' or self.img[i] == 'B':
                    screen.set_at((x,y), 'black')
        elif self.format == 'mnsl':
            for i in range(len(self.img)):
                x = i % self.img_x
                y = i // self.img_x
                char = self.img[i]
                if char in self.color_dict:
                    couleur = self.color_dict[char]
                    screen.set_at((x,y), couleur)


def nextLine(file):
    line = file.readline()
    while line[0] == '#':
        line = file.readline()
    return line.strip()
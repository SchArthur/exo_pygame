import compression
from PIL import Image
# librairie pillow sur 

def convertFilePBMtoMNS(filepath):
    entree = filepath + ".pbm"
    tmp = entree.split('.')
    sortie = tmp[0]+'.mns'

    file_in = open(entree, 'r')
    file_out = open(sortie, 'w')

    # read meta
    codex = file_in.readline()
    file_out.write('MNS\n')

    commentaire = file_in.readline()
    file_out.write(commentaire)

    size = file_in.readline()
    file_out.write(size)

    # read data

    line_out = ""
    for line in file_in:
        line = line.strip()
        line_out = line_out + line

    line_wb = ""
    for i in range(len(line_out)):
        lettre = line_out[i]
        if lettre == '0' :
            line_wb += 'W'
        elif lettre == '1' :
            line_wb += 'B'
        else:
            break

    line_compressed = compression.compressData(line_wb)
    file_out.write(line_compressed)
    print(sortie + " created. From :" + entree)

    file_in.close()
    file_out.close()

def convertFileMNSL(filepath):
    entree = filepath + ".mns"
    sortie = filepath +'.mnsl'

    file_in = open(entree, 'r')
    file_out = open(sortie, 'w')

    # read meta
    codex = file_in.readline()
    file_out.write('MNSL\n')

    commentaire = file_in.readline()
    file_out.write(commentaire)

    size = file_in.readline()
    file_out.write(size)
    size = size.split(' ')
    colors = size[2]
    for i in range(int(colors)):
        line = file_in.readline()
        file_out.write(line)

    # read data

    line_out = ""
    for line in file_in:
        line = line.strip()
        line_out = line_out + line

    line_compressed = compression.compressData(line_out)
    file_out.write(line_compressed)
    print(sortie + " created. From :" + entree)

    file_in.close()
    file_out.close()

def pngToMNSL(filepath):
    entree = filepath + ".png"
    sortie = filepath +'.mnsl'

    file_out = open(sortie, 'w')

    file_img = Image.open(entree, 'r')
    pixels = file_img.convert('RGBA')
    data = file_img.getdata()
    list_pixels = []
    for pixels in data:
        list_pixels.append(getRGBHEX(pixels))
    color_dict = create_colors_dict(list_pixels)
    print(color_dict)
    print(file_img.size)  # Get the width and hight of the image for iterating over

    file_out.write('MNSL\n')
    file_out.write('# fichier cree avec PNGtoCompressedMNSL.py de SchArthur \n')
    
    color_count = len(color_dict)
    size_string = str(file_img.size[0]) + ' ' + str(file_img.size[1]) + ' ' + str(color_count) + '\n'
    file_out.write(size_string)
    for key in color_dict:
        file_out.write(color_dict[key] + ' ' + key + '\n')

    img_str = ''
    for pixel in list_pixels:
        img_str += color_dict[pixel]

    compressed_line = compression.compressData(img_str)
    file_out.write(compressed_line)

    file_img.close()
    file_out.close()

def create_colors_dict(pixelRGBHEXlist) -> dict:
    special_char = ('&','{','#','(','[','-','|','`','_','@',')',']','=','+','}','$','*')
    color_dict = {}
    for pixelRGB in pixelRGBHEXlist:
        if pixelRGB not in color_dict:
            for i in range(0, len(special_char)):
                if special_char[i] not in color_dict.values():
                    color_dict[pixelRGB] = special_char[i]
                    break

    return color_dict

def getRGBHEX(pixelRGB) -> str:
    red = hex(pixelRGB[0])
    red = red[2:]
    if len(red) == 1 :
        red = '0' + red
    green = hex(pixelRGB[1])
    green = green[2:]
    if len(green) == 1 :
        green = '0' + green
    blue = hex(pixelRGB[2])
    blue = blue[2:]
    if len(blue) == 1 :
        blue = '0' + blue
    HEX = '#' + red + green + blue
    return HEX

# Converti le fichier 'test.png' en un fichier compressé test.mnsl
# ------------------------ATTENTION------------------------
# test.png ne doit pas contenir plus de 16 couleurs differentes
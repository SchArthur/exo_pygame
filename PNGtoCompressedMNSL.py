from PIL import Image

# PNGtoCompressedMNSL by SchArthur

def compressData(data : str) :
    """compression RLE de data"""
    assert(data.isdigit()==False)
    C = ""
    couleur = data[0]
    nbr = 1
    for i in range(1,len(data)):
        # on a toujours la même couleur qui se répète aussi, on la compte.
        if data[i]==couleur:
            nbr =nbr +1
        else:
            # on change de couleur. On stocke alors la couleur puis la lettre.
            # optimisation au lieu d'écrire 1A on écrit simplement A
            if nbr==1:
                C=C+couleur
                couleur = data[i]
                nbr = 1
            else:
                C=C+str(nbr)+couleur
                couleur = data[i]
                nbr = 1
    #gestion du dernier caractère compressé de la chaine à la fin du document 
    if nbr==1:
        C=C+couleur
    else:
        C=C+str(nbr)+couleur
    return C

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

    compressed_line = compressData(img_str)
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
pngToMNSL('test')
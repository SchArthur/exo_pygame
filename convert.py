import compression

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

convertFilePBMtoMNS('chat')
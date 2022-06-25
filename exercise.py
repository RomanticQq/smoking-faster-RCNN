import os

file_dir = './dataset/VOC2007/Annotations'


def getFlist(path):
    dst_dir = './dataset/VOC2007/ImageSets/Main/trainval.txt'
    i = 0
    f = open(dst_dir, 'w')
    for root, dirs, files in os.walk(file_dir):
        f.write('\n'.join(files).replace('.xml',''))
        i = i + 1
    f.close()
    print(i)


getFlist(file_dir)

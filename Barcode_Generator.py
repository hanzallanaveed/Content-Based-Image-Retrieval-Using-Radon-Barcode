import codecs
import json
import os

import np as np
from PIL import Image


def diagonal_projection(x, y, ydir):
    proj_sum = 0

    if x == 27:
        if ydir == -1:
            length = y + 1
        else:
            length = 28 - y
    else:
        length = x + 1

    for i in range(length):
        proj_sum += image_arr[x][y]

        x -= 1
        y += ydir

    return proj_sum


def projection():
    p1 = np.zeros(28, np.int16)
    p2 = np.zeros(28, np.int16)
    p3 = np.zeros(53, np.int16)
    p4 = np.zeros(53, np.int16)
    barcode = np.zeros(162, np.int0)
    th_p12 = 0

    for i in range(28):
        for j in range(28):
            p1[i] += image_arr[i][j]
            p2[i] += image_arr[j][i]

        th_p12 += p1[i]

    th_p12 = th_p12 / 28

    for i in range(28):
        if p1[i] > th_p12 * 1.26:
            barcode[i] = 1
        if p2[i] > th_p12 * 1.26:
            barcode[i + 28] = 1

    for i in range(28):
        p3[0] += image_arr[27 - i][27 - i]
        p4[0] += image_arr[27 - i][i]

    for i in range(26):
        p3[i + 1] = diagonal_projection(26 - i, 27, -1)
        p3[i + 27] = diagonal_projection(27, 26 - i, -1)
        p4[i + 1] = diagonal_projection(26 - i, 0, 1)
        p4[i + 27] = diagonal_projection(27, i + 1, 1)

    th_p34 = (th_p12 * 28) / 53

    for i in range(53):
        if p3[i] > th_p34 * 2.54:
            barcode[i + 56] = 1
        if p4[i] > th_p34 * 2.54:
            barcode[i + 108] = 1

    # For 1 image or text of all
    file.write(np.array2string(barcode) + "\n")

    # For all images
    # return barcode


# For 1 image
file = open("barcodes.txt", "w")

image_arr = np.asarray(Image.open(os.path.join(os.getcwd(), 'MNIST_DS/0', 'img_10007.jpg')))
projection()

file.close()

# For all images
# barcode_array = np.empty((10, 10, 162), np.int0)
#
# for i in range(10):
#     folder = os.listdir(os.path.join(os.getcwd(), 'MNIST_DS/' + str(i)))
#
#     while folder:
#         image_arr = np.asarray(Image.open(os.path.join(os.getcwd(), 'MNIST_DS/' + str(i), folder.pop())))
#         barcode_array[i][len(folder)] = projection()
#
# (json.dump(barcode_array.tolist(), codecs.open("barcodes.json", 'w', encoding='utf-8')))

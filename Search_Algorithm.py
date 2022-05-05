import codecs
import json
import os

import numpy as np


def search(num, version):
    target = array[num][version]
    similar = 0
    lowest_hd = 162

    for i in range(10):
        for j in range(10):
            if i == num and j == version:
                continue

            test = array[i][j]
            hamming_distance = 0

            for k in range(162):
                if target[k] != test[k]:
                    hamming_distance += 1

            if lowest_hd > hamming_distance:
                lowest_hd = hamming_distance
                similar = i
                savej = j

    print("Target Image: " + str(os.listdir(os.path.join(os.getcwd(), 'MNIST_DS/' + str(num)))[version]))
    print("Result Image: " + str(os.listdir(os.path.join(os.getcwd(), 'MNIST_DS/' + str(similar)))[savej]))

    if similar == num:
        return 1

    return 0


hit = 0

file = open("C:/Users/merri/PycharmProjects/Barcode_Generator/barcodes.json", "r")
array = np.array(json.loads(codecs.open("C:/Users/merri/PycharmProjects/Barcode_Generator/barcodes.json", "r",
                                        encoding='utf-8').read()), np.int0)
# 1 search
hit += search(0, 0)

print("Hit ratio: " + str(hit))

# Search all possible queries
# for i in range(10):
#     for j in range(10):
#         hit += search(i, j)
#
# print("Hit ratio: " + str(hit/100))

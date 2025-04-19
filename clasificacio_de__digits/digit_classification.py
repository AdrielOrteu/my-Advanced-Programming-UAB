from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import os

from numpy.ma.core import shape

def image_vector(image):
    v_image = np.zeros(50)
    avg = np.mean(image)
    
    mask = image < avg
    image[mask] = 0
    # image[~mask] = 255
    for index, value in np.ndenumerate(image):
        if value == 0:
            v_image[index[0]] += 1
            v_image[30 + index[1]] += 1
    return v_image

def training(directory):
    batch = []
    for filename in os.listdir(directory):
        image = plt.imread(f"{directory}/{filename}").copy()
        #print(image.shape)
        vector = image_vector(image)
        batch.append((vector, filename[15]))
    return batch

def euclid_distance(v1, v2):
    u = v1 - v2
    u = u**2
    r = np.sqrt(np.sum(u))
    return r

def classificacio_digits(train, test, k): # name_train_file, name_test_file, parameter(int)
    returned_lst = []
    vector_subset = training(train)
    for filename in os.listdir(test):
        image = plt.imread(f"{test}/{filename}").copy()
        test_vector = image_vector(image)
        distances = [ (euclid_distance(test_vector, vector[0]), vector) for vector in vector_subset]
        distances.sort(key=lambda x: x[0])
        best_vectors = [ distances[i][1] for i in range(k)]
        activation = Counter([v[1] for v in best_vectors]).most_common(1)[0][0]
        returned_lst.append( (filename, activation, test_vector) )
    
    return returned_lst

import numpy as np
import os

def training(directory):
    for filename in os.listdir(directory):
        print(filename)

def classificacio_digits(train, test, k): # name_train_file, name_test_file, parameter(int)
    training(train)
    

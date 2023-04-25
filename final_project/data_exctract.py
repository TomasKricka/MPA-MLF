#import glob
import pandas as pd
import numpy as np
#import os


print("Hello")

test_data = []
train_data = []

for i in range(3549):
    test_cesty = "D:/Pragraming/Dataset/Test/CSV/img_%d.csv" %(i)
    test_data.append(test_cesty)

for x in range(8279):
    train_cesty = "D:/Pragraming/Dataset/Train/CSV/img_%d.csv" %(x)
    train_data.append(train_cesty)


x_test_mat = []
x_train_mat = []

for file_test in test_data:
    x_test_data = pd.read_csv(file_test, index_col=None)
    x_test_mat.append(x_test_data)


print("tady hotovo")


print("tady hotovo")

for file_train in train_data:
    x_train_data = pd.read_csv(file_train, index_col=None)
    x_train_mat.append(x_train_data)

print("done x_train")



np.save("D:/Pragraming/Dataset/x_test_all", x_test_mat)
np.save("D:/Pragraming/Dataset/x_train_all", x_train_mat)

print("hotovo !!")
    
import os
from PIL import Image
from numpy import *


def load_data(path1, path2, path3, path4, path5, path6):
    filelist1 = [os.path.join(path1, f) for f in os.listdir(path1)]
    filelist2 = [os.path.join(path2, f) for f in os.listdir(path2)]
    filelist3 = [os.path.join(path3, f) for f in os.listdir(path3)]
    filelist4 = [os.path.join(path4, f) for f in os.listdir(path4)]
    filelist5 = [os.path.join(path5, f) for f in os.listdir(path5)]
    filelist6 = [os.path.join(path6, f) for f in os.listdir(path6)]
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    n1 = len(filelist1)
    n2 = len(filelist2)
    n3 = len(filelist3)
    n4 = len(filelist4)
    n5 = len(filelist5)
    n6 = len(filelist6)
    for img in filelist1:
        im = array(Image.open(img))
        x_train.append(im)
    for img in filelist2:
        im = array(Image.open(img))
        x_train.append(im)
    for img in filelist3:
        im = array(Image.open(img))
        x_train.append(im)
    for img in filelist4:
        im = array(Image.open(img))
        x_test.append(im)
    for img in filelist5:
        im = array(Image.open(img))
        x_test.append(im)
    for img in filelist6:
        im = array(Image.open(img))
        x_test.append(im)

    x_train = array(x_train)
    y_train = zeros((n1 + n2 + n3), dtype=int)
    x_test = array(x_test)
    y_test = zeros((n4 + n5 + n6), dtype=int)
    for i in range(n1):
        y_train[i] = 0
    for i in range(n2):
        y_train[n1 + i] = 1
    for i in range(n3):
        y_train[n1 + n2 + i] = 2
    for i in range(n4):
        y_test[i] = 0
    for i in range(n5):
        y_test[n4 + i] = 1
    for i in range(n6):
        y_test[n4 + n5 + i] = 2
    return x_train,y_train,x_test,y_test


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = load_data("data/train/type0", "data/train/type1", "data/train/type2","data/test/type0", "data/test/type1", "data/test/type2")
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')
    print(y_test)

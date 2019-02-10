#!coding=utf-8
'''
此代码来自于Andrew Ng deep learning系列第一课最后一个大作业
2018-09-22 Jemma @ concordia Univ
'''

import time
import numpy as np
import h5py
import matplotlib
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from PIL.Image import core as _imaging
from scipy import ndimage
#函数库
from dnn_app_utils_v3 import *
from data_preprocess import *


#np.random.seed(1) #MAKE SURE the result be the same every time you run


'''
dnn_app_utils provides the functions implemented in the 
"Building your Deep Neural Network: Step by Step" assignment to this notebook.
np.random.seed(1) is used to keep all the random function calls consistent. 
'''


#实验中使用的data is Nima provied 2-class Lung cancer data
#第一步 load data
train_x_orig, train_y, test_x_orig, test_y,classes= load_data('/')

train_x_orig_G, train_y_G,test_x_orig, test_y,classes= load_data('/Gaussian_pic/')
# #2 use only G_data
train_x_orig_45, train_y_45,test_x_orig, test_y,classes= load_data('/Rotate_45/')
train_x_orig_90, train_y_90,test_x_orig, test_y,classes= load_data('/Rotate_90/')
train_x_orig_135, train_y_135,test_x_orig, test_y,classes= load_data('/Rotate_135/')
train_x_orig_180, train_y_180,test_x_orig, test_y,classes= load_data('/Rotate_180/')
train_x_orig_225, train_y_225,test_x_orig, test_y,classes= load_data('/Rotate_225/')
train_x_orig_270, train_y_270,test_x_orig, test_y,classes= load_data('/Rotate_270/')
train_x_orig_315, train_y_315,test_x_orig, test_y,classes= load_data('/Rotate_315/')

train_x_orig =train_x_orig+train_x_orig_G+train_x_orig_45+train_x_orig_90+\
              train_x_orig_135+train_x_orig_180+train_x_orig_225+train_x_orig_270+train_x_orig_315
train_y = np.append(train_y,train_y_G)
train_y = np.append(train_y,train_y_45)
train_y = np.append(train_y,train_y_90)
train_y = np.append(train_y,train_y_135)
train_y = np.append(train_y,train_y_180)
train_y = np.append(train_y,train_y_225)
train_y = np.append(train_y,train_y_270)
train_y = np.append(train_y,train_y_315)

# train_y = np.append(train_y,train_y_45)
# train_y = np.append(train_y,train_y_90)
# train_y = np.append(train_y,train_y_135)
N=9 #how many zu data used

#Explore your dataset
m_train = np.shape(train_x_orig)[0]
# print(np.shape(train_x_orig))
num_px = np.shape(train_x_orig)[1]
m_test = np.shape(test_x_orig)[0]


print ("Number of training examples: " + str(m_train))
print ("Number of testing examples: " + str(m_test))
print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
print ("train_x_orig shape: " + str(np.shape(train_x_orig)))
print ("train_y shape: " + str(np.shape(train_y)))
print ("test_x_orig shape: " + str(len(test_x_orig)))
print ("test_y shape: " + str(np.shape(test_y)))

#2017-11-06 try to fix the data-flatten work
#in following part

train_x_flatten=[]
for pic in train_x_orig:
    temporary = pic.reshape(pic.shape[0]*pic.shape[1]*pic.shape[2],1)/255
    train_x_flatten.append(temporary)

xx=np.array(train_x_flatten )
train_x =xx.reshape(12288,85*N)

test_x_flatten=[]
for pic in test_x_orig:
    temporary = pic.reshape(pic.shape[0]*pic.shape[1]*pic.shape[2],1)/255
    test_x_flatten.append(temporary)

xx=np.array(test_x_flatten )
test_x =xx.reshape(12288,80)

#L-layer model defination
### CONSTANTS ###
layers_dims = [12288,20,7,5,1] #  4-layer model

#训练的最终目的就是获得parameters
parameters = L_layer_model(train_x, train_y, layers_dims, num_iterations = 1800, print_cost = True)

pred_test = predict(test_x, test_y, parameters)

#print_mislabeled_images(classes,test_x, test_y, pred_test)


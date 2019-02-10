#coding=utf-8
#!/usr/bin/python
from __future__ import print_function
import pandas as pd
import numpy as np
import os
from PIL import Image
import h5py

'''
Read csv files and get the label of each picture.
Store the picture data with related label.

Jemma
2018-10-31
@Concordia,Montreal,QC,CA
'''

pic_dir = './lung_data/'
file_name = './lung_data/Grade.csv'

def check_file(data_dir):
    if os.path.exists(data_dir):
            return True
    else:
        print("No such file,please check the dir!")
        return False


def load_data(subdir):
    """Loads data from CSV file.
    Retrieves a matrix of all rows and columns from Lung  dataset.
    Args:
        file_name
    Returns:
        train_img,train_label,test_img,test_label
    """
    while(check_file(file_name)):
        # FOR training data saving
        data = pd.read_csv(file_name, na_values='_')
        # split test and train data.
        # print(data)
        test_csv = data.values[0:80][:]
        train_csv = data.values[80:165][:]

        train_img = []
        test_img = []
        train_label = []
        test_label = []
        #for path, subdirs, file in os.walk('./lung_data/train/'):
        for file in os.listdir('./lung_data' + '/train'+subdir):
            if (file.startswith('train')):
                img = Image.open('./lung_data' + '/train/'+subdir + file)
                img=img.resize((64, 64),Image.BILINEAR)
                #img.show()
                img=np.array(img)
                train_img.append(img)
                for i in range(85):
                    if file.split('.')[0] == train_csv[i][0]:
                        if ( 'malignant' in train_csv[i][2] ):
                            train_label.append(1)
                        elif  ('benign' in train_csv[i][2]) :
                            train_label.append(0)
                        else:
                            train_label.append(2)
        for file in os.listdir('./lung_data' + '/test/'):
            if (file.startswith('test')):
                img = Image.open('./lung_data' + '/test/' + file)
                img = img.resize((64, 64), Image.BILINEAR)
                img = np.array(img)
                test_img.append(img)
                for i in range(80):
                    if file.split('.')[0] == test_csv[i][0]:
                        #test_label.append(test_csv[i][2])
                        if ( 'malignant' in test_csv[i][2] ):
                            test_label.append(1)
                        elif  ('benign' in test_csv[i][2]) :
                            test_label.append(0)
        train_label=np.array(train_label)
        test_label = np.array(test_label)
        classes = np.array([('malignant'),('benign')])  # the list of classes
        return train_img,np.array(train_label),np.array(test_img), np.array(test_label),classes



def save_data_into_lst(subdir):
    """Loads data from CSV file.
    Retrieves the neme and label of each picture
    Args:
        file_name
    Returns:
        none
    Get:
        a new filr named images.lst contains
        train_0.bmp 1
        train_1.bmp 2
    """
    while(check_file(file_name)):
        # FOR training data saving
        data = pd.read_csv(file_name, na_values='_')
        # split test and train data.
        # print(data)
        test_csv = data.values[0:80][:]
        train_csv = data.values[80:165][:]

        train_img = []
        test_img = []

        #for path, subdirs, file in os.walk('./lung_data/train/'):
        for file in os.listdir('./lung_data' + '/train'+subdir):
            if (file.startswith('train')):
                for i in range(85):
                    if file.split('.')[0] == train_csv[i][0]:
                        if ( 'malignant' in train_csv[i][2] ):
                            train_label = 1
                        elif  ('benign' in train_csv[i][2]) :
                            train_label = 0
                        else:
                            train_label = 2
                # files = os.listdir('images.lst')
                files = open("images.lst", "a")
                file_name_save = str(file)+' '+str(train_label)+"\n"
                files.write(str(file_name_save))

        for file in os.listdir('./lung_data' + '/test/'):
            if (file.startswith('test')):
                for i in range(80):
                    if file.split('.')[0] == test_csv[i][0]:
                        if ( 'malignant' in train_csv[i][2] ):
                            test_label = 1
                        elif  ('benign' in train_csv[i][2]) :
                            test_label = 0
                        else:
                            test_label = 2
                files = open("img_test.lst", "a")
                file_name_save = str(file) + ' ' + str(test_label) + "\n"
                files.write(str(file_name_save))
        return 0

if __name__ == "__main__":
    save_data_into_lst('/')


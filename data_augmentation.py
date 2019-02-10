'''
Augment pictures

Jemma
2018-11-10 Sat.
@Concordia,Montreal,QC,CA
'''

import cv2
import os
import numpy as np

#Rotate without cropping ! 11/21/2018
from PIL import Image
from math import sqrt

def rotate_im(image, angle):
    image_height = image.shape[0]
    image_width = image.shape[1]
    diagonal_square = (image_width*image_width) + (
        image_height* image_height
    )
    #
    diagonal = round(sqrt(diagonal_square))
    padding_top = round((diagonal-image_height) / 2)
    padding_bottom = round((diagonal-image_height) / 2)
    padding_right = round((diagonal-image_width) / 2)
    padding_left = round((diagonal-image_width) / 2)
    padded_image = cv2.copyMakeBorder(image,
                                      top=padding_top,
                                      bottom=padding_bottom,
                                      left=padding_left,
                                      right=padding_right,
                                      borderType=cv2.BORDER_CONSTANT,
                                      value=0
            )
    padded_height = padded_image.shape[0]
    padded_width = padded_image.shape[1]
    transform_matrix = cv2.getRotationMatrix2D(
                (padded_height/2,
                 padded_width/2), # center
                angle, # angle
      1.0) # scale
    rotated_image = cv2.warpAffine(padded_image,
                                   transform_matrix,
                                   (diagonal, diagonal),
                                   flags=cv2.INTER_LANCZOS4)
    return rotated_image


for path, subdirs, files in os.walk('./lung_data/train/'):
    for name in files:
        file_path = os.path.join(path, name)
        img = cv2.imread(file_path)
        # #Gaussian_filter
        # dst = cv2.GaussianBlur(img, (5, 5), 0)
        # save_path_Gaussian = os.path.join(path,'Gaussian_pic')
        # save_path_Gaussian =  os.path.join(save_path_Gaussian,name)
        # cv2.imwrite(save_path_Gaussian, dst)

        #Rotate without cropping New version!
        N =315
        rows, cols = img.shape[0], img.shape[1]
        im1 = rotate_im(img, N)
        img = Image.fromarray(im1, 'RGB')
        #save_path_R = os.path.join(path, 'Rotate_45')
        name_save = './lung_data/Rotate_'+str(N)+'/'+name
        #save_path_R = os.path.join(save_path_R, name)
        #cv2.imwrite(save_path_R, img)
        img.save(name_save,'bmp')

        # # Rotate without cropping New version!
        # im2 = rotate_im(img, 90)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_90')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')
        #
        #
        # im3 = rotate_im(img, 135)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_135')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')
        #
        # im2 = rotate_im(img, 180)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_180')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')
        #
        # im2 = rotate_im(img, 225)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_225')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')
        #
        # im2 = rotate_im(img, 270)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_270')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')
        #
        # rows, cols = img.shape[0], img.shape[1]
        # im2 = rotate_im(img, 315)
        # img = Image.fromarray(im2, 'RGB')
        # save_path_R = os.path.join(path, 'Rotate_315')
        # name_save = save_path_R + '/' + name
        # # save_path_R = os.path.join(save_path_R, name)
        # # cv2.imwrite(save_path_R, img)
        # img.save(name_save, 'bmp')











        # #Rotate_pictures_90_45_135(with cropping Old version)
        #rows, cols = img.shape[0],img.shape[1]
        # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
        # dst = cv2.warpAffine(img, M, (cols, rows))
        # save_path_R90 = os.path.join(path,'Rotate_90')
        # save_path_R90 =  os.path.join(save_path_R90,name)
        # cv2.imwrite(save_path_R90, dst)

        # # Rotate_pictures_45
        # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
        # dst = cv2.warpAffine(img, M, (cols, rows))
        # save_path_R = os.path.join(path, 'Rotate_45')
        # save_path_R = os.path.join(save_path_R, name)
        # cv2.imwrite(save_path_R, dst)
        # Rotate_pictures_135
        # M = cv2.getRotationMatrix2D((cols / 2, rows / 2),135, 1)
        # dst = cv2.warpAffine(img, M, (cols, rows))
        # save_path_R = os.path.join(path, 'Rotate_135')
        # save_path_R = os.path.join(save_path_R, name)
        # cv2.imwrite(save_path_R, dst)
        # print(save_path)

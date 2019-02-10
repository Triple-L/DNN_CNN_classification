import cv2
import os
from PIL import Image
#Rotate without cropping ! 11/21/2018

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

        im2 = rotate_im(img, 45)
        img = Image.fromarray(im2, 'RGB')

        img.save('my.png')
        img.show()
        #im2.show()



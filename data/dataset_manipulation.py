import numpy as np
import cv2
import os
import shutil

data_dir = 'data\\train'
lr_dir = 'data\\lr_images'
downsample_scale = 3

# Cropping the image to 180 x 180
for dirpath, dirnames, filenames in os.walk(data_dir):
    for file in filenames:
        if file.endswith('.png'):
            # img = cv2.imread(os.path.join(dirpath, file))
            # if (img.shape[0] == 180) and (img.shape[1] == 180):
            #     pass
            # else:                
            #     crop_img = img[0:180, 0:180]
            #     cv2.imwrite(os.path.join(dirpath, file), crop_img)

            # # downsampling high resolution images using bicubic interpolation
            # h ,w = img.shape[:2]
            # lr_image = cv2.resize(img, (w//downsample_scale, h//downsample_scale), interpolation=cv2.INTER_CUBIC)
            # cv2.imwrite(os.path.join(lr_dir, (dirpath.split('\\')[-1]+"_"+file)), lr_image)
            shutil.move(os.path.join(dirpath, file), os.path.join('data\\hr_images', (dirpath.split('\\')[-1]+"_"+file)))

    
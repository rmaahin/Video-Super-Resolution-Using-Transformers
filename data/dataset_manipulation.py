import numpy as np
import cv2
import os
from tqdm import tqdm

data_dir = 'Video-Super-Resolution-Using-Transformers\\data\\train'
# Cropping the image to 180 x 180
for dirpath, dirnames, filenames in tqdm(os.walk(data_dir)):
    for file in filenames:
        if file.endswith('.png'):
            img = cv2.imread(os.path.join(dirpath, file))
            if (img.shape[0] == 180) and (img.shape[1] == 180):
                pass
            else:                
                # crop_img = img[0:180, 0:180]
                # cv2.imwrite(os.path.join(dirpath, file), crop_img)
                print(file)
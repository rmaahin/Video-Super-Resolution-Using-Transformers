import numpy as np
import cv2
import os
import shutil
from tqdm import tqdm

downsample_scale = 3

dataset_dir = 'data\\dataset'
for folder in tqdm(os.listdir(dataset_dir)):
    os.makedirs(os.path.join(dataset_dir, folder, 'lr_images'), exist_ok=True)
    os.makedirs(os.path.join(dataset_dir, folder, 'hr_images'), exist_ok=True)
    for file in os.listdir(os.path.join(dataset_dir, folder)):
        if file.endswith('.png'):
            img = cv2.imread(os.path.join(dataset_dir, folder, file))
            crop_img = img[0:180, 0:180]
            cv2.imwrite(os.path.join(dataset_dir, folder, 'hr_images', file), crop_img)

for folder in tqdm(os.listdir(dataset_dir)):
    for file in os.listdir(os.path.join(dataset_dir, folder, 'hr_images')):
        img = cv2.imread(os.path.join(dataset_dir, folder, 'hr_images', file))

        # downsampling high resolution images using bicubic interpolation
        h, w = img.shape[:2]
        lr_image = cv2.resize(img, (w//downsample_scale, h//downsample_scale), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(dataset_dir, folder, 'lr_images', file), lr_image)

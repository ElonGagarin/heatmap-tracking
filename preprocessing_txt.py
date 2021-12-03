import os
import re
import numpy as np

import cv2

# Получить изображение фона без людей



height = 1080
width = 1920
threshold = 5

path = 'yolov5/runs/detect/exp2/labels'




def get_mask(path, base):
    with open(path, 'r') as f:
        line = f.read()

    # print(line)  

    for i in line.split('\n'):
        try:
            x, y, h, w = i.split()[1:]

            # x_new = int(float(x)*height + float(h)*height)  # h_new
            # y_new = int(float(y)*width)

            x_new = int(float(x)*width)  # h_new
            y_new = int(float(y)*height + float(h)*height)
            

            # # # h_new = int(h*height)
            # # # w_new = int(w*width)

            base[x_new-threshold:x_new+threshold,y_new-threshold:y_new+threshold] = 255
        except:
            pass
    return base, x_new, y_new








# x = []
# y = []
mask = np.zeros((height, width), np.uint8)
for file in sorted(os.listdir(path)):
# file = 'input_1.txt'

    base = np.zeros((height, width), np.uint8)
    point, x_, y_ = get_mask(os.path.join(path, file), base)

    from scipy.ndimage.filters import gaussian_filter

    # point = gaussian_filter(point, sigma=10)
    mask = cv2.add(mask, point)


   
import matplotlib.pyplot as plt
plt.imshow(np.stack([mask,mask,mask], axis=-1))
plt.show()
# print(mask.shape)

import cv2
color_image_video = cv2.applyColorMap(mask, cv2.COLORMAP_SUMMER)
print(color_image_video)

# np.save('out_x.npy', np.array(x))
# np.save('out_y.npy', np.array(y))

cv2.imwrite('./frame_.jpg', color_image_video)

from merge import merge

merge()
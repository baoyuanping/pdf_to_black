### white_to_black.py代码
# -*- coding: utf-8 -*-

import cv2
import os
import glob
import shutil
import numpy as np

def white_to_black(src, dst):
    
    if os.path.exists(dst):  # 判断存放图片的文件夹是否存在
        shutil.rmtree(dst)   # 如果存在文件夹，就删除文件夹

    os.makedirs(dst)  # 创建文件夹

    index = 0
    for img in sorted(glob.glob("{}/*".format(src))):  # 读取图片，确保按文件名排序
        # print(img)
        cvimg = cv2.imread(img, 1)
        height, width, deep = cvimg.shape
        # 彩色图像颜色反转 NewR = 255-R
        dst1 = np.zeros((height, width, deep), np.uint8)
        for i in range(0, height):
            for j in range(0,width):
                (b, g, r) = cvimg[i, j]
                dst1[i, j] = (255-b,255-g,255-r)
        file_path = dst + '/' + 'images_{:0>4d}_black.png'.format(index)
        if os.path.exists(file_path):
            os.remove(file_path)
        cv2.imwrite(file_path, dst1)
        print(img, 'convert to', file_path)

        index += 1


if __name__ == '__main__':
    img_dir = "./lunxing_imgs"
    dst_dir = './lunxing_imgs_black'
    white_to_black(img_dir, dst_dir)



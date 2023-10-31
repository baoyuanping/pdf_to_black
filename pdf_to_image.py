### pdf_to_image.py代码
# -*- coding: utf-8 -*-

import datetime
import os
import shutil  

import fitz  # fitz就是pip install PyMuPDF


def pyMuPDF_fitz(pdfPath, imagePath):
    if os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
        shutil.rmtree(imagePath)   # 如果存在文件夹，就删除文件夹

    os.makedirs(imagePath)  # 创建文件夹

    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.page_count):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        pix.save(imagePath + '/' + 'images_{:0>4d}.png'.format(pg))  # 将图片写入指定的文件夹内
        print('split pdf to %s' % 'images_{:0>4d}.png'.format(pg))

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img 时间=', (endTime_pdf2img - startTime_pdf2img).seconds, 's')


if __name__ == "__main__":
    # 1、PDF地址
    pdfPath = 'lunxing.pdf'
    # 2、需要储存图片的目录
    imagePath = './lunxing_imgs'
    pyMuPDF_fitz(pdfPath, imagePath)


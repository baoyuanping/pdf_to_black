### image_to_pdf.py代码
# -*- coding: utf-8 -*-

import glob
import os

import fitz  # pip install PyMuPDF


def pic2pdf(img_dir, save_file_name):
    doc = fitz.open()
    for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convert_to_pdf()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)  # 将当前页插入文档
    if os.path.exists(save_file_name):
        os.remove(save_file_name)
    doc.save(save_file_name)  # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    img_dir = "./lunxing_imgs_black"
    pic2pdf(img_dir, "allimages.pdf")


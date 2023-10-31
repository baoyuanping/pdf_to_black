### pdf_to_black.py代码
# -*- coding: utf-8 -*-

import argparse
import fitz

from pdf_to_image import *
from white_to_black import *
from image_to_pdf import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='输入pdf文件背景转黑色背景')
    parser.add_argument('input_file', metavar='input',type=str, help='输入的文件名')
    parser.add_argument('output_file', metavar='output', type=str,  help='输出文件名')

    args = parser.parse_args()
    print(args.input_file, args.output_file)
    # 1、PDF地址
    pdfPath = args.input_file
    out_pdf = args.output_file
    # 2、需要储存图片的目录
    imagePath = './imgs'
    pyMuPDF_fitz(pdfPath, imagePath)
    # 3、转换图片背景
    dst_dir = './imgs_black'
    white_to_black(imagePath, dst_dir)
    # 4、生成新的pdf
    tmp_pdf = 'tmp.pdf'
    if os.path.exists(tmp_pdf):
        os.remove(tmp_pdf)
    pic2pdf(dst_dir, tmp_pdf)
    # 5、pdf生成目录
    doc = fitz.open(pdfPath)
    toc = doc.get_toc()

    out_doc = fitz.open(tmp_pdf)
    out_doc.set_toc(toc)
    out_doc.save(out_pdf)
    out_doc.close()
    
    if os.path.exists(tmp_pdf):
        os.remove(tmp_pdf)

    print('************************end**********************')

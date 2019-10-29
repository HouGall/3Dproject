#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: HG
@contact: 18165271995@163.com
@file: main.py
@time: 2019/10/18 15:17
'''
from loadobj import loadobj
from protection_matrix import protection_matrix
from protection import protection,img
from mould_rota import rotationx,rotationy,rotationz
import cv2 as cv
import os
import matplotlib.pyplot as plt
if __name__ == '__main__':
    y_angle=120
    W=480
    H=400
    n_z=5
    z_f=40
    rota=0
    filepath="H:/Process/projection/data/mould"
    filelist=os.listdir(filepath)
    for filenames in filelist:
        (filename, extension) = os.path.splitext(filenames)
        print("读入文件：%s"%filenames)
        point_data = loadobj(filepath+"/"+filenames)  # 读取obj文件
        protection_matrix = protection_matrix(y_angle, W, H, n_z, z_f)
        outpath = "H:/Process/projection/data/projectionimg"+"/"+filename
        print("%s投影结果位置:%s" % (filename, outpath))
        while 1:
            if rota > 360:
                break
            if os.path.exists(outpath):
                Vx = rotationx(point_data, rota)
                data1 = protection(protection_matrix, Vx)
                IMG1 = img(data1, H, W)
                cv.imwrite(outpath + "/" + filename + "Vx" + str(rota) + ".png", IMG1)
                Vy = rotationy(point_data, rota)
                data2 = protection(protection_matrix, Vy)
                IMG2 = img(data2, H, W)
                cv.imwrite(outpath + "/" + filename + "Vy" + str(rota) + ".png", IMG2)
                Vz = rotationz(point_data, rota)
                data3 = protection(protection_matrix, Vz)
                IMG3 = img(data3, H, W)
                cv.imwrite(outpath + "/" + filename + "Vz" + str(rota) + ".png", IMG3)
                rota = rota + 30
            else:
                os.mkdir(outpath)
                print("%s不存在，已完成创建" % (outpath))










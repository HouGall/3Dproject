#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: HG
@contact: 18165271995@163.com
@file: protection_matrix.py
@time: 2019/10/21 15:37
'''
import numpy as np

def protection_matrix(y_angle,H,W,n,f):
    aspect=W/H
    protection_matrix=np.zeros((4,4),np.float32)
    a=1/np.tan(y_angle/2)
    protection_matrix[0][0]=a/aspect
    protection_matrix[1][1]=a
    protection_matrix[2][2]=-(f+n)/(f-n)
    protection_matrix[2][3]=-2*f*n/(f-n)
    protection_matrix[3][2]=-1
    return protection_matrix
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: HG
@contact: 18165271995@163.com
@file: mould_rota.py
@time: 2019/10/21 17:25
'''
import numpy as np
def rotationx(point_data,o):
    rota_matrix=np.zeros((3,3),np.float32)
    rota_matrix[0,0]=1
    rota_matrix[1,1]=np.cos(o)
    rota_matrix[1,2]=np.sin(o)
    rota_matrix[2,1]=-np.sin(o)
    rota_matrix[2,2]=np.cos(o)
    V=np.dot(point_data,rota_matrix)
    return V

def rotationy(point_data,o):
    rota_matrix = np.zeros((3, 3), np.float32)
    rota_matrix[0, 0] = np.cos(o)
    rota_matrix[0, 2] = -np.sin(o)
    rota_matrix[1, 1] = 1
    rota_matrix[2, 0] = np.sin(o)
    rota_matrix[2, 2] = np.cos(o)
    V = np.dot(point_data, rota_matrix)
    return V

def rotationz(point_data,o):
    rota_matrix = np.zeros((3, 3), np.float32)
    rota_matrix[0, 0] = np.cos(o)
    rota_matrix[0, 1] = np.sin(o)
    rota_matrix[1, 0] = -np.sin(o)
    rota_matrix[1, 1] = np.cos(o)
    rota_matrix[2, 2] = 1
    V = np.dot(point_data, rota_matrix)
    return V



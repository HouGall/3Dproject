#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: HG
@contact: 18165271995@163.com
@file: protection.py
@time: 2019/10/18 16:56
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
# def init_img(H,W):
#     img = (np.zeros((H, W), np.float32))
#     return img
#
# def normaliz(img , H,W):
#     org_img = (np.zeros((H,W), np.float32))
#     org_img.fill(255)
#     img = org_img - (img / np.max(img)) * 255  #img = np.round(org_img - np.rint((img / np.max(img)) * 255))
#     #return mean(img.astype("int"))
#     return img

def protection(protection_matrix,data_point):
    [rows, cols] = data_point.shape
    V=np.zeros((rows,4),np.float32)
    for i in range(rows):
        V[i,0:3]=data_point[i,0:3]
        V[i,3]=1
    protection_img=np.dot(V,protection_matrix)
    data=np.zeros((rows,2))
    data[:,0]=protection_img[:,0]
    data[:,1]=protection_img[:,1]
    return data

def normaliz(img , H ,W):
    org_img = (np.zeros((H, W), np.float32))
    org_img.fill(255)
    img = org_img - (img / np.max(img)) * 255  #img = np.round(org_img - np.rint((img / np.max(img)) * 255))
    #return mean(img.astype("int"))
    return img

def coordinate_transformationx(x,W):
    xs=int(round(x / (10 * 1 / W)) + W / 2)
    return xs
def coordinate_transformationy(y,H):
    ys = int(round(y / (10 * 1 / H)) + H / 2)
    return ys

def mean(img):  #去椒盐噪声  基于卷积
    dst = cv.medianBlur(img , 5)
    return dst

def img(data,H,W):
    img = (np.zeros((W, H), np.float32))
    img.fill(255)
    # org_img = (np.zeros((H, W), np.float32))
    # org_img.fill(255)
    # img = org_img - (img / np.max(img)) * 255  # img = np.round(org_img - np.rint((img / np.max(img)) * 255))
    # img=normaliz(img,H,W)
    [rows, cols] = data.shape
    for i in range(rows):
        # img[round(data[i,0]),round(data[i,1])]=250
        img[coordinate_transformationx(data[i, 0],W),coordinate_transformationx(data[i, 1],H)] = abs(data[i,0])
    #img=mean(img)
    return img



#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: HG
@contact: 18165271995@163.com
@file: loadobj.py
@time: 2019/10/18 15:29
'''
import numpy as np
def loadobj(filename):
    point_data=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split()
            if data[0] != "v":
                break
            data = list(map(float, data[1:]))
            point_data.append(data)
    point_data = np.array(point_data)
    return point_data

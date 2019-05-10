#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 21:24
# @Author  : JYJ
# @Site    : 
# @File    : labeldemo.py
# @Software: PyCharm

import os
import linecache
import math

rootdir1 = '/home/jiayj267/IMP/Data/coordinate/'
# filename_list = []
for dirpath, dirnames, filenames in os.walk(rootdir1):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        pdbid = filename.split('.')[0]
        filelines = linecache.getlines(filepath)
        for each_item in filelines:
            for i in range(len(each_item)):
                if each_item[i] == ' 'and each_item[i-1] == ' ':
                    continue
                else:
                    print(each_item[i])
                    outfilepath = '/home/jiayj267/IMP/Data/newcoordinate/' + pdbid + '.txt'
                    writefile = open(outfilepath, 'a')
                    a = each_item[i]
                    writefile.write(a)
                    writefile.close()
                i = i + 1

# rootdir2 = 'D:/000000/IMPContact/coordinatetest/M/'
# # filename_list2 = []
# for dirpath, dirnames, filenames in os.walk(rootdir2):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         filelines = linecache.getlines(filepath)
#         coordinate = filelines
#         a = int(coordinate[0][4:8])
#         b = a
#         i = 0
#         j = 0
#         for i in range(0, len(filelines)):
#             for j in range(i + 1, len(filelines)):
#                 # if i!=j:
#                 x1 = float(coordinate[i][9:16])
#                 y1 = float(coordinate[i][17:24])
#                 z1 = float(coordinate[i][25:])
#                 x2 = float(coordinate[j][9:16])
#                 y2 = float(coordinate[j][17:24])
#                 z2 = float(coordinate[j][25:])
#                 result = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
#                 if result <= 5.5:
#                     label = 1
#                 else:
#                     label = 0
#                 outfile = filepath2 + "/" + file
#                 writefile = open(outfile, 'a')
#                 x = int(coordinate[i][4:8]) - b
#                 y = int(coordinate[j][4:8]) - b
#                 line = str(x) + '\t' + str(y) + '\t' + str(result) + '\t' + str(label) + '\n'
#                 writefile.write(line)
#                 writefile.close()
#                 j = j + 1
#             i = i + 1

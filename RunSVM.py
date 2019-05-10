#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 15:39
# @Author  : Jiayj
# @Site    : 
# @File    : RunSVM.py
# @Software: PyCharm

import os
cmd = 'svm-train -s 0 -t 2 -h 0 -b 1 -c 32768 -g 0.03125 /home/jiayj267/IMP/experiment/orderSample29.txt /home/jiayj267/IMP/experiment/orderSample29.model'
os.system(cmd)
# svm-train -s 0 -t 2 -h 0 -b 1 C:/Users/jiayj/Desktop/train.txt /home/jiayj267/OMPcontact/svm/MI/10/1/contact1.model'

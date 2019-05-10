#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/19 10:25
# @Author  : JYJ
# @Site    : 
# @File    : SVMPredictADCalculate.py
# @Software: PyCharm
import os
import pandas as pd
import math

class Predict:
    def __init__(self):
        """

        """

    def svmpredict(self, filename, filepath):
        pdbid = filename.split('.')[0]
        # cmd = 'svm-predict -b 1 ' + filepath + ' /home/jiayj267/IMP/libsvm-3.20/tools/ELSCNR3.model /home/jiayj267/IMP/nr/testing/predictresult/' + pdbid + '.result'
        cmd = 'svm-predict ' + filepath + ' /home/jiayj267/IMP/libsvm-3.20/tools/ELSCNR3.model /home/jiayj267/IMP/nr/testing/predictresult/' + pdbid + '.result'
        os.system(cmd)

    def calculate(self, filename):
        pdbid = filename.split('.')[0]
        labelpath = '/home/jiayj267/IMP/nr/testing/label/' + pdbid + '.txt'
        labelfile = pd.read_csv(labelpath, sep=' ', names=['siteone', 'sitetwo', 'result', 'label'])
        label = labelfile.iloc[:, 3]
        predictpath = '/home/jiayj267/IMP/nr/testing/predictresult/' + pdbid + '.result'
        predictfile = pd.read_csv(predictpath, sep=' ', names=['predictlabel'])
        predictlabel = predictfile.iloc[:,0]
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        if len(label) == len(predictlabel):
            for i in range(len(label)):
                if label[i] == '1' and predictlabel[i] == '1':
                    TP += 1
                elif label[i] == '0' and predictlabel[i] == '0':
                    TN += 1
                elif label[i] == '0' and predictlabel[i] == '1':
                    FP += 1
                elif label[i] == '1' and predictlabel[i] == '0':
                    FN += 1
            mcc = float(TP * TN - FP * FN) / (math.sqrt(TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mccfilepath = '/home/jiayj267/IMP/nr/testing/mccresult.txt'
            mccfile = open(mccfilepath, 'a')
            mccfile.write(pdbid + ' ' + str(mcc))
        else:
            print(pdbid + len(label) + len(predictlabel))


def main():
    rootdir = '/home/jiayj267/IMP/nr/testing/slidwindow/ELSC/predict'
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            print(filename)
            filepath = os.path.join(dirpath, filename)
            predict = Predict()
            # predict.svmpredict(filename, filepath)
            predict.calculate(filename)


if __name__ == '__main__':
    main()

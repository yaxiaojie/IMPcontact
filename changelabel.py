#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 20:59
# @Author  : Jiayj
# @Site    : 
# @File    : changelabel.py
# @Software: PyCharm
import pandas as pd
import os


class ChangeLabel:

    def __init__(self):
        """

        """

    def changelabel(self, oldfeaturedirpath, labeldirpath, newfeaturedirpath):
        oldfeaturefiles = os.listdir(oldfeaturedirpath)  # 得到文件夹下的所有文件名称
        for oldfeaturefile in oldfeaturefiles:  # 遍历文件夹
            oldfeaturepath = oldfeaturedirpath + "/" + oldfeaturefile
            oldfeature = pd.read_csv(oldfeaturepath, sep=' ', names=['Label', 'covariance',
                                                                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                                                     '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28','29', '30'])
            # oldfeature = pd.read_csv(oldfeaturepath, sep=' ', names=['Label', 'covariance',
            #                                                          '1', '2', '3', '4', '5', '6', '7', '8', '9',
            #                                                          '10', '11', '12', '13', '14', '15', '16', '17', '18'])
            a = len(oldfeature)
            labelfiles = os.listdir(labeldirpath)
            if oldfeaturefile in labelfiles:
                labelfilepath = labeldirpath + oldfeaturefile
                newlabelfile = pd.read_csv(labelfilepath, sep='\t', names=['site1', 'site2', 'result', 'label'])
                b = len(newlabelfile)
                if a == b:
                    newfeature = oldfeature
                    newlabel = newlabelfile.iloc[:, 3]
                    newfeature['Label'] = newlabel
                    newfeaturefilepath = newfeaturedirpath + "/" + oldfeaturefile
                    newfeature.to_csv(newfeaturefilepath, sep=' ', header=None, index=None)
                else:
                    print(oldfeaturefile + " " + str(a) + " " + str(b))
            else:
                print("LabelPath don't have the file" + oldfeaturefile)


def main():
    newlabel = ChangeLabel()
    newlabel.changelabel('/home/jiayj267/IMP/nr/slidwindow/ELSC/predict/', '/home/jiayj267/IMP/Data/5.5label/training/', '/home/jiayj267/IMP/nr/slidwindow/ELSC/5.5new/')


if __name__ == '__main__':
    main()

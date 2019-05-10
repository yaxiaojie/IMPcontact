#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:41
# @Author  : JYJ
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import os


class Covariance:

    def __init__(self):
        """

        """
    def runcovariance(self):
        rootdir = '/home/jiayj267/IMP/ThirdPartToolsResult/covariance/input/'
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                # filepath = os.path.join(dirpath, filename)
                # with open(filepath, 'r') as f:
                #     lines = f.readlines()
                pdbid = filename.split('.')[0]
                print(pdbid)
                cmd = 'java covariance.algorithms.McBASCCovariance /home/jiayj267/IMP/ThirdPartToolsResult/covariance/input/' + pdbid + '.txt /home/jiayj267/IMP/ThirdPartToolsResult/covariance/output/McBASC/' + pdbid + '.txt'
                os.system(cmd)
        # cmd = 'java covariance.algorithms.ELSCCovariance /home/jiayj267/IMP/ThirdPartToolsResult/covariance/input/1ar1_B.txt /home/jiayj267/IMP/ThirdPartToolsResult/covariance/output/ELSC/1ar1_B.txt'
        # os.system(cmd)


def main():
    covariance = Covariance()
    covariance.runcovariance()


if __name__ == '__main__':
    main()

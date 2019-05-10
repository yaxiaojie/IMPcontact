#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : PreDeal.py
# @Author  : JYJ
# @Time    : 2018/8/7 17:38
# @Desc  :
# @Software: PyCharm
import os
import numpy as np
import pandas as pd
import linecache
import random
##############   Cut the region sequence file    #################
# with open('D:/000000/IMPContact/data/non-redundant-alpha-id-sequence.txt', 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         for j in range(len(lines[i])):
#             if lines[i][j] == '>':
#                 file = open('D:/000000/IMPContact/data/non-redundant-alpha-id-sequence-two.txt', 'a')
#                 file.write('\n')
#                 file.write(lines[i][j])
#                 file.close()
#             else:
#                 file = open('D:/000000/IMPContact/data/non-redundant-alpha-id-sequence-two.txt', 'a')
#                 file.write(lines[i][j])
#                 file.close()
##############   Separate the all sequence file to single   #################
# with open('D:/000000/IMPContact/data/non-redundant-alpha-id-sequence-two.txt', 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         filename = lines[i][1:7]
#         print(filename)
#         address = 'D:/000000/IMPContact/sequence/'+filename+'.fasta'
#         file = open(address, 'w')
#         fastaid = lines[i][0:7]
#         sequence = lines[i][7:].replace(' ', '').strip('\n')
#         file.write(fastaid)
#         file.write('\n')
#         file.write(sequence)
#         file.close()

##############   Random separate training set and testing set   #################
# rootdir = 'D:/000000/IMPContact/sequence/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filename_list.append(filename)
#     # print(filename_list)
#     index = [i for i in range(len(filename_list))]
#     random.shuffle(index)
#     a = index[0:62]
#     b = index[62:]
#     # print(index)
#     # print(a)
#     # print(b)
#     training = []
#     testing = []
#     for i in a:
#         testing.append(filename_list[i])
#     for z in range(len(testing)):
#         file = open('D:/000000/IMPContact/testing.txt', 'a')
#         file.write(testing[z]+'\n')
#         file.close()
#     for j in b:
#         training.append(filename_list[j])
#     for m in range(len(training)):
#         file = open('D:/000000/IMPContact/training.txt', 'a')
#         file.write(training[m]+'\n')
#         file.close()
#     # print(testing)
#     # print(training)

##############   useless   #################
# with open('D:/000000/IMPContact/training.txt', 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         file = open('D:/000000/IMPContact/training2.txt', 'a')
#         file.write(lines[i][0:6]+'\n')
#         file.close()

# ##############   coordinate   #################
# rootdir = 'D:/000000/IMPContact/PDB分类/M/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         print(filename)
#         filelines = linecache.getlines(filepath)
#         for each_item in filelines:
#             # print(each_item)
#             if (each_item[0:4] == 'ATOM' and each_item[21] == 'M') and (
#                     each_item[13] == 'C' and each_item[14] == 'A') and (each_item[16] == ' ' or each_item[16] == 'A'):
#                 # atom_serial_number = each_item[6:11]
#                 residue_name = each_item[17:20]
#                 # x = each_item[17:20]
#                 y = each_item[22:26]
#                 z = each_item[31:54]
#                 pdbid = filename.split('.')[0]
#                 outfilepath = 'D:/000000/IMPContact/coordinate/' + pdbid + '.txt'
#                 writefile = open(outfilepath, 'a')
#                 line = str(residue_name) + '\t' + str(y) + '\t' + str(z) + '\n'
#                 writefile.write(line)
#                 writefile.close()

# ##############   coordinate test  #################
# rootdir = 'D:/000000/IMPContact/PDB分类/小v/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         print(filename)
#         filelines = linecache.getlines(filepath)
#         for each_item in filelines:
#             # print(each_item)
#             if (each_item[0:4] == 'ATOM' and each_item[21] == 'v') and (each_item[13] == 'C' and each_item[14] == 'A') and (each_item[16] == ' ' or each_item[16] == 'A'):
#                 # atom_serial_number = each_item[6:11]
#                 residue_name = each_item[17:20]
#                 # x = each_item[17:20]
#                 y = each_item[22:26]
#                 z = each_item[31:54]
#                 pdbid = filename.split('.')[0]
#                 outfilepath = 'D:/000000/IMPContact/coordinatetest/小v/' + pdbid + '.txt'
#                 writefile = open(outfilepath, 'a')
#                 # line = str(residue_name) + '\t' + str(y) + '\t' + str(z) + '\n'
#                 line = each_item
#                 writefile.write(line)
#                 writefile.close()


##############   cooperate label  #################
# rootdir = 'D:/000000/IMPContact/coordinatetest/222/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         pdbid = filename.split('.')[0]
#         filelines = linecache.getlines(filepath)
#         for each_item in filelines:
#             for i in range(len(each_item)):
#                 if each_item[i] == ' 'and each_item[i-1] == ' ':
#                     continue
#                 else:
#                     print(each_item[i])
#                     outfilepath = 'D:/000000/IMPContact/coordinatetest/' + pdbid + '.txt'
#                     writefile = open(outfilepath, 'a')
#                     a = each_item[i]
#                     writefile.write(a)
#                     writefile.close()
#                 i = i+1

##############   加尾缀  #################
# rootdir = 'D:/000000/IMPContact/coordinatetest/A/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         pdbid = filename.split('.')[0]
#         filelines = linecache.getlines(filepath)
#         for each_item in filelines:
#             outfilepath = 'D:/000000/IMPContact/coordinatetest/test/' + pdbid + '_A.txt'
#             writefile = open(outfilepath, 'a')
#             writefile.write(each_item)
#             writefile.close()

##############   多model  #################
# rootdir = 'D:/000000/IMPContact/new2/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         pdbid = filename.split('.')[0]
#         filelines = linecache.getlines(filepath)
#         coordinate = filelines
#         num = 0
#         total = 0
#         # print(filename)
#         first = coordinate[0].split(' ')[5]
#         for i in range(len(filelines)):
#             x = coordinate[i].split(' ')[5]
#             if x == first:
#                 num = num + 1
#         if num > 1:
#             print(pdbid)

##############   坐标错误修改  #################
# with open('C:/Users/Administrator/Desktop/5xjy_A.txt', 'r') as f:
#     lines = f.readlines()
#     # outfilepath = 'C:/Users/Administrator/Desktop/3jav.txt'
#     # writefile = open(outfilepath, 'a')
#     for i in range(len(lines)):
#
#         for j in range(len(lines[i])):
#             if lines[i][j] == 'A' and (lines[i][j+1] == '1' or lines[i][j+1] == '2' or lines[i][j+1] == '3' or lines[i][j+1] == '4' or lines[i][j+1] == '5'):
#                 outfilepath = 'C:/Users/Administrator/Desktop/5xjy.txt'
#                 writefile = open(outfilepath, 'a')
#                 writefile.write(str(lines[i][j]))
#                 writefile.write(' ')
#                 writefile.close()
#             else:
#                 outfilepath = 'C:/Users/Administrator/Desktop/5xjy.txt'
#                 writefile = open(outfilepath, 'a')
#                 writefile.write(str(lines[i][j]))
#                 writefile.close()


# with open('C:/Users/Jiayj/Desktop/4uwa_A.txt', 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         for j in range(len(lines[i])):
#             if lines[i][j] == '-' and lines[i][j-1] != ' ':
#                 outfilepath = 'C:/Users/Jiayj/Desktop/4uwa.txt'
#                 writefile = open(outfilepath, 'a')
#                 writefile.write(' ')
#                 writefile.write(str(lines[i][j]))
#
#                 writefile.close()
#             else:
#                 outfilepath = 'C:/Users/Jiayj/Desktop/4uwa.txt'
#                 writefile = open(outfilepath, 'a')
#                 writefile.write(str(lines[i][j]))
#                 writefile.close()

##############   坐标文件的序列统计  #################
# rootdir = 'D:/0data/IMPContact/new/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         filepath = os.path.join(dirpath, filename)
#         pdbid = filename.split('.')[0]
#         # f = pd.read_csv(filepath,)
#         # file = pd.read_csv(filepath, header=None)
#         # # for i in range(len(file)):
#         # amid_line = file.iloc[:, [1]]
#         # print(amid_line)
#         print(pdbid)
#         gradualamid = {'GLY': 'G', 'ALA': 'A', 'LEU': 'L', 'ILE': 'I', 'VAL': 'V', 'PRO': 'P', 'PHE': 'F', 'MET': 'M',
#                        'TRP': 'W', 'SER': 'S', 'GLN': 'Q', 'THR': 'T', 'CYS': 'C', 'ASN': 'N', 'TYR': 'Y', 'ASP': 'D',
#                        'GLU': 'E', 'LYS': 'K', 'ARG': 'R', 'HIS': 'H', 'ALYS': 'K', 'AGLU': 'E', 'UNK': 'U'}
#         outfilepath = 'C:/Users/Jiayj/Desktop/1/' + pdbid + '.txt'
#         writefile = open(outfilepath, 'a')
#         writefile.write('>' + pdbid + '\n')
#         with open(filepath, 'r') as f:
#             lines = f.readlines()
#             for i in range(len(lines)):
#                 amid = lines[i].split(' ')[3]
#                 if len(amid) == 4:
#                     amid = amid[1:]
#                 newamid = gradualamid[amid]
#                 outfilepath = 'C:/Users/Jiayj/Desktop/1/' + pdbid + '.txt'
#                 writefile = open(outfilepath, 'a')
#                 writefile.write(newamid)
#                 writefile.close()

##############   比较PDB序列和标签文件序列  #################
# with open('C:/Users/Jiayj/Desktop/pdb.txt', 'r') as f:
#     lines = f.readlines()
#     s1 = lines[1]
#     with open('C:/Users/Jiayj/Desktop/1ar1_B.fasta', 'r') as f2:
#         lines2 = f2.readlines()
#         s2 = lines2[1]
#         for i in range(len(s1)):
#             for j in range(len(s2)):
#                 if s1[i] == s2[j]:
#                     print(j)

##############   更改文件后缀  #################
# rootdir = 'D:/0data/IMPContact/pdb文件序列/testing/'
# # filename_list = []
# # for dirpath, dirnames, filenames in os.walk(rootdir):
# #     for filename in filenames:
# #         filepath = os.path.join(dirpath, filename)
# #         pdbid = filename.split('.')[0]
# #         with open(filepath, 'r') as f:
# #             lines = f.readlines()
# #             outfilepath = 'C:/Users/Jiayj/Desktop/13/' + pdbid + '.fasta'
# #             for i in range(len(lines)):
# #                 writefile = open(outfilepath, 'a')
# #                 writefile.write(lines[i])
# #                 writefile.close()

##############   更改SVM输入文件的标签  #################
# rootdir = 'C:/Users/Jiayj/Desktop/label/'
# filename_list = []
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         a = filename.split('.')[0]
#         filename_list.append(a)
# rootdir2 = 'C:/Users/Jiayj/Desktop/old/'
# filename_list2 = []
# for dirpath2, dirnames2, filenames2 in os.walk(rootdir2):
#     for filename2 in filenames2:
#         b = filename2.split('.')[0]
#         filename_list2.append(b)
# for i in range(len(filename_list)):
#     if filename_list[i] in filename_list2:
#         continue
#     else:
#         print(filename_list[i])

##############   总和所有序列的正负样本  #################
# rootdir = '/home/jiayj267/IMP/nr/slidwindow/ELSC/new/'
# positive = 0
# negative = 0
# for dirpath, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         print(filename)
#         filepath = os.path.join(dirpath, filename)
#
#         # positive = 0
#         # negative = 0
#         with open(filepath, 'r')as  f:
#             lines = f.readlines()
#             for i in range(len(lines)):
#                 if lines[i].split(' ')[0] == '1':
#                     writefile = open('/home/jiayj267/IMP/nr/svminput/ELSC/positive.txt', 'a')
#                     writefile.write(lines[i])
#                     positive += 1
#                 else:
#                     writefile = open('/home/jiayj267/IMP/nr/svminput/ELSC/negative.txt', 'a')
#                     writefile.write(lines[i])
#                     negative += 1
# print(positive)
# print(negative)

##############   总和所有序列的正负样本  #################
with open('/home/jiayj267/IMP/nr/svminput/ELSC/positive.txt', 'r')as f:
    lines = f.readlines()
    a = len(lines)
    print(a)
    with open('/home/jiayj267/IMP/nr/svminput/ELSC/negative.txt', 'r')as f2:
        lines2 = f2.readlines()
        print(len(lines2))
        index = [i for i in range(a)]
        random.shuffle(index)
        writefile = open('/home/jiayj267/IMP/nr/svminput/ELSC/ELSCnegative.txt', 'a')
        for i in index:
            writefile.write(lines2[i])

##############   打乱同数量的正负样本生成训练文件  #################
# with open('F:/000000/。。。/滑窗为3/ELSC/ELSCsvminput.txt', 'r')as f2:
#     lines2 = f2.readlines()
#     a = len(lines2)
#     index = [i for i in range(a)]
#     random.shuffle(index)
#     writefile = open('F:/000000/。。。/滑窗为3/ELSC/ELSCinput.txt', 'a')
#     for i in index:
#         writefile.write(lines2[i])

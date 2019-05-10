#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 19:43
# @Author  : Jiayj
# @Site    : 
# @File    : all.py
# @Software: PyCharm

import os
import numpy as np


class IMP:
    def __init__(self):
        """

        """

    ##############   PSIBLAST   #################
    def psiblast(self, filename, filepath):
        pdbid = filename.split('.')[0]
        cmd = '/home/ThirdPartTools/blast/bin/psiblast -evalue 10 -num_iterations 3 -db /home/ThirdPartTools/blast/db/nr -query ' + filepath + ' -outfmt 0 -out /home/jiayj267/IMP/nr/testing/psiblastout/' + pdbid + '.fm0 -out_ascii_pssm /home/jiayj267/IMP/nr/testing/pssm/' + pdbid + '.pssm -num_alignments 1500 -num_threads 48'
        os.system(cmd)

    ##############   HMMTOP   #################
    def hmmtop(self, filename, filepath):
        pdbid = filename.split('.')[0]
        os.chdir('/home/ThirdPartTools/hmmtop_2.1/')
        cmd = 'hmmtop -if=' + filepath + ' -pl -of=/home/jiayj267/IMP/nr/testing/hmmtop/' + pdbid + '.hmm'
        os.system(cmd)

    ##############   Convert HMMTOP result  #################
    def cover_hmmtop(self, filename):
        pdbid = filename.split('.')[0]
        firstline = '>' + pdbid + '\n'
        hmmtoppath = '/home/jiayj267/IMP/nr/testing/hmmtop/' + pdbid + '.hmm'
        with open(hmmtoppath, 'r') as f:
            lines = f.readlines()
            seq = ''
            i = 5
            while i <= len(lines)-2:
                pre = lines[i][10:]
                pre1 = pre.replace(' ', '')
                pre2 = pre1.replace('\n', '')
                seq = seq+pre2
                i = i+3
            parsedfile = open('/home/jiayj267/IMP/nr/testing/topology/'+pdbid+'.txt', 'w')
            parsedfile.write(firstline)
            for j in range(len(seq)):
                if seq[j] == 'I':
                    seq = seq[0:j] + 'i' + seq[j+1:]
                elif seq[j] == 'O':
                    seq = seq[0:j] + 'o' + seq[j+1:]
                elif seq[j] == 'H':
                    seq = seq[0:j] + 'm' + seq[j+1:]
            parsedfile.write(seq)
            parsedfile.close()

    ##############   MView  #################
    def mview(self, filename):
        pdbid = filename.split('.')[0]
        cmd = '/home/ThirdPartTools/mview-1.61/bin/mview -in blast -out fasta /home/jiayj267/IMP/nr/testing/psiblastout/' + pdbid + '.fm0 > /home/jiayj267/IMP/nr/testing/mview/' + pdbid + '.aln'
        os.system(cmd)

    ##############   Convert MView result  #################
    def convertmviewformat(self, lines):
        mviewout = []
        ll = []
        for i in range(len(lines)):
            if lines[i].startswith('>'):
                if ll != []:
                    new_seq = ''.join(ll)
                    mviewout.append(new_seq)
                mviewout.append(lines[i])
                ll = []
                i += 1
            else:
                line = str(lines[i].strip('\n'))
                ll.append(line)
        new_last = ''.join(ll)
        mviewout.append(new_last)
        return mviewout

    def convertcovarianceinput(self, filename):
        pdbid = filename.split('.')[0]
        filepath = '/home/jiayj267/IMP/nr/testing/mview/'+pdbid + '.aln'
        # for dirpath, dirnames, filenames in os.walk(rootdir):
        #     for filename in filenames:
        #         filepath = os.path.join(dirpath, filename)
        pdbid = filename.split('.')[0]
        with open(filepath, 'r') as f:
            lines = f.readlines()
            mview = self.convertmviewformat(lines)
            count = len(mview)
            i = 2
            inputfilepath = '/home/jiayj267/IMP/nr/testing/covariance/input/' + pdbid + '.txt'
            inputFile = open(inputfilepath, 'w')
            while i < count - 1:
                part1 = mview[i].split()[0][1:]
                part2 = mview[i + 1]
                line = part1 + '        ' + part2
                inputFile.write(line + '\n')
                i = i + 2
            inputFile.close()

    ##############   Covariance  #################
    def Covariance(self, filename):
        pdbid = filename.split('.')[0]
        cmd = 'java covariance.algorithms.ELSCCovariance /home/jiayj267/IMP/nr/testing/covariance/input/' + pdbid + '.txt /home/jiayj267/IMP/nr/testing/covariance/output/ELSC/' + pdbid + '.txt'
        os.system(cmd)

    ##############   ZScore  #################
    def zscore(self, filename):
        pdbid = filename.split('.')[0]
        filepath = '/home/jiayj267/IMP/nr/testing/covariance/output/ELSC/' + pdbid + '.txt'
        meannum, stdnum = self.getCalculationParameters(filepath)
        outfile = '/home/jiayj267/IMP/nr/testing/covariance/zscore/ELSC/' + pdbid + '_zscore.txt'
        writefile = open(outfile, 'w+')
        with open(filepath, 'r') as covariancelines:
            lines = covariancelines.readlines()
            for i in range(len(lines)):
                if i == 0:
                    zscorereturn = lines[0].replace('\n', '')
                else:
                    zscore = str((float(lines[i].split()[2]) - meannum) / stdnum)
                    zscorereturn = str(lines[i].split()[0]) + ' ' + str(lines[i].split()[1]) + ' ' + zscore
                writefile.write(zscorereturn + '\n')
            writefile.close()

    def getCalculationParameters(self, path):
        covariancescore = []
        with open(path, 'r') as f:
            covarianceLines = f.readlines()
            for linenum in range(1, len(covarianceLines)):
                covariancescore.append(float(covarianceLines[linenum].split()[2]))
            numarray = np.array(covariancescore)
            meannum = np.mean(numarray)
            stdnum = np.std(numarray)
            return meannum, stdnum

    def dealPssmFile(self, filename):
        pdbid = filename.split('.')[0]
        filepath = '/home/jiayj267/IMP/nr/testing/pssm/' + pdbid + '.pssm'
        residuePosition = {"A": 22, "R": 23, "N": 24, "D": 25, "C": 26, "Q": 27, "E": 28, "G": 29, "H": 30, "I": 31,
                           "L": 32, "K": 33, "M": 34, "F": 35, "P": 36, "S": 37, "T": 38, "W": 39, "Y": 40, "V": 41}
        with open(filepath, 'r') as f:
            lines = f.readlines()
            outfile = pdbid + '.txt'
            writefile = open('/home/jiayj267/IMP/nr/testing/feature/'+outfile, 'w+')
            for line in lines:
                lines = line.split()
                if len(lines) == 44:
                    residue = lines[1]
                    if residue == "U":
                        outline = residue + ' 1:0.00'
                    else:
                        position = residuePosition[residue]
                        ele = self.dealPssmfrequency(lines, position)
                        outline = residue + ' '+ele
                    writefile.write(outline + '\n')
            writefile.close()

    def dealPssmfrequency(self, lines, position):
        ele1 = str((round((int(lines[position])/100), 2)))
        if len(ele1) == 4:
            ele = ele1
        elif len(ele1) == 1:
            ele = ele1 + '.00'
        else:
            ele = ele1 + '0'
        return ele


    def dealTopologyFile(self, filename):
        pdbid = filename.split('.')[0]
        filepath = '/home/jiayj267/IMP/nr/testing/topology/' + pdbid + '.txt'
        residuePosition = {"i": 1, "m": 0, "o": -1}
        path = '/home/jiayj267/IMP/nr/testing/feature/' + pdbid + '.txt'
        with open(path, 'r') as f2:
            filelines = f2.readlines()
            with open(filepath, 'r') as f:
                topologyLines = f.readlines()
                for i in range(len(topologyLines[1])):
                    position = topologyLines[1][i]
                    positionResult = str(residuePosition[position])
                    newline = filelines[i].replace('\n', ' ')
                    newline += positionResult
                    writefile = open('/home/jiayj267/IMP/nr/testing/featurenew/'+pdbid+'.txt', "a")
                    writefile.write(newline + '\n')
                writefile.close()


    def getRelativeFeature(self, filename):
        pdbid = filename.split('.')[0]
        filepath = '/home/jiayj267/IMP/nr/testing/topology/' + pdbid + '.txt'
        with open(filepath, 'r')as f:
            topologyLines = f.readlines()
            path = '/home/jiayj267/IMP/nr/testing/featurenew/' + pdbid + '.txt'
            with open(path, 'r') as f2:
                filelines = f2.readlines()
                writefile = open(path, "w+")
                positionFlag = topologyLines[1][0]
                firstFlag = positionFlag
                changeCount = 1
                membraneCount = 0
                membraneBeginPos = 0
                for j in range(len(topologyLines[1])):
                    position = topologyLines[1][j]
                    if position != positionFlag:
                        positionFlag = position
                        changeCount += 1
                        if changeCount != 1:
                            if changeCount % 4 == 3:
                                if firstFlag == 'i':
                                    membraneBeginPos, membraneCount = self.reverseNumber(filelines, membraneCount,
                                                                                          membraneBeginPos, writefile)
                                else:
                                    membraneBeginPos, membraneCount = self.positiveNumber(filelines, membraneCount,
                                                                                           membraneBeginPos, writefile)
                            elif changeCount % 4 == 1:
                                if firstFlag == 'i':
                                    membraneBeginPos, membraneCount = self.positiveNumber(filelines, membraneCount,
                                                                                           membraneBeginPos, writefile)
                                else:
                                    membraneBeginPos, membraneCount = self.reverseNumber(filelines, membraneCount,
                                                                                          membraneBeginPos, writefile)
                    if position == 'm':
                        membraneCount += 1
                        if membraneBeginPos == 0:
                            membraneBeginPos = j
                    else:
                        newline = filelines[j].replace('\n', ' ')
                        newline += "0"
                        writefile.write(newline + '\n')
                writefile.close()

    def positiveNumber(self, filelines, membraneCount, membraneBeginPos, writefile):
        positionResult = 0
        for k in range(membraneCount):
            newline = filelines[k + membraneBeginPos].replace('\n', ' ')
            positionResult += 1
            newline += str(positionResult)
            writefile.write(newline + '\n')
        return 0, 0

    def reverseNumber(self, filelines, membraneCount, membraneBeginPos, writefile):
        for k in range(membraneCount):
            newline = filelines[k + membraneBeginPos].replace('\n', ' ')
            positionResult = str(membraneCount - k)
            newline += positionResult
            writefile.write(newline + '\n')
        return 0, 0


    def predictDataGenerate(self, filename):
        pdbid = filename.split('.')[0]
        with open('/home/jiayj267/IMP/nr/testing/covariance/zscore/ELSC/' + pdbid + '_zscore.txt', 'r')as f:
            covarianceLines = f.readlines()
            covariancecount = len(covarianceLines)
            featurefile = '/home/jiayj267/IMP/nr/testing/featurenew/' + pdbid + '.txt'
            with open(featurefile, 'r')as f2:
                featureLines = f2.readlines()
                featurecount = len(featureLines)
                outfile = '/home/jiayj267/IMP/nr/testing/slidwindow/ELSC/predict/' + pdbid + '.txt'
                writefile = open(outfile, "w+")
                orderpath = '/home/jiayj267/IMP/nr/testing/slidwindow/ELSC/order/' + pdbid + '.txt'
                orderfile = open(orderpath, "w+")
                for k in range(1, covariancecount):
                    aheadtwo = ""
                    aheadone = ""
                    backtwo = ""
                    aheadtwoofsec = ""
                    backoneofsec = ""
                    backtwoofsec = ""
                    firstpos = covarianceLines[k].split()[0]
                    secpos = covarianceLines[k].split()[1]
                    covariance = covarianceLines[k].split()[2]
                    if int(firstpos) == 0:
                        aheadtwo = " 2:-1 3:-2 4:-1"
                        aheadone = " 5:-1 6:-2 7:-1"
                        backtwoline = featureLines[int(firstpos) + 2].split()
                        backtwo = " 14:" + backtwoline[1] + " 15:" + backtwoline[2] + " 16:" + backtwoline[3]
                    elif int(firstpos) == 1:
                        aheadtwo = " 2:-1 3:-2 4:-1"
                        aheadoneline = featureLines[int(firstpos) - 1].split()
                        aheadone = " 5:" + aheadoneline[1] + " 6:" + aheadoneline[2] + " 7:" + aheadoneline[3]
                        backtwoline = featureLines[int(firstpos) + 2].split()
                        backtwo = " 14:" + backtwoline[1] + " 15:" + backtwoline[2] + " 16:" + backtwoline[3]
                    else:
                        if int(firstpos) == featurecount - 2:
                            backtwo = " 14:-1 15:-2 16:-1"
                        else:
                            backtwoline = featureLines[int(firstpos) + 2].split()
                            backtwo = " 14:" + backtwoline[1] + " 15:" + backtwoline[2] + " 16:" + backtwoline[3]
                        aheadtwoline = featureLines[int(firstpos) - 2].split()
                        aheadoneline = featureLines[int(firstpos) - 1].split()
                        aheadtwo = " 2:" + aheadtwoline[1] + " 3:" + aheadtwoline[2] + " 4:" + aheadtwoline[3]
                        aheadone = " 5:" + aheadoneline[1] + " 6:" + aheadoneline[2] + " 7:" + aheadoneline[3]
                    ownline = featureLines[int(firstpos)].split()
                    own = " 8:" + ownline[1] + " 9:" + ownline[2] + " 10:" + ownline[3]
                    backoneline = featureLines[int(firstpos) + 1].split()
                    backone = " 11:" + backoneline[1] + " 12:" + backoneline[2] + " 13:" + backoneline[3]
                    if int(secpos) == featurecount - 1:
                        backoneofsec = " 26:-1 27:-2 28:-1"
                        backtwoofsec = " 29:-1 30:-2 31:-1"
                        aheadtwoofsecline = featureLines[int(secpos) - 2].split()
                        aheadtwoofsec = " 17:" + aheadtwoofsecline[1] + " 18:" + aheadtwoofsecline[2] + " 19:" + \
                                        aheadtwoofsecline[3]
                    elif int(secpos) == featurecount - 2:
                        backtwoofsec = " 29:-1 30:-2 31:-1"
                        backoneofsecline = featureLines[int(secpos) + 1].split()
                        backoneofsec = " 26:" + backoneofsecline[1] + " 27:" + backoneofsecline[2] + " 28:" + \
                                       backoneofsecline[3]
                        aheadtwoofsecline = featureLines[int(secpos) - 2].split()
                        aheadtwoofsec = " 17:" + aheadtwoofsecline[1] + " 18:" + aheadtwoofsecline[2] + " 19:" + \
                                        aheadtwoofsecline[3]
                    else:
                        if int(secpos) == 1:
                            aheadtwoofsec = " 17:-1 18:-2 19:-1"
                        else:
                            aheadtwoofsecline = featureLines[int(secpos) - 2].split()
                            aheadtwoofsec = " 17:" + aheadtwoofsecline[1] + " 18:" + aheadtwoofsecline[2] + " 19:" + \
                                            aheadtwoofsecline[3]
                        backoneofsecline = featureLines[int(secpos) + 1].split()
                        backtwoofsecline = featureLines[int(secpos) + 2].split()
                        backoneofsec = " 26:" + backoneofsecline[1] + " 27:" + backoneofsecline[2] + " 28:" + \
                                       backoneofsecline[3]
                        backtwoofsec = " 29:" + backtwoofsecline[1] + " 30:" + backtwoofsecline[2] + " 31:" + \
                                       backtwoofsecline[3]
                    ownsecline = featureLines[int(secpos)].split()
                    ownsec = " 23:" + ownsecline[1] + " 24:" + ownsecline[2] + " 25:" + ownsecline[3]
                    aheadoneofsecline = featureLines[int(secpos) - 1].split()
                    aheadoneofsec = " 20:" + aheadoneofsecline[1] + " 21:" + aheadoneofsecline[2] + " 22:" + \
                                    aheadoneofsecline[3]
                    outelscline = "0 1:" + covariance + aheadtwo + aheadone + own + backone + backtwo + aheadtwoofsec + aheadoneofsec + ownsec + backoneofsec + backtwoofsec
                    writefile.write(outelscline + "\n")
                    orderfile.write(firstpos + ' ' + secpos + "\n")
                writefile.close()
                orderfile.close()


def main():

    #############   遍历文件夹中的所有文件进行下面的操作   #################
    rootdir = '/home/jiayj267/IMP/Data/pdbsequence/testing/'
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            print(filename)
            filepath = os.path.join(dirpath, filename)
            impcontact = IMP()
            # impcontact.psiblast(filename, filepath)
            # impcontact.hmmtop(filename, filepath)
            # impcontact.cover_hmmtop(filename)
            # impcontact.mview(filename)
            # impcontact.convertcovarianceinput(filename)
            impcontact.Covariance(filename)
            impcontact.zscore(filename)
            impcontact.dealPssmFile(filename)
            impcontact.dealTopologyFile(filename)
            impcontact.getRelativeFeature(filename)
            impcontact.predictDataGenerate(filename)


if __name__ == '__main__':
    main()

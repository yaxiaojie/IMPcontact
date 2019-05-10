#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : imp.py
# @Author  : JYJ
# @Time    : 2018/8/31 10:26
# @Desc  :
# @Software: PyCharm

import os
import numpy as np


class IMP:
    def __init__(self):
        """

        """

    """
    ##############   PSIBLAST   #################
    def psiblast(self, filename):
        # rootdir = '/home/jiayj267/IMP/Data/training/'
        pdbid = filename.split('.')[0]
        print(pdbid)
        cmd = '/home/songjz671/blast/bin/psiblast -evalue 10 -num_iterations 3 -db /home/songjz671/blast/db/uniprot -query /home/jiayj267/IMP/Data/pdbsequence/testing/' + pdbid + '.fasta -outfmt 0 -out /home/jiayj267/IMP/testingthirdpartresult/psiblastout/' + pdbid + '.fm0 -out_ascii_pssm /home/jiayj267/IMP/testingthirdpartresult/pssm/' + pdbid + '.pssm -num_alignments 1500 -num_threads 48'
        os.system(cmd)
        # /home/jiayj267/IMP/ThirdPartToolsResult/psiblastout

    
    ##############   HMMTOP   #################
    def hmmtop(self):
        # rootdir = '/home/jiayj267/IMP/Data/training/'
        pdbid = lines[0][1:7]
        print(pdbid)
        cmd = '/home/songjz671/newIMPcontact/hmmtop -if=/home/jiayj267/IMP/Data/training/' + pdbid + '.fasta -of=/home/jiayj267/IMP/ThirdPartToolsResult/hmmtop/' + pdbid + '.pl -pl'
        os.system(cmd)
    
    ##############   Convert HMMTOP result  #################
    def cover_hmmtop(self, filename, lines):
        # rootdir = '/home/jiayj267/IMP/ThirdPartToolsResult/hmmtop/'
        pdbid = filename.split('.')[0]
        print(pdbid)
        firstline = '>' + pdbid + '\n'
        seq = ''
        i = 5
        while i <= len(lines)-2:
            pre = lines[i][10:]
            pre1 = pre.replace(' ', '')
            pre2 = pre1.replace('\n', '')
            seq = seq+pre2
            i = i+3
        parsedfile = open('/home/jiayj267/IMP/testingthirdpartresult/topology/'+pdbid+'.txt', 'w')
        parsedfile.write(firstline)
        # print(seq)
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
        # rootdir = '/home/jiayj267/IMP/Data/training/'
        pdbid = filename.split('.')[0]
        print(pdbid)
        cmd = '/home/ThirdPartTools/mview-1.61/bin/mview -in blast -out fasta /home/jiayj267/IMP/testingthirdpartresult/psiblastout/' + pdbid + '.fm0 > /home/jiayj267/IMP/testingthirdpartresult/mview/' + pdbid + '.aln'
        os.system(cmd)

    
    ##############   Convert MView result  #################
    def convertmviewformat(self, lines):
        # with open(mviewpath, 'r') as mviewfiles:
        #     ll = []
        #     lines = mviewfiles.readlines()
        mviewout = []
        ll = []
        for i in range(len(lines)):
            if lines[i].startswith('>'):
                if ll != []:
                    new_seq = ''.join(ll)
                    mviewout.append(new_seq)
                    # print(mviewout)
                mviewout.append(lines[i])
                ll = []
                i += 1
            else:
                line = str(lines[i].strip('\n'))
                ll.append(line)
        new_last = ''.join(ll)
        mviewout.append(new_last)
        return mviewout

    def convertcovarianceinput(self):
        # with open(configpath, 'rb') as file:
        #     dict = pickle.load(file)
        #     covarianceinputfilepath = dict.get('covarianceInputFile')
        #     mviewoutfilepath = dict.get('MViewOutFilePath')
        rootdir = '/home/jiayj267/IMP/testingthirdpartresult/mview/'
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                pdbid = filename.split('.')[0]
                print(pdbid)
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                    mview = self.convertmviewformat(lines)
                    count = len(mview)
                    i = 2
                    inputfilepath = '/home/jiayj267/IMP/testingthirdpartresult/covariance/input/' + pdbid + '.txt'
                    inputFile = open(inputfilepath, 'w')
                    while i < count - 1:
                        part1 = mview[i].split()[0][1:]
                        part2 = mview[i + 1]
                        line = part1 + '        ' + part2
                        inputFile.write(line + '\n')
                        i = i + 2
                    inputFile.close()

    
    ##############   Covariance  #################
    def Covariance(self):
        rootdir = '/home/jiayj267/IMP/testingthirdpartresult/covariance/input/'
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                pdbid = filename.split('.')[0]
                print(pdbid)
                cmd = 'java covariance.algorithms.OmesCovariance /home/jiayj267/IMP/testingthirdpartresult/covariance/input/' + pdbid + '.txt /home/jiayj267/IMP/testingthirdpartresult/covariance/output/Omes/' + pdbid + '.txt'
                os.system(cmd)

    
    ##############   ZScore  #################
    def zscore(self):
        rootdir = '/home/jiayj267/IMP/testingthirdpartresult/covariance/output/Omes/'
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                meannum, stdnum = self.getCalculationParameters(filepath)
                pdbid = filename.split('.')[0]
                outfile = '/home/jiayj267/IMP/testingthirdpartresult/covariance/zscore/Omes/' + pdbid + '_zscore.txt'
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

    
    def dealPssmFile(self, filename, filepath):
        residuePosition = {"A": 22, "R": 23, "N": 24, "D": 25, "C": 26, "Q": 27, "E": 28, "G": 29, "H": 30, "I": 31,
                           "L": 32, "K": 33, "M": 34, "F": 35, "P": 36, "S": 37, "T": 38, "W": 39, "Y": 40, "V": 41}
        with open(filepath, 'r') as f:
            lines = f.readlines()
            outfile = filename.split('.')[0] + '.txt'
            writefile = open('/home/jiayj267/IMP/testingthirdpartresult/feature/'+outfile, 'w+')
            # writefile = open('C:/Users/Jiayj/Desktop/13/' + outfile, 'w+')
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

    
    def dealTopologyFile(self, filename, filepath):
        pdbid = filename.split('.')[0]
        print(pdbid)
        residuePosition = {"i": 1, "m": 0, "o": -1}
        path = '/home/jiayj267/IMP/testingthirdpartresult/feature/' + pdbid + '.txt'
        # writefile = open(path, "w")
        with open(path, 'r') as f2:
            filelines = f2.readlines()
            # print(filelines)
            with open(filepath, 'r') as f:
                topologyLines = f.readlines()
                for i in range(len(topologyLines[1])):
                    position = topologyLines[1][i]
                    positionResult = str(residuePosition[position])
                    # for j in range(len(filelines)):
                    newline = filelines[i].replace('\n', ' ')
                    newline += positionResult
                    # print(newline)
                    writefile = open('/home/jiayj267/IMP/testingthirdpartresult/feature2/'+pdbid+'.txt', "a")
                    writefile.write(newline + '\n')
                writefile.close()

   
    def getRelativeFeature(self, filename, filepath):
        pdbid = filename.split('.')[0]
        with open(filepath, 'r')as f:
            topologyLines = f.readlines()
            path = '/home/jiayj267/IMP/testingthirdpartresult/feature/' + pdbid + '.txt'
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

    
    
    def predictDataGenerate(self, filename, filepath):
        pdbid = filename.split('.')[0]
        with open('/home/jiayj267/IMP/testingthirdpartresult/covariance/zscore/Omes/' + pdbid + '_zscore.txt', 'r')as f:
            covarianceLines = f.readlines()
            covariancecount = len(covarianceLines)
            featurefile = '/home/jiayj267/IMP/testingthirdpartresult/feature/' + pdbid + '.txt'
            with open(featurefile, 'r')as f2:
                featureLines = f2.readlines()
                featurecount = len(featureLines)
                outfile = '/home/jiayj267/IMP/testingthirdpartresult/slidwindow/Omes/predict/' + pdbid + '.txt'
                writefile = open(outfile, "w+")
                orderpath = '/home/jiayj267/IMP/testingthirdpartresult/slidwindow/Omes/order/' + pdbid + '.txt'
                orderfile = open(orderpath, "w+")
                for k in range(1, covariancecount):
                    aheadtwo=""
                    aheadone=""
                    backtwo=""
                    aheadtwoofsec=""
                    backoneofsec=""
                    backtwoofsec=""
                    firstpos = covarianceLines[k].split()[0]
                    secpos = covarianceLines[k].split()[1]
                    covariance = covarianceLines[k].split()[2]
                    if int(firstpos) == 0:
                        aheadtwo = " 2:-1 3:-2 4:-1"
                        aheadone = " 5:-1 6:-2 7:-1"
                        backtwoline = featureLines[int(firstpos)+2].split()
                        backtwo = " 14:"+backtwoline[1]+" 15:"+backtwoline[2]+" 16:"+backtwoline[3]
                    elif int(firstpos) == 1:
                        aheadtwo = " 2:-1 3:-2 4:-1"
                        aheadoneline = featureLines[int(firstpos)-1].split()
                        aheadone = " 5:"+aheadoneline[1]+" 6:"+aheadoneline[2]+" 7:"+aheadoneline[3]
                        backtwoline = featureLines[int(firstpos)+2].split()
                        backtwo = " 14:"+backtwoline[1]+" 15:"+backtwoline[2]+" 16:"+backtwoline[3]
                    else:
                        if int(firstpos) == featurecount-2:
                            backtwo = " 14:-1 15:-2 16:-1"
                        else:
                            backtwoline = featureLines[int(firstpos)+2].split()
                            backtwo = " 14:"+backtwoline[1]+" 15:"+backtwoline[2]+" 16:"+backtwoline[3]
                        aheadtwoline = featureLines[int(firstpos)-2].split()
                        aheadoneline = featureLines[int(firstpos)-1].split()
                        aheadtwo = " 2:"+aheadtwoline[1]+" 3:"+aheadtwoline[2]+" 4:"+aheadtwoline[3]
                        aheadone = " 5:"+aheadoneline[1]+" 6:"+aheadoneline[2]+" 7:"+aheadoneline[3]
                    ownline = featureLines[int(firstpos)].split()
                    own = " 8:" + ownline[1] + " 9:" + ownline[2] + " 10:" + ownline[3]
                    backoneline = featureLines[int(firstpos)+1].split()
                    backone = " 11:"+backoneline[1]+" 12:"+backoneline[2]+" 13:"+backoneline[3]
                    if int(secpos) == featurecount-1:
                        backoneofsec = " 26:-1 27:-2 28:-1"
                        backtwoofsec = " 29:-1 30:-2 31:-1"
                        aheadtwoofsecline = featureLines[int(secpos)-2].split()
                        aheadtwoofsec = " 17:"+aheadtwoofsecline[1]+" 18:"+aheadtwoofsecline[2]+" 19:"+aheadtwoofsecline[3]
                    elif int(secpos) == featurecount-2:
                        backtwoofsec = " 29:-1 30:-2 31:-1"
                        backoneofsecline = featureLines[int(secpos)+1].split()
                        backoneofsec = " 26:"+backoneofsecline[1]+" 27:"+backoneofsecline[2]+" 28:"+backoneofsecline[3]
                        aheadtwoofsecline = featureLines[int(secpos)-2].split()
                        aheadtwoofsec = " 17:"+aheadtwoofsecline[1]+" 18:"+aheadtwoofsecline[2]+" 19:"+aheadtwoofsecline[3]
                    else:
                        if int(secpos) == 1:
                            aheadtwoofsec = " 17:-1 18:-2 19:-1"
                        else:
                            aheadtwoofsecline = featureLines[int(secpos)-2].split()
                            aheadtwoofsec = " 17:"+aheadtwoofsecline[1]+" 18:"+aheadtwoofsecline[2]+" 19:"+aheadtwoofsecline[3]
                        backoneofsecline = featureLines[int(secpos)+1].split()
                        backtwoofsecline = featureLines[int(secpos)+2].split()
                        backoneofsec = " 26:"+backoneofsecline[1]+" 27:"+backoneofsecline[2]+" 28:"+backoneofsecline[3]
                        backtwoofsec = " 29:"+backtwoofsecline[1]+" 30:"+backtwoofsecline[2]+" 31:"+backtwoofsecline[3]
                    ownsecline = featureLines[int(secpos)].split()
                    ownsec = " 23:" + ownsecline[1]+" 24:"+ownsecline[2]+" 25:"+ownsecline[3]
                    aheadoneofsecline = featureLines[int(secpos)-1].split()
                    aheadoneofsec = " 20:"+aheadoneofsecline[1]+" 21:"+aheadoneofsecline[2]+" 22:"+aheadoneofsecline[3]
                    outelscline = "-1 1:"+covariance+aheadtwo+aheadone+own+backone+backtwo+aheadtwoofsec+aheadoneofsec+ownsec+backoneofsec+backtwoofsec
                    writefile.write(outelscline+"\n")
                    orderfile.write(firstpos+' '+secpos+"\n")
                writefile.close()
                orderfile.close()
    """
    def getslidwindow(self, filename):
        pdbid = filename.split('.')[0]
        with open('/home/jiayj267/IMP/thirdresult/covariance/zscore/ELSC/' + pdbid + '_zscore.txt', 'r')as f:
            covarianceLines = f.readlines()
            covariancecount = len(covarianceLines)
            featurefile = '/home/jiayj267/IMP/feature_3kind/' + pdbid + '.txt'
            with open(featurefile, 'r')as f2:
                featureLines = f2.readlines()
                featurecount = len(featureLines)
                outfile = '/home/jiayj267/IMP/thirdresult/slidwindow/ELSC/predict/' + pdbid + '.txt'
                writefile = open(outfile, "w+")
                orderpath = '/home/jiayj267/IMP/thirdresult/slidwindow/ELSC/order/' + pdbid + '.txt'
                orderfile = open(orderpath, "w+")
                for k in range(1, covariancecount):
                    firstpos = covarianceLines[k].split()[0]
                    secpos = covarianceLines[k].split()[1]
                    covariance = covarianceLines[k].split()[2]
                    if int(firstpos) == 0:
                        ahead = " 2:-1 3:-2 4:-1"
                        backline = featureLines[int(firstpos) + 1].split()
                        back = " 8:" + backline[1] + " 9:" + backline[2] + " 10:" + backline[3]
                    else:
                        if int(firstpos) == featurecount - 1:
                            back = " 8:-1 9:-2 10:-1"
                        else:
                            backline = featureLines[int(firstpos) + 1].split()
                            back = " 8:" + backline[1] + " 9:" + backline[2] + " 10:" + backline[3]
                        aheadline = featureLines[int(firstpos) - 1].split()
                        ahead = " 2:" + aheadline[1] + " 3:" + aheadline[2] + " 4:" + aheadline[3]
                    ownline = featureLines[int(firstpos)].split()
                    own = " 5:" + ownline[1] + " 6:" + ownline[2] + " 7:" + ownline[3]
                    if int(secpos) == featurecount - 1:
                        backofsec = " 17:-1 18:-2 19:-1"
                    else:
                        backofsecline = featureLines[int(secpos) + 1].split()
                        backofsec = " 17:" + backofsecline[1] + " 18:" + backofsecline[2] + " 19:" + \
                                       backofsecline[3]
                    ownsecline = featureLines[int(secpos)].split()
                    ownsec = " 14:" + ownsecline[1] + " 15:" + ownsecline[2] + " 16:" + ownsecline[3]
                    aheadofsecline = featureLines[int(secpos) - 1].split()
                    aheadofsec = " 11:" + aheadofsecline[1] + " 12:" + aheadofsecline[2] + " 13:" + \
                                    aheadofsecline[3]
                    outelscline = "0 1:" + covariance + ahead + own + back + aheadofsec + ownsec + backofsec
                    writefile.write(outelscline + "\n")
                    orderfile.write(firstpos + ' ' + secpos + "\n")
                writefile.close()
                orderfile.close()


def main():
    # covar = IMP()
    # covar.Covariance()
    # convert = IMP()
    # convert.convertcovarianceinput()
    # zs = IMP()
    # zs.zscore()
    #############   遍历文件夹中的所有文件进行下面的操作   #################
    rootdir = '/home/jiayj267/IMP/feature_3kind/'
    # rootdir = 'C:/Users/Jiayj/Desktop/ThirdPartToolsResult/pssm/'
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            # hmm = IMP()
            # hmm.cover_hmmtop(filename)
            filepath = os.path.join(dirpath, filename)
            slid = IMP()
            slid.getslidwindow(filename)
            # slid.predictDataGenerate(filename, filepath)
            # pssm = IMP()
            # pssm.dealPssmFile(filename, filepath)
            # with open(filepath, 'r') as f:
            #     lines = f.readlines()
            #     hmm = IMP()
            #     hmm.cover_hmmtop(filename, lines)
            # psi = IMP()
            # psi.psiblast(filename)
            # top = IMP()
            # top.dealTopologyFile(filename, filepath)
            # rela = IMP()
            # rela.getRelativeFeature(filename, filepath)
    #         mv = IMP()
    #         mv.mview(filename)


if __name__ == '__main__':
    main()

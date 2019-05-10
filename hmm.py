import os,sys

path ='/home/jiayj267/IMP/Data/pdbsequence/testing/'
outpath ='/home/jiayj267/IMP/testingthirdpartresult/hmmtop/'
#cmd='export PATH=/home/ThirdPartTools/hmmtop_2.1/:$PATH'
#os.system(cmd)
#cmd='export LD_LIBRARY_PATH=/home/ThirdPartTools/hmmtop_2.1:$LD_LIBRARY_PATH'
#os.system(cmd)

s = os.listdir(path)
for i in s:
    if os.path.splitext(i)[1] == '.fasta':
        os.chdir('/home/ThirdPartTools/hmmtop_2.1/')
        cmd = 'hmmtop -if=' + path + i + ' -pl -of=' + outpath + i.split('.', 1)[0] + '.hmm'
        os.system(cmd) 

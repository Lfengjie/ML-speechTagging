# -*- coding: utf-8 -*-
import codecs, sys
from Util import Util
from pycrfsuite import Trainer
import codecs, sys

def getData(dataPath):
    xseqs = []
    yseqs = []
    xseq = []
    yseq = []
    originData = codecs.open(dataPath, 'r', 'utf-8')
    
    for line in originData.readlines():
        word_list = line.strip().split()
        if word_list:
            for word in word_list:
                single_word_list = word.split('/')
                if single_word_list[1] == "":
                    continue
                xseq.append(single_word_list[0].strip())
                yseq.append(single_word_list[1].strip())
        else:
            xseqs.append(xseq)
            yseqs.append(yseq)
            xseq = []
            yseq = []

    xseqs.append(xseq)
    yseqs.append(yseq)
    originData.close()

    return xseqs, yseqs

def trainer(util, xseqs, yseqs):
    trainer = Trainer('lbfgs')
    len_train = 0
    if util.isTest == False:
        len_train = int(len(xseqs) * 0.7)
    else:
        len_train = len(xseqs)

    for i in range(len_train):
        trainer.append(xseqs[i], yseqs[i])

    trainer.set("linesearch", "Backtracking")
    trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
    })
    # trainer.set("max_iterations", 400)
    trainer.train(util.moduleFilePath)


if __name__ == '__main__':
    util = Util()
    xseqs, yseqs = getData(util.originTrainDataPath)
    trainer(util, xseqs, yseqs)

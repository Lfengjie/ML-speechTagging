# -*- coding: utf-8 -*-
import codecs, sys
from Util import Util
from pycrfsuite import Tagger
import codecs, sys
import train

def getOriginData(dataPath):
    xOriginseqs, yOriginseqs = train.getData(dataPath)
    xseqs_len = len(xOriginseqs)
    xOriginseqs = xOriginseqs[int(xseqs_len * 0.7):xseqs_len]
    yOriginseqs = yOriginseqs[int(xseqs_len * 0.7):xseqs_len]
    yOriginseqs_oneList = []
    # for i in xOriginseqs[0]:
    #     print i
    for i in yOriginseqs:
        yOriginseqs_oneList.extend(i)
    return xOriginseqs, yOriginseqs_oneList

def getTagData(dataPath):
    xTagseqs, yTagseqs = train.getData(dataPath)
    yTagseqs_oneList = []
    # for i in xTagseqs[0]:
    #     print i
    for i in yTagseqs:
        yTagseqs_oneList.extend(i)

    return xTagseqs, yTagseqs_oneList

def getPrecisionAndRecall(yOriginseqs, yTagseqs):
    tags = list(set(yTagseqs))
    right_size = 0
    print "tag                     precision                       recall              FValue"
    for tag in tags:
        tpSize = 0
        tpSize_tags = yTagseqs.count(tag)
        tpSize_originTags = yOriginseqs.count(tag)
        for i in range(len(yOriginseqs)):
            if yOriginseqs[i] == tag and yOriginseqs[i] == yTagseqs[i]:
                tpSize = tpSize + 1

        precision = tpSize / (tpSize_tags * 1.0)
        recall = tpSize / (tpSize_originTags * 1.0)
        FValue = (2 * tpSize) / (tpSize_tags * 1.0 + tpSize_originTags * 1.0)
        right_size = right_size + tpSize

        str_evaluation = tag + "    " + str(precision) + "      " + str(recall) + "       " + str(FValue)
        print str_evaluation
    precision_all = right_size / (len(yOriginseqs) * 1.0)
    strprecision_all = "all precision      " + str(precision_all)
    print strprecision_all

if __name__ == '__main__':
    util = Util()
    xOriginseqs, yOriginseqs = getOriginData(util.originTrainDataPath);
    xTagseqs, yTagseqs = getTagData(util.testTagPath)
    getPrecisionAndRecall(yOriginseqs, yTagseqs)
# -*- coding: utf-8 -*-
import codecs, sys
from Util import Util
from pycrfsuite import Tagger
import codecs, sys

def getTestData_train(util, dataPath):
    xseqs = []
    xseq = []
    tagData = codecs.open(dataPath, 'r', 'utf-8')

    for line in tagData.readlines():
        word_list = line.strip().split()
        if word_list:
            for word in word_list:
                single_word_list = word.split('/')
                if util.isTest == False:
                    if single_word_list[1] == "":
                        continue
                xseq.append(single_word_list[0].strip())
        else:
            xseqs.append(xseq)
            xseq = []

    xseqs.append(xseq)
    tagData.close()
    return xseqs

# def getTestData(util, dataPath):
#     xseqs = []
#     xseq = []
#     tagData = codecs.open(dataPath, 'r', 'utf-8')

#     for line in tagData.readlines():
#         word_list = line.strip().split()
#         if word_list:
#             for word in word_list:
#                 single_word_list = word.split('/')
#                 if util.isTest == False:
#                     if single_word_list[1] == "":
#                         continue
#                 xseq.append(single_word_list[0].strip())
#         else:
#             xseqs.append(xseq)
#             xseq = []

#     xseqs.append(xseq)
#     tagData.close()
#     return xseqs

def tagging(util, xseqs, endTags):
    tags = []
    tagData = codecs.open(util.testTagPath, 'w', 'utf-8')
    tagger = Tagger()
    tagger.open(util.moduleFilePath)

    for xseq in xseqs:
        tagger.set(xseq)
        tag = tagger.tag()
        tags.append(tag)

        for i in range(len(xseq)):
            tagData.write(xseq[i].strip())
            tagData.write("/")
            tagData.write(tag[i].strip())
            if xseq[i] in endTags:
                tagData.write("\n")
            else:
                tagData.write(" ")
        tagData.write("\n")
        
def test(xseqs):
    xseqs_len = len(xseqs)
    testXseqs = xseqs[int(xseqs_len * 0.7):xseqs_len]
    return testXseqs

if __name__ == '__main__':
    util = Util()
    endTags = [u"，", u"。", u"；", u"：", u"…", u"？"]
    if util.isTest == False:
        xseqs = getTestData_train(util, util.originTrainDataPath)
        tagging(util, test(xseqs), endTags)
    else:
        xseqs = getTestData_train(util, util.originTestDataPath)
        tagging(util, xseqs, endTags)

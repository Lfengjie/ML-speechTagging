# -*- coding: utf-8 -*-
import re

class Util(object):
    """The Util Data
    这个文档类主要用于存放固定的数据类型

    Attributes:
        discard: 处理网页时,没有获得任何特征的网页rank存放这个文件中

    """
    def __init__(self):
        super(Util, self).__init__()

        self.originTrainDataPath = "../data/originData/train_utf16.tag"
        self.originTestDataPath = "../data/originData/test_utf16.tag"

        # self.moduleFilePath = "../data/generateData/module"
        # self.moduleFilePath = "../data/generateData/module_linerSearch_Backtracking"
        # self.testTagPath = "../data/generateData/tag.tag"

        self.moduleFilePath = "../data/generateData/module_all"
        self.testTagPath = "../data/generateData/tag.txt"

        self.isTest = True

    def str_strip(self, inputStr):
        replacedStr = re.sub("[^a-zA-Z0-9]", " ", str(inputStr))
        string = re.sub("\s+", " ", replacedStr)
        return string.strip()
        
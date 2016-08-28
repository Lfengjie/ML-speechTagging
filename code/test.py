# -*- coding: utf-8 -*-
import re, os, csv, sys
import codecs
from pycrfsuite import Trainer

# def hh():
#     a = 1
#     b = 2
#     return a, b

# reload(sys)
# sys.setdefaultencoding('utf-8')
# sq = []
# s1 = [1,2,3]
# s1.append(3)
# sq.append(s1)
# #mtext.write(str1)

# print sq


# a, b = hh()
# print a
# print b
trainer = Trainer()
print trainer.get_params()
for (k,v) in  trainer.get_params().items():
    print trainer.help(k)
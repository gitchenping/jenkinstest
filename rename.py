
import os
filedir='E:\我的书库\英语\听书学英语\谁动了我的奶酪'

[os.rename(os.path.join(filedir,file),os.path.join(filedir,file+".wma")) for file in os.listdir(filedir) ]
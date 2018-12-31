
import os

srcdir="E:\\我的书库\\音频\\上帝之饮"
[os.rename(os.path.join(srcdir,file),os.path.join(srcdir,file+".wma")) for file in os.listdir(srcdir) if not file.endswith("wma")]
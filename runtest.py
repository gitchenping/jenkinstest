import time
import os
import sys
import json.loads

import suit
import HTMLTestRunnerCN
#run
if __name__ == '__main__':
    # 添加Suite
    print("run start....")
    suiteTest=suit.suite()

    #确定生成报告的路径
    time_str=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(__file__)) + "\\report\\"
    filename ="wap_" + time_str + ".html"
    filefullpath=file_path+filename

    fp = open(filefullpath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'wap自动化测试报告',
        #description='详细测试用例结果',
        # tester=u"DKDtester"
        )
    #运行测试用例

    runner.run(suiteTest)
    # 关闭文件，否则会无法生成文件
    fp.close()
    print("run complete!")

import unittest
from common import HTMLTestRunner_cn
# 用例路径
casePath = r'C:\web_test\testcase'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
print(discover)

reportPath = 'C:\\web_test\\report\\' + 'result.html'

fp = open(reportPath, 'wb')
my_run = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='报告的title', description='描述报告干嘛的')

my_run.run(discover)
import unittest  # 导入数据库
from BeautifulReport import BeautifulReport
import os

DIR = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录，os系统命令。跟随当前目录虽在位置，是不会变化的。
# 可以实现环境模块的切换
# Environ_offline = '/env_config/offline'
Environ_online = '/env_config/online'


def run(test_suite):
    # 定义输出文件和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description="测试报告", report_dir=DIR)  # dir是存储目录,


if __name__ == '__main__':
    strategy = "all"
    if strategy == 'smoke':
        pattern = 'test_level1.py'
        suite = unittest.TestLoader().discover("./text_case", pattern)
    else:
        suite = unittest.TestLoader().discover("./text_case",
                                               "test*.py")  # 把目录名写，自动遍历目录下所有，必须是一个包！                                          # runner = unittest.TextTestRunner()使用Beautiful库就不用这个了
    run(suite)

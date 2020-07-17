""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

爬取AO3的小说
"""

import io
import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import os


class Ao3:
    def __init__(self):
        self.url = "https://archiveofourown.org/"
        self.ua = UserAgent()
        self.headers = {
            # "Cookie": "",
            "User-Agent": self.ua.random,  # 获取随机的User-Agent
        }

    def get_ao3_novel(self):
        # 访问主网页
        res = requests.get(self.url, headers=self.headers)
        # print(res.text)
        root = etree.HTML(res.text)
        novel_path = root.xpath('//*[@id="medium_4"]/a/@href')[0]
        print(novel_path)
        novel_path = 'https://archiveofourown.org' + novel_path
        # 访问
        res = requests.get(novel_path, headers=self.headers)
        print(res.text)









if __name__ == '__main__':
    path = "D:/imagetest/"
    ao = Ao3()
    ao.get_ao3_novel()





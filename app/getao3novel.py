""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

爬取AO3的小说
"""

import requests
from lxml import etree
from fake_useragent import UserAgent
import os


class Ao3:
    def __init__(self):
        self.url = "https://www.archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D="
        self.ua = UserAgent()
        self.headers = {
            "User-Agent": self.ua.random,  # 获取随机的User-Agent
        }

    def get_ao3_novel(self):
        # 访问主网页
        home_url = self.url + "大天狗"
        res = requests.get(home_url, headers=self.headers)
        # print(res.text)
        root = etree.HTML(res.text)
        novel_title = root.xpath('//*[@id="work_20845193"]/div/h4/a[1]/text()')[0]
        novel_path = root.xpath('//*[@id="work_20845193"]/div/h4/a[1]/@href')[0]
        # print(novel_title)
        # print(novel_path)
        novel_path = 'https://archiveofourown.org' + novel_path + '?view_adult=true'
        print(novel_path)
        res = requests.get(novel_path, headers=self.headers)
        root = etree.HTML(res.text)
        print(res.text)
        novel_text_list = root.xpath('//*[@id="chapters"]/div/p[1]/text()')
        # print(novel_text)
        if not os.path.exists(path + novel_title + '.txt'):
            os.mkdir(path + novel_title + '.txt')
        for novel_text in novel_text_list:
            open(path + novel_title + '.txt', 'a').write(novel_text)
            open(path + novel_title + '.txt', 'a').write('\n')





# 动态ip 多线程 定位排错








if __name__ == '__main__':
    path = "D:/Ao3/"
    ao = Ao3()
    ao.get_ao3_novel()





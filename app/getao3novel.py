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

    def get_ao3_novel_path_map(self):
        # 访问主网页,获取小说地址
        novel_path_map = {}
        home_url = self.url + "大天狗"
        for page_num in range(2):
            res = requests.get(home_url, headers=self.headers)
            root = etree.HTML(res.text)
            novel_title_list = root.xpath('//*[@class="work index group"]/li/div/h4/a[1]/text()')
            novel_path_list = root.xpath('//*[@class="work index group"]/li/div/h4/a[1]/@href')
            next_page = root.xpath('//*[@class="next"]/a/@href')[0]
            home_url = "https://archiveofourown.org" + next_page
            print(home_url)
            for i in range(len(novel_title_list)):
                novel_path_map.setdefault(novel_title_list[i], "https://archiveofourown.org" + novel_path_list[i] + "?view_adult=true")
        return novel_path_map


    def get_ao3_novel(self, novel_path_map, file_path):
        for key in novel_path_map:
            print(key)
            print(novel_path_map.get(key))
            res = requests.get(novel_path_map.get(key), headers=self.headers)
            root = etree.HTML(res.text)
            # print(res.text)
            novel_text_list = root.xpath('//*[@id="chapters"]/div/p/text()')

            # 创建文件，写入内容（文件命名不能有 /）
            novel_title = key.replace('/', ' ')
            novel_title = novel_title.replace('|', ' ')
            novel_path = file_path + novel_title + '.txt'
            print(novel_path)
            try:
                f = open(novel_path, 'a', encoding = 'utf-8')
                for novel_text in novel_text_list:
                    f.write(novel_text)
                    f.write('\n')
            except Exception as e:
                print("写入失败，失败原因：" + str(e))
# 动态ip 多线程 定位排错


if __name__ == '__main__':
    file_path = "D:/Ao3/"
    ao = Ao3()
    novel_path_map = ao.get_ao3_novel_path_map()
    ao.get_ao3_novel(novel_path_map, file_path)




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
from selenium import webdriver
import os
import io


class Ao3:
    def __init__(self):
        self.url = "https://www.zhihu.com/"
        self.jiandan_url = "http://jandan.net/ooxx/MjAyMDA3MjUtMTI"
        self.ua = UserAgent()
        self.headers = {
            # 获取随机的User-Agent
            "User-Agent": self.ua.random ,
            "referer":  "https://www.zhihu.com/"
        }

    def get_ao3_novel(self):
        # 访问主网页
        res = requests.get(self.url, headers=self.headers)
        res.encoding='utf-8'
        print(res.text)
        root = etree.HTML(res.text)
        novel_path = root.xpath('//*[@class="cp-pagenavi"]/div[0]/meta[1]/@content')
        novel_path = root.xpath('//*[@id="root"]/div/main/div/div[1]/div/div/ul/li[2]/a/text()')
        print(novel_path)


    def selenium_test(self):
        browser = webdriver.Chrome()
        browser.get('https://www.zhihu.com/')
        html = browser.page_source
        browser.quit()  # 关闭浏览器
        print(html)

    # 打开浏览器模拟请求
    def get_jiandan(self):
        picturl_path_list = []
        for i in range(10):
            print(i)
            jiandan_url = self.jiandan_url + str(i)
            # 访问主网页
            res = requests.get(self.jiandan_url, headers=self.headers)
            res.encoding='utf-8'
            # print(res.text)
            root = etree.HTML(res.text)
            picturl_path_list = picturl_path_list + root.xpath('//*[@class="commentlist"]/li/div/div/div[2]/p/a/@href')
            print(picturl_path_list)
        return picturl_path_list

    # 根据图片url下载图片到本地
    def fetch_img(self, path, data_list):
        if not os.path.exists(path):
            os.mkdir(path)

        x = 0
        for list in data_list:
            list = "http:" + list
            print(list)
            ir = requests.get(list)
            # 下载图片到本地
            open(path + '%d.jpg' % x, 'wb').write(ir.content)
            x += 1

if __name__ == '__main__':
    ao = Ao3()
    path = "D:/picture/JianDan/"
    # ao.get_ao3_novel()
    # ao.selenium_test()
    picturl_path_list = ao.get_jiandan()
    picturl_path_list = list(set(picturl_path_list))
    print(picturl_path_list)
    ao.fetch_img(path,picturl_path_list)




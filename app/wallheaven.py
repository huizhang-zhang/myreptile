""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

爬取网页壁纸并下载
"""


import requests
from lxml import etree
from fake_useragent import UserAgent
from selenium import webdriver
import os
import io
from pyquery import PyQuery as pq 
import time

class Ao3:
    def __init__(self,url):
        self.url = url
        self.ua = UserAgent()
        self.headers = {
            # 获取随机的User-Agent
            "User-Agent": self.ua.random ,
            "referer":  "https://www.zhihu.com/"
        }

    # 获取照片地址列表
    def get_pic_list(self):
        picturl_path_list = []
        url = self.url
        # 访问主网页
        res = requests.get(url, headers=self.headers)
        res.encoding='utf-8'
        html = etree.HTML(res.text)
        urllist = html.xpath('//*[@id="main"]//div//section//ul//li//figure/a/@href')
        num = 1
        for i in urllist:   
            res2 = requests.get(i)
            res2.encoding = 'utf-8'
            html2 = etree.HTML(res2.text)
            url1 = html2.xpath('//*[@id="main"]/section/div/img/@src')
            print('解析图片%d中... ' %(100*n + num) )
            num += 1
            try:
                picturl_path_list.append(url1[0])
            except:
                print("图片解析错误")
                continue
        return picturl_path_list
  
    # 根据图片url下载图片到本地
    def fetch_img(self, path, data_list):
        if not os.path.exists(path):
            os.mkdir(path)

        x = 1
        m = n
        for pic in data_list:
            picPath = path + str(100*m + x) + pic[-4:]
            ir = requests.get(pic)
            while os.path.exists(picPath):
                m += 1
                picPath = path + str(100*m + x) + pic[-4:]
            # 下载图片到本地
            open(picPath, 'wb').write(ir.content)
            print('下载图片%d中...' %(100*m + x) )
            x += 1


if __name__ == '__main__':
    for n in range(1, 100):
        try:
            url = "https://wallhaven.cc/random?seed=o5jTX&page=" + str(n)
            path = "D:/picture/wallHeaven/"
            if not os.path.exists(path):
                os.mkdir(path)
            print("=====================================")
            print("数据源网址是：" + url)
            print("存储路径是：" + path)
            print("=====================================")
            ao = Ao3(url)
            picturl_path_list = ao.get_pic_list()
            picturl_path_list = list(set(picturl_path_list))
            ao.fetch_img(path,picturl_path_list)
        except:
            print("error")
            continue
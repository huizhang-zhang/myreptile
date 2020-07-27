""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

爬取jabil网页缩写文件
"""

import requests
from selenium import webdriver
from fake_useragent import UserAgent



class ReptileTest:
    def __init__(self):
        self.url = "http://jabil.sharepoint.com/cns/employees/Pages/Acronym-List.aspx#Z"
        self.ua = UserAgent()
        self.headers = {
            # "cookie": "ctoken=f374f64f01f946739825f8e05dd4e9d7; Max-Age=43200; Path=/; Expires=Mon, 27 Jul 2020 13:24:42 GMT",
            "User-Agent": self.ua.random,  # 获取随机的User-Agent
        }

    # 获取图片url
    def getIntPages(self):

        # 访问主网页
        res = requests.get(self.url, headers=self.headers)
        print(res.text)
        # root = etree.HTML(res.text)
        # novel_title = root.xpath('//*[@id="work_20845193"]/div/h4/a[1]/text()')[0]





if __name__ == '__main__':
    rt = ReptileTest()
    rt.getIntPages()





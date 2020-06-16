""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

爬取下载百度图片
"""

import io
import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import os


class ReptileTest:
    def __init__(self):
        self.url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B6%AF%C2%FE%B1%DA%D6%BD&fr=ala&ala=1&pos=0&alatpl=wallpaper&oriquery=%E5%8A%A8%E6%BC%AB%E5%A3%81%E7%BA%B8"
        self.ua = UserAgent()
        self.headers = {
            "Cookie": "PSTM=1592207600; BIDUPSID=F8664C1881AF7F2A7F91737947F97635; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=8AB553CA11874217DDC92470819F778B:FG=1; indexPageSugList=%5B%22ni%22%5D; H_PS_PSSID=1443_21121_31253_32046_30824_26350; delPer=0; PSINO=3; BDSFRCVID=X6LsJeCCxG3_b6Jug5l_j8Yqc0CH6AQX2liC3J; H_BDCLCKID_SF=tbkD_C-MfIvhDRTvhCcjh-FSMgTBKI62aKDsKJox-hcqEpO9QTbr-6Kp5fJi0lLL25vfKIJnWIQNVfP4h-rTDUThDNtDt60jfn3tWJTOaj6jDbTnMIT8bKCShUFsXT5r-2Q-5hOy3KOrHCQ_5tthhh4qebrD55OmWncCbxP-anTThpFu-n5jHjJ0ja_j3J; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala",
            "User-Agent": self.ua.random,  # 获取随机的User-Agent
        }

    # 获取图片url
    def getIntPages(self, keyword, pages):
        params = []
        for i in range(30, 30*pages+30, 30):
            params.append({
                'tn':'resultjson_com',
                'ipn': 'rj',
                'ct':'201326592',
                'is': '',
                'fp': 'result',
                'queryWord': keyword,
                'cl': '2',
                'lm': '-1',
                'ie': 'utf-8',
                'oe': 'utf-8',
                'st': '-1',
                'ic': '0',
                'word': keyword,
                'face': '0',
                'istype': '2',
                'nc': '1',
                'pn': i,
                'rn': '30'
            })
        print(params)
        url = 'https://image.baidu.com/search/acjson'
        urls = []
        for i in params:
            content = requests.get(url, params=i).text
            # 正则获取方法
            img_urls = re.findall(r'"thumbURL":"(.*?)"', content)
            print(img_urls)
            urls.append(img_urls)
            # urls.append(requests.get(url,params = i).json().get('data'))开始尝试的json提取方法
            # print("%d times : " % x, img_urls)
        return urls

    # 根据图片url下载图片到本地
    def fetch_img(self, path, data_list):
        if not os.path.exists(path):
            os.mkdir(path)

        x = 0
        for list in data_list:
            for i in list:
                print("=====downloading %d/1500=====" % (x + 1))
                print(i)
                ir = requests.get(i)
                # 获取图片的大小KB
                image_b = io.BytesIO(ir.content).read()
                size = len(image_b)
                open(path + '%d.jpg' % x, 'wb').write(ir.content)
                x += 1
                # print(size)
                # if size > 1:
                #     print(1)
                #     # 写入图片
                #     open(path + '%d.jpg' % x, 'wb').write(ir.content)
                #     x += 1


if __name__ == '__main__':
    file = "D:/imagetest/"
    rt = ReptileTest()
    # 依据蔬菜关键词获取50页的图片列表，每页30张图片
    dataList = rt.getIntPages('动漫美图', 50)
    # 存取图片
    rt.fetch_img(file, dataList)





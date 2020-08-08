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


if __name__ == '__main__':
    home_url = "https://archiveofourown.org/works/14068860?view_adult=true"
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,  # 获取随机的User-Agent
    }

    res = requests.get(home_url, headers=headers)
    print(res.text)
    root = etree.HTML(res.text)
    novel_title_list = root.xpath('//*[@class="userstuff module"]/p/text()')
    print(novel_title_list)




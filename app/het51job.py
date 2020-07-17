""""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

抓取智联招聘网站信息
"""

from urllib import request
import re


def downdate(url):
    return request.urlopen(url).read()

def get_number(str):
    restr = """<div class="rt">([\\s\\S]*?)</div>"""
    return re.findall(restr, str)


if __name__ == '__main__':
    city_name_map = {'上海': '020000', '北京': '010000', '无锡': '070400'}
    search_name_list = ['python', 'java']
    search_name = ""
    city_name = ""
    result_map = {}
    for city_name,city_code in city_name_map.items():
        for search_name in search_name_list:
            url = "https://search.51job.com/list/" + city_code +"%252C010000,000000,0000,01,9,99," + search_name +",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
            down = downdate(url)
            # print(bytes.decode(down, encoding="gb18030"))
            page_list = get_number(bytes.decode(down, encoding="gb18030"))
            if len(page_list) == 0:
                print("爬取失败")
            else:
                num_list = re.findall("共(\\d+)条职位",page_list[0])
                if len(num_list) == 0:
                    print("爬取失败")
                else:
                    result_map.setdefault(city_name + search_name,num_list[0])
    print(result_map)
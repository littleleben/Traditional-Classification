import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import lxml


class ZhilianSpider(object):

    url = 'https://sou.zhaopin.com/?'
    def __init__(self,jl,kw,start_page,end_page):
        self.jl =jl
        self.kw =kw
        self.start_page =start_page
        self.end_page =end_page

    def handle_request(self,page):
        data = {

            'jl':self.jl,
            'kw':self.kw,
            'p':page,
            'sf':0,
            'st':0,
            'kt':4,

        }

        url_now = self.url +urllib.parse.urlencode(data)###如果是表单要记得处理一下
        ##构建请求对象发送请求
        headers = {
            'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            'Cookie': 'anonymid=jzox8gtw-vad1pq; depovince=JS; _r01_=1; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C19e4492c1b8383305862c9d7d1b0b8c5%7C1566613839259%7C1%7C1566613840104; JSESSIONID=abcyAJ3o1SPqXcnA2FbZw; ick_login=59f79762-5591-484a-8b9a-289d8fc4db0c; wp_fold=0; ick=53af59fc-85e1-4508-a579-0caa1af04928; jebecookies=20459254-6fb8-4b69-a201-3209310cdb9c|||||; _de=11393ADFE3F26CC8D89AADF4B0420A80; p=6f2a1ad1ead406b7c63564d8eb74f2766; first_login_flag=1; ln_uact=15951840090; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=be1e1e563d48ebc02422b9e29ccd05d16; societyguester=be1e1e563d48ebc02422b9e29ccd05d16; id=972032866; xnsid=3e7a788e; ver=7.0; loginfrom=null; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C2d04cc3ce01b4d4a5ce62827de6f3706%7C1566614851140%7C1%7C1566614851977'

        }
        request = urllib.request.Request(url=url_now,headers=headers)
        return request

    def parse_content(self,content):
        ##生成对象
        soup = BeautifulSoup(content,'lxml')
        ###思路！：先找到所有的table，因为一个工作岗位就一个table，遍历这个table的列表，然后通过table对象的selcet、dind方法去找每一条记录的具体信息
        div_list = soup.select('#"listContent" class="contentpile__content">#contentpile__content__wrapper clearfix')
        print(div_list)
        print(len(div_list))



    def run (self):
        for page in range(self.start_page,self.end_page+1):
            request = self.handle_request(page)

            content = urllib.request.urlopen(request).read().decode()
            ##解析内容
            self.parse_content(content)


def main():
    jl = input('请输入工作地点：')
    kw = input('请输入工作关键字：')

    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    ###创建对象，启动爬取程序
    spider = ZhilianSpider(jl,kw,start_page,end_page)
    spider.run()

if __name__ =='__main__':
    main()
import urllib.request
import urllib.parse
import re
import os
import time




def handle_request(url,page=None):
    if page != None:
        url = url +str(page)+'.html'
    headers ={

        'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        'Cookie': 'anonymid=jzox8gtw-vad1pq; depovince=JS; _r01_=1; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C19e4492c1b8383305862c9d7d1b0b8c5%7C1566613839259%7C1%7C1566613840104; JSESSIONID=abcyAJ3o1SPqXcnA2FbZw; ick_login=59f79762-5591-484a-8b9a-289d8fc4db0c; wp_fold=0; ick=53af59fc-85e1-4508-a579-0caa1af04928; jebecookies=20459254-6fb8-4b69-a201-3209310cdb9c|||||; _de=11393ADFE3F26CC8D89AADF4B0420A80; p=6f2a1ad1ead406b7c63564d8eb74f2766; first_login_flag=1; ln_uact=15951840090; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=be1e1e563d48ebc02422b9e29ccd05d16; societyguester=be1e1e563d48ebc02422b9e29ccd05d16; id=972032866; xnsid=3e7a788e; ver=7.0; loginfrom=null; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C2d04cc3ce01b4d4a5ce62827de6f3706%7C1566614851140%7C1%7C1566614851977'

    }
    request =urllib.request.Request(url=url,headers=headers)
    return request


def get_text(a_herf):
    request = handle_request(a_herf)
    content = urllib.request.urlopen(request).read().decode()

    pattern = re.compile(r'<div class="neirong">(.*?)</div>',re.S)
    lt = pattern.findall(content)

    text =lt[0]
    ###写正则，将内容里面的图片清空
    pat = re.compile(r'<img.*?>')
    pat.sub('',text)
    return text



def parse_content(content):
    pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)">(.*?)</a></h3>')
    lt = pattern.findall(content)
    ####返回的lt是一个列表，列表中的元素都是元组，元组的第一个元素就是正则中第一个小括号匹配到的内容，第二个元素就是第二个小括号匹配的内容
    for herf_title in lt:
        a_herf = 'http://www.yikexun.cn'+herf_title[0]

        title = herf_title[1]
        ##向a_herf发送请求，获取相应内容,所以继续创建get——text的函数
        text = get_text(a_herf)

        string = '<h1>%s</h1>%s'%(title,text)
        with open('lizhi.html','a')as fp:###用w写每次都会被清空
            fp.write(string)

    # print(lt)
    # print(len(lt))


def main():
    url ='http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))+1
    for page in range(start_page,end_page):
        request = handle_request(url,page)
        content = urllib.request.urlopen(request).read().decode()

        parse_content(content)

if __name__ =='__main__':
    main()

#####保存在html文件中，标题用h1,内容使用p即可
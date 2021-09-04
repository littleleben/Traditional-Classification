import urllib.request
import urllib.parse
import re
import os
import time


def handle_request(url,page):
    url = url +str(page)+'/'

    headers = {

        'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        'Cookie': 'anonymid=jzox8gtw-vad1pq; depovince=JS; _r01_=1; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C19e4492c1b8383305862c9d7d1b0b8c5%7C1566613839259%7C1%7C1566613840104; JSESSIONID=abcyAJ3o1SPqXcnA2FbZw; ick_login=59f79762-5591-484a-8b9a-289d8fc4db0c; wp_fold=0; ick=53af59fc-85e1-4508-a579-0caa1af04928; jebecookies=20459254-6fb8-4b69-a201-3209310cdb9c|||||; _de=11393ADFE3F26CC8D89AADF4B0420A80; p=6f2a1ad1ead406b7c63564d8eb74f2766; first_login_flag=1; ln_uact=15951840090; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=be1e1e563d48ebc02422b9e29ccd05d16; societyguester=be1e1e563d48ebc02422b9e29ccd05d16; id=972032866; xnsid=3e7a788e; ver=7.0; loginfrom=null; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C2d04cc3ce01b4d4a5ce62827de6f3706%7C1566614851140%7C1%7C1566614851977'

    }
    request = urllib.request.Request(url=url,headers=headers)
    return request


def download_image(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?</a>',re.S)###要的话用（.*?），不要的话直接.*？
    lt = pattern.findall(content)
    print(lt)
    ###遍历列表，依次下载图片
    for image_src in lt:
        ##先处理image_src
        image_src = 'http:'+image_src
        #发送请求下载图片
        ###创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = image_src.split('/')[-1]
        filepath = dirname +'/'+filename

        print('%s图片正在下载...'%filename)
        urllib.request.urlretrieve(image_src,filepath)
        print('%s图片结束下载...'%filename)
        time.sleep(1)

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page,end_page):
        print('第%s页正在下载...'%page)
        ###生成请求对象
        request = handle_request(url,page)
        ###发送请求对象，获取相应内容
        content = urllib.request.urlopen(request).read().decode()
        ###解析内容，提取所有的图片链接，下载图片
        download_image(content)
        print('第%s页结束下载...' %page)
        time.sleep(2)
if __name__ == '__main__':
    main()

{ 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh - CN, zh;q = 0.9',
    'Connection': 'keep - alive',
    'Content - Length': '91',

    'Cookie': 'BAIDUID = 0DF55D767635F1C3698B67A76891DC0F: FG = 1;BIDUPSID = 0DF55D767635F1C3698B67A76891DC0F;PSTM = 1565327023;BDUSS = lTbEM3a352RTBYcUh1djB2MFZQZC1hMGxIdkREUWhBSUtYSGlyOE1LVG9 - WGhkSVFBQUFBJCQAAAAAAAAAAAEAAAA30Po3zP3Ltcv7sK67qLuoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOhwUV3ocFFdZW;BDORZ = B490B5EBF6F3CD402E515D22BCDA1598;Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a = 1569292229, 1569500726, 1569500745, 1569554041;delPer = 0;PSINO = 1;H_PS_PSSID = 1434_21107_29523_29720_29568_29221_26350',
    'Host': 'baike.baidu.com',
    'Origin': 'https: // baike.baidu.com',
    'Referer': 'https: // baike.baidu.com / wikitag / taglist?tagId = 75953',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same - origin',
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X - Requested - With': 'XMLHttpRequest',}
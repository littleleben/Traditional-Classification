# cookie  服务器给客户留下一些身份信息
#
# 很多页面需要登录成功才能看的，所以需要模拟登录
####抓包获取cookie

import urllib.request
import urllib.parse

url = 'http://www.renren.com/972032747/profile'

headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
'Cookie': 'anonymid=jzox8gtw-vad1pq; depovince=JS; _r01_=1; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C19e4492c1b8383305862c9d7d1b0b8c5%7C1566613839259%7C1%7C1566613840104; JSESSIONID=abcyAJ3o1SPqXcnA2FbZw; ick_login=59f79762-5591-484a-8b9a-289d8fc4db0c; wp_fold=0; ick=53af59fc-85e1-4508-a579-0caa1af04928; jebecookies=20459254-6fb8-4b69-a201-3209310cdb9c|||||; _de=11393ADFE3F26CC8D89AADF4B0420A80; p=6f2a1ad1ead406b7c63564d8eb74f2766; first_login_flag=1; ln_uact=15951840090; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=be1e1e563d48ebc02422b9e29ccd05d16; societyguester=be1e1e563d48ebc02422b9e29ccd05d16; id=972032866; xnsid=3e7a788e; ver=7.0; loginfrom=null; jebe_key=73b46d5a-916b-4923-bc5f-aa2c4c9d29e0%7C2d04cc3ce01b4d4a5ce62827de6f3706%7C1566614851140%7C1%7C1566614851977'

}
####fiddler需要抓用户界面
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

with open('renren.html','wb')as fp:
    fp.write(response.read())


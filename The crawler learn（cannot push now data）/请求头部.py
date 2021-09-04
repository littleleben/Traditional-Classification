###构建头部请求   反爬虫的第一步！

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/' ###/这个斜线十分重要，必须要加

response = urllib.request.urlopen(url)

print(response.read().decode())

##伪装自己的UA，让服务端以为浏览器上网
#通过 urllib.request.Request() 类来创建请求对象！


headers = {
    'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}

###构建请求对象
request = urllib.request.Request(url=url,headers=headers)

###发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())

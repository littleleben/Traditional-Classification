# Handler处理器 自定义Opener
# urlopen()   给一定发送请求获取响应，不能定制请求头部
# 所以我们用Request()定制请求头来创建请求对象
#
# 高级功能：使用代理，cookie(浏览器保存状态的)
#
# ####基本用法：###########
import urllib.request
import urllib.parse

url = 'http://www.baidu.com'

headers = {

    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}

###创建一个Handler
handler = urllib.request.HTTPHandler()##普通请求，如果用cookie和代理会不一样
###通过handler创建一个opener
###Opner就是一个请求对象，不需要使用urlopen了

opener = urllib.request.build_opener(handler)

####构建请求对象
request = urllib.request.Request(url=url,headers=headers)

####发送请求
response = opener.open(request)
###不管用post还是get都是可以的
print(response.read().decode())


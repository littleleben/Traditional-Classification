####刷新界面的时候 ajax的接口

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

page = int(input('请输入想要第几页的数据：'))

number = 20

data ={
    'start':(page - 1)*number,
    'limit':number,

}
##将字典转换成querystring

query_string = urllib.parse.urlencode(data)
url = url+query_string

#构造请求对象
headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())

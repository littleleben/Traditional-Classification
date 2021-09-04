########笔记#######
# response这个对象的功能

# read()     读取相应的内容，内容是字节类型
# geturl()     获取请求的url
# getheaders()  获取头部信息  元组格式 可以dict转化
# getcode()     获取状态码
# readlines()     按行读取，返回列表，都是字节类型

########笔记#######

import urllib.request

url = 'http://www.baidu.com'
##完整的url  http://www.baidu.com/index.html?name=goudan&...

##发送请求
response = urllib.request.urlopen(url=url)


print(dict(response.getheaders()))
print(response.getcode())
print(response.readlines())




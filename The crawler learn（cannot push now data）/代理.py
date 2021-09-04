# 代理是什么？
#比如:微商,代练,代驾,代考,代购,


#程序中的代理]
# 正向的代理   我用代理器替我上网
#
# 反向的代理  服务器分包

# ////////
# 浏览器配置:
# 西刺代理
# 设置-----高级------代理-----局域网设置


# 代码配置:####################

import urllib.request
import urllib.parse
###普通的不能实现,所以要创建handler
handler = urllib.request.ProxyHandler({'http':''###ip地址
                                       })##注意不是HTTPhandler

opener = urllib.request.build_opener(handler)


url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}
request = urllib.request.Request(url=url,headers=headers)

response = opener.open(request)

with open('ip.html','wb') as fp:
    fp.write(response.read())


##创建一个handler，创建一个opener，后期使用opener.open去发送即可
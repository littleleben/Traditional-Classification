import urllib.request
import urllib.parse
import http.cookiejar###用来保存cookie的

######真实的模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
###创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
###通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
###通过handler创建opener
opener = urllib.request.build_opener(handler)


post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019761149190 '

formdata= {

    'email':'15951840090',
    'icode':'',
    'origURL':'http://www.renren.com/home',
    'domain':'renren.com',
    'key_id':'1',
    'captcha_type':'web_login',
    'password':'3d1abba6de06cd6c7e5d98ba2978672995114cd84cb542bbdd7e4fa4879a9278',
    'rkey':'8e6d0e7e8bd82b41b381ffa77d33fee9',
    'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dhpm6Vo2MfFq3TLnF2PzMKCGjc3xm-Gh1-me9H7KgM6wjote1Mv2fqwGpF3eE1_Nu%26wd%3D%26eqid%3D80de73cf0004247c000000045d60abff',
}
headers = {

    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}
request = urllib.request.Request(url=post_url,headers=headers)

formdata = urllib.parse.urlencode(formdata).encode()
response = opener.open(request,data=formdata)

print(response.read().decode)
print('*'*50)
#####以上已经登陆成功
# with open('rr.html','wb')as fp:
#     fp.write(response.read())

get_url = 'http://www.renren.com/972032866/profile'
request = urllib.request.Request(url=get_url,headers=headers)

response =opener.open(request)

print(response.read().decode)


###############方法
cj
handler
opener
先用opener储存一个cookie，然后再用这个opener去访问post网页


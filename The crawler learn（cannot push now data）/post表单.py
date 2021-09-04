import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/sug'

word = input('输入你要查找的单词：')

##构建post表单数据
form_data = {
    'kw':word,
}

headers = {
'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}

##构建请求对象
request = urllib.request.Request(url=post_url,headers=headers)
######对于post来说，需要处理下表单数据,不可忘了！
form_data = urllib.parse.urlencode(form_data).encode()

##发送请求
response = urllib.request.urlopen(request,data=form_data)##get的时候可以默认，但post的时候需要有data

print(response.read().decode())


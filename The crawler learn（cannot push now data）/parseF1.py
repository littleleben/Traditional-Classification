######笔记##########

# urllib.parse
# quote    编码，主要是中文空格类的，将中文变成%%%XXX....
# unquote   解码
# urlencode   给一个字典，将字典拼接为query_string
######笔记################笔记##########

import urllib.parse
url = 'http://www.baidu.com/index.html?name=哈哈哈￥pwd=123435'

#但是是无法上传的，因为有中文，所以此时需要编码，就需要用quote
print(urllib.parse.quote(url))
#可以去 url编码 网站进行解析，就能翻译回来了！

ret = urllib.parse.quote(url)
re = urllib.parse.unquote(ret)
print(re)###就解码了
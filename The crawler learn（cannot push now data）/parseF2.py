######笔记##########

# urllib.parse
# quote    编码，主要是中文空格类的，将中文变成%%%XXX....
# unquote   解码
# urlencode   给一个字典，将字典拼接为query_string
######笔记################笔记##########

import urllib.parse

url = 'http://www.baidu.com/index.html'

###假如参数有 name age sex height


name = 'hhh'
age = '18'
sex = 'nv'
height= '180'


data = {
    'name':name,
    'age':age,
    'sex':sex,
    'height':height,
    'weight':180,
}

###拼接方法一
# it= []
# for k,v in data.items():###字典内的项
#     it.append(k+'='+str(v))
# query_string = '&'.join(it)
# url = url + '?'+query_string


####拼接方法二！ 自带的拼装！并且可以自动把中文编码，也就是quote过了
query_string = urllib.parse.urlencode(data)
url = url + '?'+query_string
print(url)
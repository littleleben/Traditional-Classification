import urllib.request
import urllib.response

image_url = 'http://photocdn.sohu.com/20150724/mp24129102_1437711995584_2.gif'

response = urllib.request.urlopen(image_url)


####图片只能本地二进制形式

with open ('tu.gif','wb') as fp:
    fp.write(response.read())


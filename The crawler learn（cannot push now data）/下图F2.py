import urllib.request
import urllib.response

image_url = 'http://photocdn.sohu.com/20150724/mp24129102_1437711995584_2.gif'

response = urllib.request.urlopen(image_url)


urllib.request.urlretrieve(image_url,'tu2.gif')
####urlretrieve(image_url,image_path)后面这个默认是当前位置，可以自行写路径！

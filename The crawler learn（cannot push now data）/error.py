import urllib.request
import urllib.parse
import urllib.error

url = 'http://www.maodan.com/'

try:

    response = urllib.request.urlopen(url)
    print(response)
except Exception as e:###Exception任何异常都能捕获
    print(e)

except urllib.error.URLError as e:###精确捕获
    print(e)

####HTTPError是URLError的子类，所以写的时候可以

except urllib.error.HTTPError as e:
    print(e)

except urllib.error.URLError as e:
    print(e)
####两个同时捕获的时候，可以把HTTP写在上面，URL写在下面







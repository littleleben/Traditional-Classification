import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'


city = input('请输入要查询的城市：')
page = input('请输入要查询的页码：')
size = input('需要多少个数据：')
formdata = {

    'cname': city,
    'pid':'',
    'pageIndex': page,
    'pageSize': size,
}

headers = {

    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

}

request = urllib.request.Request(url=post_url,headers=headers)

formdata =urllib.parse.urlencode(formdata).encode()


response = urllib.request.urlopen(request,data=formdata)#####有表单的时候一定要写
####表单的时候一定要写啊！

print(response.read().decode())



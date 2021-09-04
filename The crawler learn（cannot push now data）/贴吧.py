import urllib.request
import urllib.parse
import os

url = 'http://tieba.baidu.com/f?&ie=utf-8&'


#1  pn 50
#2  pn 100
#n  pn (n-1)*50

##输入吧名，输入起始页码，输入结束页码，在当前文件夹中创建一个以吧名为名字
# 的文件夹，里面是每一页的html的内容

ba_name =input('请输入要爬取的吧名：')
start_page = int(input('请输入要爬取的起始页码：'))
end_page = int(input('请输入要爬取的结束页码:'))

###创建文件夹  os

if not os.path.exists(ba_name):
    os.mkdir(ba_name)


#####文件夹的创建！


###循环，依次循环爬取
for page in range(start_page,end_page+1):
    ##拼接url的过程
    data = {
        'kw':ba_name,
        'pn':(page-1)*50,

    }
    data = urllib.parse.urlencode(data)

    ##生成指定的url

    url_t =url+ data

    headers = {
        'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

    }
    request = urllib.request.Request(url=url_t,headers=headers)

    print('第%s页开始下载...'%page)

    response = urllib.request.urlopen(request)
    #生成文件名
    filename = ba_name +'_'+str(page)+'.txt'
    #拼接文件路径
    filepath = ba_name + '/'+filename

    with open(filepath,'wb') as fp:
        fp.write(response.read())

    print('第%s页结束下载...'%page)
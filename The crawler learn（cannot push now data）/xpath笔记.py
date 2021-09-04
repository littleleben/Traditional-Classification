
详细的内容主要见 url = 'https://www.w3school.com.cn/xpath/index.asp'
###常用的路径表达式
# //：不考虑位置的查找
# ./：从当前结点开始往下找
# @：选择属性


实例
/bookstore/book      选择根节点bookstore下面的所有book（仅限子类，孙类找不到）
//book               选取所有的book
bookstore//book      选择根节点bookstore下面的所有book
/bookstore/book[1]   选择根节点bookstore下面的第一个book元素  #注意不是[0],此处0就是代表第一个
/bookstore/book[position()<3]   选择根节点bookstore前两个元素
//title[@lang]       所有的带有lang属性的开头

属性定位
//input[@id="kw"]

层级定位
//div[@id="head"]/div/div[2]/a[1]#配了索引

索引定位
//div[@id="head"]/div/div[2]/a[1]#配了索引

逻辑运算
and =并且

模糊匹配
1.contains  如  //input[contains(@class,'s_i')]###指的是所有input 包含s_i的节点

2.starts_with    如//input[start_with(@class,'s_i')]###指的是所有input 必须以s_i开头的节点


取文本
//div[@id="u_sp"]/a[5]/text()


直接将所有的内容拼接起来的方法：###记住即可   其实用ret =tree.xpath('//div[@class="song"]//text()')双斜杠text就是可以用的
ret =tree.xpath('//div[@class="song"]')
string = ret[0].xpath('string(.)')
print(string.replace('\n','').replace('\t',''))

取属性
//div[@id="u_sp"]/a[5]/@href


使用xpath
from lxml import etree
将html文档变成一个对象，然后调用对象的方法去查找指定的节点

tree = etree.parse(文件名)##本地

tree = etree.HTML(网页字符串)##网页


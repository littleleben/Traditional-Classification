###获取属性
#soup.a.attrs 获取所有的属性和值，返回一个字典
#soup.a.attrs['href']  获取href属性
#soup.a['href']  简写


###获取内容
#soup.a.text
#soup.a.string  只能有文本，不可有标签，如果标签内有标签，则返回NONE
#soup.a.get_text()

###find
#soup.find.('a')  找到第一个符合要求的a
#soup.find.('a',title=...)  通过第二个来限制
#可以层层套着用
# 比如
# div = soup.find('div',class_='tang')
# print(div.find('a',class_ ='du'))

###find_all
# soup.find_all('a')    找出所有的a
# soup.find_all(['a','b'])   找出满足a或者b的
# soup.find_all('a',limit =2)   限制前两个

###select 返回的永远是列表，需要通过下标提取指定的对象，然后获取属性和节点
# 也可以让普通对象使用，如上列子
# 根据选择器选择指定的内容
# 常见的选择器：标签选择器、类选择器、id选择器、组合选择器、层级选择器、伪类选择器、属性选择器
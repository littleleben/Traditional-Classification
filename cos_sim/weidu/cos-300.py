# -*- coding: utf-8 -*-
import codecs
import numpy
import gensim
import numpy as np
from word2extract import *
import os
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import random
import re

wordvec_size=300
def get_char_pos(string,char):
    chPos=[]
    try:
        chPos=list(((pos) for pos,val in enumerate(string) if(val == char)))
    except:
        pass
    return chPos

def word2vec(file_name,model):
    with codecs.open(file_name, 'r') as f:
        try:
            word_vec_all = numpy.zeros(wordvec_size)
            for data in f:
                space_pos = get_char_pos(data, ' ')
                first_word=data[0:space_pos[0]]
                if model.__contains__(first_word):
                    word_vec_all= word_vec_all+model[first_word]

                for i in range(len(space_pos) - 1):
                    word = data[space_pos[i]:space_pos[i + 1]]
                    if model.__contains__(word):
                        word_vec_all = word_vec_all+model[word]
            return word_vec_all
        except:
            return []


def simlarityCalu(vector1,vector2):
    try:
        vector1Mod=np.sqrt(vector1.dot(vector1))
        vector2Mod=np.sqrt(vector2.dot(vector2))
        if vector2Mod!=0 and vector1Mod!=0:
            simlarity=(vector1.dot(vector2))/(vector1Mod*vector2Mod)####修改过了，注意一下！！！！
            if simlarity==0.9999999999999999or simlarity==1.0000000000000002or simlarity==1.0:
                simlarity=(vector1.dot(vector2))/(vector1Mod*vector2Mod)-0.01*vector1Mod
        else:
            simlarity=0
        return simlarity
    except:
        return 0



def url_open(url_random):
    url_random_new='https://'+url_random
    # print(url_random_new)
    headers = {

        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    }
    request = urllib.request.Request(url=url_random_new, headers=headers)
    response_stop = urllib.request.urlopen(request)
    content = response_stop.read().decode('gbk')
    soup = BeautifulSoup(content, 'lxml')
    title_url = soup.findAll('div', class_="pb20 article_detail")
    for i in title_url:
        i_txt=i.get_text()
        # print(i_txt)
        compare_list.append(i_txt)
    # compare_list_str=str(compare_list)
    # return compare_list_str
    # print(title_url.get_text())



# def find_chinese(file):
#     pattern = re.compile(r'[^\u4e00-\u9fa5]')
#     chinese = re.sub(pattern, '', file)
#     return chinese




def hdf_urlsearch(jbms):
    query_jbms = urllib.parse.quote(jbms)
    # print(query_jbms)
    url_jb = 'https://so.haodf.com/index/search?kw=' + query_jbms

    headers = {

        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    }
    request = urllib.request.Request(url=url_jb, headers=headers)
    response_stop = urllib.request.urlopen(request)
    content = response_stop.read().decode()
    soup=BeautifulSoup(content,'lxml')
    title_url=soup.findAll('a',class_="sc-wz-title-a a-title")
    re_url=re.compile(' href="//(.*?)"',re.S)
    title_url_re=re_url.findall(str(title_url))
    random_url=random.sample(title_url_re,2)####随机选择两个网址
    for i in title_url_re:
        # print(i)
        url_open(i)


    # print(soup)



def list_deal(list_str):
    remove_1_i_txt=list_str.replace(' ','')###去掉所有的空格
    # print(remove_blank_i_txt)
    remove_2_i_txt = str(remove_1_i_txt).replace('\n', '')  ###去掉所有的空格
    remove_3_i_txt = str(remove_2_i_txt).replace('\xa0', '')
    return remove_3_i_txt


path_jib = "/疾病gather/万方加百度筛选后的疾病/"
files= os.listdir(path_jib)


if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('/gensim-linuxs/data/word词去停用词/jb_use_300.word2vec')

    p1_keywords = '/gensim-linuxs/data/P11_keywords.txt'
    p2_keywords = '/gensim-linuxs/data/P12_keywords.txt'
    p1_keywords_new='/gensim-linuxs/data/P11_keywords_new.txt'

    jbms=input('请输入要查找的疾病名称：')
    JBMS=jbms.split(' ')


    # getKeywords(p2, p2_keywords)
    # p1_vec=word2vec(p1_keywords,model)
    # p2_vec=word2vec(p2_keywords,model)
    for jb in JBMS:
        try:
            compare_list = []
            print('                     ')
            # hdf_urlsearch(jb)￥￥￥￥￥￥不需要下载时注释
            # compare_list_str = str(compare_list)￥￥￥￥￥￥不需要下载时注释

            pvec_list=[]
            p1 = '/疾病gather/好大夫搜索测试BM25-L/'+jb+'.txt'
            # for i in compare_list:￥￥￥￥￥￥不需要下载时注释
            #     # print(i)￥￥￥￥￥￥不需要下载时注释
            #     with open(p1,'a',encoding='utf-8')as fi:￥￥￥￥￥￥不需要下载时注释
            #         fi.write(i)￥￥￥￥￥￥不需要下载时注释
            #         fi.close()￥￥￥￥￥￥不需要下载时注释


            compare = {}
            getKeywords(p1, p1_keywords)
            with open(p1_keywords, 'r',encoding='utf-8')as fi:
                key_word=fi.readlines()
                for j in key_word:
                    p1_keywords_newkey=j.replace('\\n','')
                    pvec_list.append(j)
            with open(p1_keywords_new,'w',encoding='utf-8')as fp:
                pvec_list_str=str(pvec_list).replace('\\n','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('    ','').replace('   ','').replace('  ','').replace(' ','',1)

                fp.write(pvec_list_str)

            p1_vec = word2vec(p1_keywords_new, model)
            # print(p1_vec)
            for file in files:  # 遍历文件夹
                f = os.path.basename(file)
                name_s = f.replace('.txt', '')

                # print(name)
                p2 = path_jib + '/' + f
                # p2 = './data/糖尿病.txt'
                getKeywords(p2, p2_keywords)

                p2_vec = word2vec(p2_keywords, model)
                # print(p2_vec)
                sim = simlarityCalu(p1_vec, p2_vec)
                sim_4 = round(sim, 4)
                compare[name_s] = sim_4


            n = 10
        ########################################################################
            L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
            L = L[:n]
            print(jb)
            print(L)
            # print(simlarityCalu(p1_vec,p2_vec))
        except:
            print(jb)
            print('报错报错报错**********')
            continue
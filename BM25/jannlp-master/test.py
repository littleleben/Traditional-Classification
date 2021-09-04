import jieba
from similarity.bm25 import BM25
from summary.textrank import TextRank
from utils import utils
from snownlp import seg
import os
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from word2extract import *
import random
import re

path_jib = "E:\\疾病gather\\万方加百度筛选后的疾病"
files= os.listdir(path_jib)


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
    # random_url=random.sample(title_url_re,2)####随机选择两个网址
    for i in title_url_re:
        # print(i)
        url_open(i)


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

# text = '''
# 自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
# 它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
# 自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
# 因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
# 所以它与语言学的研究有着密切的联系，但又有重要的区别。
# 自然语言处理并不是一般地研究自然语言，
# 而在于研制能有效地实现自然语言通信的计算机系统，
# 特别是其中的软件系统。因而它是计算机科学的一部分。
# '''




if __name__ == '__main__':
    jbms = input('请输入要查找的疾病名称：')
    JBMS = jbms.split(' ')
    p1_keywords = 'E:\\BM25\\data\\P11_keywords.txt'
    p1_keywords_new='E:\\BM25\\data\\P11_keywords_new.txt'


    for jb in JBMS:
        compare = {}
        compare_list = []
        print('                     ')
        hdf_urlsearch(jb)
        compare_list_str = str(compare_list)

        pvec_list = []
        p1 = 'E:\\疾病gather\\好大夫搜索测试BM25\\' + jb + '.txt'
        for i in compare_list:
            # print(i)
            with open(p1, 'a', encoding='utf-8')as fi:
                fi.write(i)
                fi.close()

        getKeywords(p1, p1_keywords)

        # jishu = 0

        with open(p1_keywords, 'r')as fi:
            key_word = fi.readlines()
            for j in key_word:
                p1_keywords_newkey = j.replace('\\n', '')
                pvec_list.append(j)

        with open(p1_keywords_new, 'w')as fp:
            pvec_list_str = str(pvec_list).replace('\\n', '').replace("'", '').replace(',', '').replace('[','').replace(']','').replace('    ', '').replace('   ', '').replace('  ', '').replace(' ', '', 1)
            fp.write(pvec_list_str)
            fp.close()

        with open(p1_keywords_new, 'r')as fr:
            sim_list = fr.read()

        for file in files:
            # jishu=jishu+1
            #############################################################
            f = os.path.basename(file)
            name_s = f.replace('.txt', '')

            p2 = path_jib + '\\' + f
            with open(p2,'r',encoding='utf-8')as fp:
                text=fp.read()
                fp.close()

            sents = utils.get_sentences(text)
            doc = []

            for sent in sents:
                words = seg.seg(sent)
                # words = list(jieba.cut(sent))
                words = utils.filter_stop(words)
                doc.append(words)
            # print(doc)
        # s = BM25(doc)
        # print(s.f)
        # print(s.df)
        # print(s.idf)
            s = BM25(doc)
            sim_num = (s.simall(sim_list))
            k=0
            m=0
            for num_i in sim_num:###求和
                k=k+num_i
                m=m+1
                    # print(k)
                    # print(m)
            sim_numall=k/m

            # print(jishu)
            #
            # print(sim_numall)
            # print(name_s)

            compare[name_s]=sim_numall


        n = 10
        L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
        L = L[:n]
        print(jb)
        print(L)




    # rank = TextRank(doc)
    # rank.text_rank()
    # for index in rank.top_index(3):
    #     print(sents[index])

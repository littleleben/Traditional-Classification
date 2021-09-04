# -*- coding: utf-8 -*-
import codecs
import numpy
import gensim
import numpy as np
from word2extract import *
import os

wordvec_size=192
def get_char_pos(string,char):
    chPos=[]
    try:
        chPos=list(((pos) for pos,val in enumerate(string) if(val == char)))
    except:
        pass
    return chPos

def word2vec(file_name,model):
    with codecs.open(file_name, 'r',encoding='utf-8') as f:
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

def simlarityCalu(vector1,vector2):
    vector1Mod=np.sqrt(vector1.dot(vector1))
    vector2Mod=np.sqrt(vector2.dot(vector2))
    if vector2Mod!=0 and vector1Mod!=0:
        simlarity=(vector1.dot(vector2))/(vector1Mod*vector2Mod)####修改过了，注意一下！！！！
    else:
        simlarity=0
    return simlarity

def stopword(word,keywords):
    with open(word, 'r', encoding='utf-8')as fi:
        text=fi.read()
        # print(text)
    # getKeywords(p1, p1_keywords)
    #     print(text)
        stop_save=[]
        for i in text:
            stop_save.append(i)
        stop_save_str=str(stop_save)
        stop_save_use1=stop_save_str.replace(',','')
        stop_save_use2 = stop_save_use1.replace("'", '')
        with open(keywords, 'w', encoding='utf-8')as fi:
            fi.write(stop_save_use2)
            fi.close()


path_jib = "E:\\疾病gather\\疾病清洗"
files= os.listdir(path_jib)

if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('jb_all_word.word2vec')

    p1_keywords = './data/P11_keywords.txt'


    # getKeywords(p2, p2_keywords)
    # p1_vec=word2vec(p1_keywords,model)
    # p2_vec=word2vec(p2_keywords,model)
    jbms =str(input('请输入您目前的病症或疾病描述：'))
    print('正在疾病库中查找，请稍后...')
    compare = {}
    p1 = 'C:\\Users\\雷神\\Desktop\\Pinput.txt'
    with open(p1,'w',encoding='utf-8')as fp:
        fp.write(jbms)
        fp.close()
    stopword(p1,p1_keywords)


    k=1
    for file in files:  # 遍历文件夹
        k=k+1
        if k%1000==1:
            print('please wait a moment')
        p2_keywords = './data/P12_keywords.txt'
        f = os.path.basename(file)
        name_s = f.replace('.txt', '')
        # print(name)
        p2 = path_jib + '\\' + f
        stopword(p2,p2_keywords)
        # p2 = './data/糖尿病.txt'
        # getKeywords(p2, p2_keywords)
        # with open(p2, 'w', encoding='utf-8')as fi:
        #     fi.write(jbms)
        #     fi.close()


        sim=model.n_similarity(p1_keywords,p2_keywords)
        p1_vec = word2vec(p1_keywords, model)
        print(p1_vec)
        p2_vec = word2vec(p2_keywords, model)
        print(p2_vec)
        # sim = simlarityCalu(p1_vec, p2_vec)
        # compare[name_s] = sim
        # y=model.most_similar('疼',topn=5)
        # print(y)
    n = 5
########################################################################
    L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
    L = L[:n]
    print(L)
    # print(simlarityCalu(p1_vec,p2_vec))

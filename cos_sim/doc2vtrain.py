# coding:utf-8
import sys
import gensim
import sklearn
import numpy as np
import codecs
import os
import gensim.models as g

from gensim.models.doc2vec import Doc2Vec, LabeledSentence

TaggededDocument = gensim.models.doc2vec.TaggedDocument

def train(x_train, vector_size=200, epoch_num=1):
    model_dm = Doc2Vec(x_train, min_count=1, window=3, vector_size=vector_size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=70)
    model_dm.save('E:\\gensim\\data\\doc的训练向量-800M\\doc_jb')

path_jib = "E:\\训练向量的文本-800M\\qy-1"
files= os.listdir(path_jib)
x_train = []
def get_datasest():
    # x_train = []
    k =1
    for file in files:  # 遍历文件夹
        print('第'+str(k)+'篇读取完成')
        k=k+1
        f = os.path.basename(file)
        name_s = f.replace('.txt', '')
        # print(name)
        paths = path_jib + '\\'+f

        with open(paths, 'r',encoding='utf-8') as cf:
            docs = cf.readlines()
            print(len(docs))
        # y = np.concatenate(np.ones(len(docs)))
            for i, text in enumerate(docs):
                word_list = text.split(' ')
                l = len(word_list)
                word_list[l - 1] = word_list[l - 1].strip()
                document = TaggededDocument(word_list, tags=[i])
                x_train.append(document)
        # print(x_train)
    return x_train

if __name__ == '__main__':
    x_train = get_datasest()
    print(x_train)
    model_dm = train(x_train)

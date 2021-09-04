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


# def get_datasest():
#     with open("C:\\Users\\雷神\\Desktop\\luntan.txt", 'r',encoding='utf-8') as cf:
#         docs = cf.readlines()
#         print(len(docs))
#
#     x_train = []
#     # y = np.concatenate(np.ones(len(docs)))
#     for i, text in enumerate(docs):
#         word_list = text.split(' ')
#         l = len(word_list)
#         word_list[l - 1] = word_list[l - 1].strip()
#         document = TaggededDocument(word_list, tags=[i])
#         x_train.append(document)
#
#     return x_train


def getVecs(model, corpus, vector_size):
    vecs = [np.array(model.docvecs[z.tags[0]].reshape(1, vector_size)) for z in corpus]
    return np.concatenate(vecs)



#
start_alpha = 0.01
infer_epoch = 1000
docvec_size = 192



def doc2vec(file_name, model):
    import jieba
    doc = [w for x in codecs.open(file_name, 'r', 'utf-8').readlines() for w in jieba.cut(x.strip())]
    doc_vec_all = model.infer_vector(doc, alpha=start_alpha, steps=infer_epoch)
    return doc_vec_all



def simlarityCalu(vector1, vector2):
    vector1Mod = np.sqrt(vector1.dot(vector1))
    vector2Mod = np.sqrt(vector2.dot(vector2))
    if vector2Mod != 0 and vector1Mod != 0:
        simlarity = (vector1.dot(vector2)) / (vector1Mod * vector2Mod)
    else:
        simlarity = 0
    return simlarity


path_jib = "E:\\疾病gather\\百度万方疾病"
files= os.listdir(path_jib)
if __name__ == '__main__':
    # x_train = get_datasest()
    # model_dm = train(x_train)
    model = g.Doc2Vec.load("E:\\gensim\\data\\doc的训练向量-200M\\doc_all_jb")
    jbms =str(input('请输入您目前的病症或疾病描述：'))
    print('正在疾病库中查找，请稍后...')
    p1 = 'C:\\Users\\雷神\\Desktop\\Pdoc.txt'
    with open(p1,'w',encoding='utf-8')as fi:
        fi.write(jbms)
        fi.close()
    # p1 = 'C:\\Users\\雷神\\Desktop\\Pdoc.txt'
    compare={}
    for file in files:  # 遍历文件夹
        f = os.path.basename(file)
        name_s = f.replace('.txt', '')

        # print(name)
        p2 = path_jib + '\\' + f
        # p2 = './data/糖尿病.txt'
        P1_doc2vec = doc2vec(p1, model)
        P2_doc2vec = doc2vec(p2, model)
        sim = simlarityCalu(P1_doc2vec, P2_doc2vec)
        sim_4=round(sim,4)
        compare[name_s] = sim_4
    n = 5

    L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
    L = L[:n]
    print(L)
    # dictdata = {}
    # for l in L:
    #     dictdata[l[0]] = l[1]
    # print(dictdata)

    # sims = test()
    # for count, sim in sims:
    #     sentence = x_train[count]
    #     words = ''
    #     for word in sentence[0]:
    #         words = words + word + ' '
    #     print(words, sim, len(sentence[0]))
import os
from word2extract import *
# import Levenshtein
import distance

path_jib = "E:\\疾病gather\\万方加百度筛选后的疾病"
files= os.listdir(path_jib)

# def edit_distance(s1, s2):
#     return distance.levenshtein(s1, s2)


def similarity(s1, s2):
    m = max(len(s1), len(s2))
    d = distance.levenshtein(s1,s2)
    # print(d)
    return (m - d) / m


if __name__ == '__main__':
    jbms = input('请输入要查找的疾病名称：')
    JBMS = jbms.split(' ')
    p1_keywords = 'E:\\编辑距离\\data\\P11_keywords.txt'
    p2_keywords = 'E:\\编辑距离\\data\\P12_keywords.txt'
    p1_keywords_new='E:\\编辑距离\\data\\P11_keywords_new.txt'


    for jb in JBMS:
        compare = {}
        compare_list = []
        print('                     ')

        compare_list_str = str(compare_list)

        pvec_list = []
        p1 = 'E:\\疾病gather\\好大夫搜索测试编辑距离\\' + jb + '.txt'

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
            target_list = fr.read()
            target_str=str(target_list).replace(' ','')

        for file in files:
            # jishu=jishu+1
            #############################################################
            f = os.path.basename(file)
            name_s = f.replace('.txt', '')

            p2 = path_jib + '\\' + f
            getKeywords(p2, p2_keywords)

            with open(p2_keywords,'r')as fp:
                jbku_list=fp.read()
                jbku_str=str(jbku_list).replace(' ','')
                fp.close()

            edit_distance_sim=similarity(target_str,jbku_str)
            # print(edit_distance_sim)
            # print(name_s)


            # print(doc)
        # s = BM25(doc)
        # print(s.f)
        # print(s.df)
        # print(s.idf)



            # print(jishu)
            #
            # print(sim_numall)
            # print(name_s)

            compare[name_s]=edit_distance_sim


        n = 10
        L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
        L = L[:n]
        print(jb)
        print(L)



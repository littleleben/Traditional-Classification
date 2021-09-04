# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    news = open('/gensim-linuxs/data/word+character_wash done.txt', 'r',encoding='utf-8')
    model = Word2Vec(LineSentence(news), sg=1,size=100, window=10, min_count=5, workers=10)
    model.save('/gensim-linuxs/data/word词去停用词/jb_use_100.word2vec')

if __name__ == '__main__':
    my_function()

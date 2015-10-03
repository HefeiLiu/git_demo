#coding:utf-8
'''
Created on 2015-9-23
测试所有文档的wordde
@author: Liu
'''

import gensim,logging
from gensim import corpora
import codecs
import jieba
#from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec

def getStopWords():
    ''' 获取停用词表   '''
    fileName ='G:\\SetExpansion\\stopwords.txt'
    stopWordsList = []
    #fin = codecs.open(fileName,"r","gb2312")
    fin = open(fileName,"r")
    for stopword in fin:
        stopword = stopword.decode("gb2312","ignore")
        stopWordsList.append(stopword.strip())
    fin.close()
    return stopWordsList
def writeSegwordsToFile(allSegwordsList,writeToFilePath):
    with codecs.open(writeToFilePath,"w","utf-8") as fout:
        for lineWord in allSegwordsList:
            for word in lineWord:
                fout.write(word+" ")
            fout.write("\n")
    print "写入文件完成"

def getcorpus(path):
    '''  获取所有的corpus，进行分词，去除停用词，得到所有文档的分词列表allSegwordsList ，为进行lda的运算提前做好准备'''
    #得到停用词
    stopWordsList = getStopWords()
    fin = codecs.open(path,"r","utf-8")
    #docList =[doc.strip() for doc in fin ]
    allSegwordsList = []
    i=1
    for doc in fin:
        print i
        i += 1
        segwordsForDoc = jieba.cut(doc.strip())
        singleDocSegwords = []
        for word in segwordsForDoc:
            if word not in stopWordsList:
                singleDocSegwords.append(word)
        allSegwordsList.append(singleDocSegwords)
    fin.close()
    print "分词完成"
    return allSegwordsList

def testWord2vec(allSegwordsList):
    #sentences =[["first","sentence"],["second","sentence"]]
    print "训练word2vec中………………"
    sentences = word2vec.Text8Corpus("G:\\SetExpansion\\SegWordsResult.txt")
    model = gensim.models.Word2Vec(sentences,size =100)
    '''
    model = gensim.models.Word2Vec()
    print model
    model.build_vocab(sentences)
    print 
    model.train(sentences)
    '''
    print "训练word2vec完成"
    print  '保存model中…………'
    model.save("G:\\SetExpansion\\word2vecModel.model")
    print  '保存model完成'
    print model
    print model.similarity(u"北京",u"上海")
    print 
    
    
    

if __name__ == '__main__':
    corpusPath = "G:\\SetExpansion\\corpus1.txt"
    writeToFilePath = "G:\\SetExpansion\\SegWordsResult.txt"
    #allSegwordsList = getcorpus(corpusPath)
    #writeSegwordsToFile(allSegwordsList,writeToFilePath)
    
    #logging.basicConfig(format="%(asctime)s:%(levelname)s : %(message)s", level = logging.INFO)
    
    testWord2vec(None)
    #model = word2vec.Word2Vec.load("G:\\SetExpansion\\word2vecModel.model")
    #print model.doesnt_match([u"北京日报",u"人民日报",u"中广网",u"汉网"])
    '''
    使用心得：
        在使用word2vec时，必须使用unicode编码的字符串，使用步骤：
        1、首先对要分析的预料文本进行分词，去除停用词，然后存放到文档A（以utf-8编码）中，以空格分开，每个文档占用一行
        2、使用word2vec.Text8Corpus去去读文件获取预料保存到sentences中，利用word2vec.Word2Vec去训练语料，就可以求出
    '''
    
    
    
    
#coding=utf-8  
import jieba  
import sys 
sys.path.append("../") 
jieba.load_userdict("/home/alber/jieba/user_dict.txt")　　　　　#用户词表位置
import jieba.posseg as pseg 
import time  
t1=time.time() 

stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt') ])    #听用词表位置
f1=open("/home/alber/llq.txt","r") #读取文本  
txtlist=f1.readlines()
f1.close()
f2=open("/home/alber/llq_seg.txt",'a')
for line in txtlist:
	line_cut=list(pseg.cut(line))
	for w in line_cut:
		if w.word not in stopwords:
			f2.write(w.word+" ")
		else:
			pass
t2=time.time() 
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果
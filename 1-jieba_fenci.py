#coding=utf-8  
import jieba  
import sys 
sys.path.append("../") 
jieba.load_userdict("/home/alber/jieba/user_dict.txt")
import jieba.posseg as pseg 
import time  
t1=time.time() 

stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt') ])
f=open("/home/alber/data_base/jd_content/app-mac/app-mac.txt","r") #读取文本  
txtlist=f.read().decode('utf-8')
words=jieba.cut(txtlist)  
	for w in words: 
		seg=str(w.word.encode('utf-8'))
		if seg not in stopwords:
			result+=str(seg)+" "#+"/"+str(w.flag)+" " #去停用词  
			f=open("/home/alber/data_base/jd_content/app-mac/mac-result-nostopword.txt","a")  #将结果保存到另一个文档中  
			f.write(result)
	
f.close()  
t2=time.time() 
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果
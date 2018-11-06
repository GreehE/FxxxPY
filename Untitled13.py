#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# In[1]:


from snownlp import sentiment


# In[ ]:


import pandas as pd 
text=pd.read_excel(u'D:/PYFxxx/评论文本.xlsx',header=0) #读取文本数据
text0=text.iloc[:,0] #提取所有数据
text1=[i.decode('utf-8') for i in text0] #上一步提取数据不是字符而是object，所以在这一步进行转码为字符


# In[ ]:


sentiment.train('D:/1.txt') 


# In[ ]:


sentiment.save('D:/pyscript/sentiment.marshal')


# In[ ]:


from snownlp import SnowNLP


# In[ ]:


senti=[SnowNLP(i).sentiments for i in text1] 


# In[ ]:


newsenti=[]
for i in senti:
  if (i>=0.6):
      newsenti.append(1)
  else:
      newsenti.append(-1)
text['predict']=newsenti  


# In[ ]:


counts=0
for j in range(len(text.iloc[:,0])):
    if text.iloc[j,2]==text.iloc[j,1]:
        counts+=1
print u"准确率为:%f"%(float(counts)/float(len(text)))


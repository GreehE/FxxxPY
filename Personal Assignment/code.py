#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver


# In[ ]:


import requests


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import os


# In[44]:


import time


# In[6]:


from os import listdir


# In[21]:


if __name__ == "__main__":
    if  os.path.exists("D:\\catalog\\heyanglin"):
        print("文件夹已存在")
    else :
        os.mkdir("D:\\catalog\\heyanglin")


# In[52]:


browser=webdriver.Chrome()
browser.get('https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&ch=1&tn=78040160_26_pg&wd=%E4%BD%95%E6%9D%A8%E6%9E%97&oq=%25E4%25BD%2595%25E6%259D%25A8%25E6%259E%2597&rsv_pq=b3cb635700029f85&rsv_t=20d3u1nVpZFs1rIumYX8f8UBI%2BBGyfvM06AkW10O1A6y5rJFozP6oqyeRTjZWw6YgFRXocQ&rqlang=cn&rsv_enter=0&prefixsug=%25E4%25BD%2595%25E6%259D%25A8%25E6%259E%2597&rsp=0&rsv_sug=1')


# In[55]:


r=requests.get('https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&ch=1&tn=78040160_26_pg&wd=%E4%BD%95%E6%9D%A8%E6%9E%97&oq=%25E4%25BD%2595%25E6%259D%25A8%25E6%259E%2597&rsv_pq=b3cb635700029f85&rsv_t=20d3u1nVpZFs1rIumYX8f8UBI%2BBGyfvM06AkW10O1A6y5rJFozP6oqyeRTjZWw6YgFRXocQ&rqlang=cn&rsv_enter=0&prefixsug=%25E4%25BD%2595%25E6%259D%25A8%25E6%259E%2597&rsp=0&rsv_sug=1')


# In[62]:


r.status_code


# In[75]:


html = r.content
doc = pq(html)
doc1=doc('t')


# In[88]:


soup=BeautifulSoup(doc,"html.parser")
elems=soup.find('div',class_="result c-container").a.get_text()
for elem in elems:
    title =elem.text#获取每个搜索结果标题


# In[85]:


for elem in doc1('a'):
        url=elem.get('href')#每个搜索结果的链接
        reps=request.get(url)
        soup1=BeautifulSoup(reps.content)
        content=soup.find("div",class_="text well").font.get_text() #每个链接点击进去的内容
   


# In[86]:


with open('D:\\catalog\\heyanglin/'+title+'.txt',"a",encoding='utf-8') as f:
    f.write(content+'\n')


# In[90]:


#分词
labels=[] #搜索结果集合
results=[] 
all_files=listdir('D:/catalog/heyanglin')

 for i in range(0,len(all_files)):
        filename=all_files[i]
        filelabel=filename.split('.')[0]
        labels.append(filelabel)
        file_add='D:/Parse/lixiang/'+ filename
        print(file_add)


# In[ ]:


doc=open(file_add,encoding='utf-8').read()
        data=jieba.cut(doc,cut_all=True) 
        data_adj=''
        delete_word=[]
        results.append(data_adj)


# In[ ]:


#对文本内容进行分类


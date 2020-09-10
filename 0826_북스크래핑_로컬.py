#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from urllib.request import urlopen
import os

java_url='https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%25EC%259E%2590%25EB%25B0%2594&orderClick=LAG'
django_url='https://search.kyobobook.co.kr/web/search?vPstrKeyWord=django&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&currentPage=1&orderClick=LIZ'
cloud_url='https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%25ED%2581%25B4%25EB%259D%25BC%25EC%259A%25B0%25EB%2593%259C&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&currentPage=1&orderClick=LIZ'
react_url='https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%25EB%25A6%25AC%25EC%2595%25A1%25ED%258A%25B8&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&currentPage=1&orderClick=LIZ'
mysql_url='https://search.kyobobook.co.kr/web/search?vPstrKeyWord=mysql&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&currentPage=1&orderClick=LIZ'
url_dict={'java':java_url,'django':django_url,'cloud':cloud_url,'react':react_url,'mysql':mysql_url}

final_list=[]
for book_key,url in url_dict.items():
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html,'html.parser')
    
    n=1
    books=soup.select("#search_list tr ")[:1]
    # for i in soup.select('#search_list tr td.image div.cover a img'):
    #     print(i['src'])
    #
    #     img_url=i['src']
    #     with urlopen(img_url) as f:
    #         with open('C:/LECTURE_REVIEW/lecture/static/lecture/img/'+book_key+str(n)+'.jpg','wb') as h:
    #             ima=f.read()
    #             h.write(ima)
    #     n+=1
    #     if n>10:
    #         break
    
    
    for i in books:
        book_dic={}
        title=(i.select('td.detail div.title strong')[0].text)
        author=(i.select('td.detail div.author a')[0].text)
        price=(i.select('td.price div.sell_price strong')[0].text)
        like=(i.select('td.info div.review.klover a b')[0].text)
        lin=i.select('td.detail div.title a')[0]
        kind=book_key
        book_dic['book_title']=title
        book_dic['book_author']=author
        book_dic['book_price']=price
        book_dic['book_like']=like
        book_dic['book_kind']=kind
        book_dic['book_link']=lin['href']
        final_list.append(book_dic)
        print(title)
        
book_list=pd.DataFrame(columns=['book_title','book_author','book_price','book_like','book_link'])    
for i in final_list:
    tmp=pd.Series(i)
    book_list=book_list.append(tmp,ignore_index=True)

book_list


# In[8]:


import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:"+"root"+"@localhost/django_db",encoding="utf-8")
conn = engine.connect()

book_list.to_sql(name='lecture_book', con=engine, if_exists='replace', index=True,               index_label='id')


# In[6]:





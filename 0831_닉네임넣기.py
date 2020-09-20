#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from urllib.request import urlopen
import os



temp_list=[
    '공항도둑',
    '해장국집 우산도둑',
    '멀티캠퍼스 하리보 도둑',
    '이민용의 피자빵 담당',
    '메이플스토리 유명인사',
    '학창시절 비의도적 골키퍼 담당',
    '저기 니남친 지나간다의 남친',
    '싸이월드 최대 투데이 3',
    '욕쟁이할머니 담배셔틀',
    '인스타 좋아요 최대 2',
    '편의점 면접 정장입고 탈락',
    '김치부침개 오징어 도둑',
    '경비실 누룽지사탕 서리꾼',
    '인생 최대 일탈 눈썹문신',
    '코로나 마스크 착용 수혜자',
    '인생 최대 업적 롤 골드티어',
    '칼국수집 녹말이쑤시개 도둑'
 
    
    
]

final_list=[]

for i in temp_list:
    dic={}
    i=i.replace(' ','_')
    dic['nick_nickname']=i
    final_list.append(dic)

   

        
nick_list=pd.DataFrame(columns=['nick_nickname'])    
for i in final_list:
    tmp=pd.Series(i)
    nick_list=nick_list.append(tmp,ignore_index=True)

final_list

print(final_list)
# In[17]:


import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:"+"root"+"@localhost/django_db",encoding="utf-8")
conn = engine.connect()

nick_list.to_sql(name='chat_nick', con=engine, if_exists='append', index=True,               index_label='id')


# In[8]:


import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:"+"root"+"@localhost/django_db?charset=utf8",encoding="utf-8")
conn = engine.connect()

nick_list.to_sql(name='chat_nick', con=engine, if_exists='append', index=True,               index_label='id')


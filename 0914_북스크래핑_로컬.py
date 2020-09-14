from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from urllib.request import urlopen
import os

url_head = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
url_tail = "&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&currentPage=1&orderClick=LIZ"
# 제목 #search_list > tr:nth-child(6) > td.detail > div.title > a > strong
# 가격 #search_list > tr:nth-child(6) > td.price > div.sell_price > strong
#       search_list > tr:nth-child(6) > td.price > div.sell_price > strong
# 저자 #search_list > tr:nth-child(6) > td.detail > div.author > a:nth-child(1)
# 이미지 #search_list > tr:nth-child(6) > td.image > div.cover > a > img

url_dict = {}
u_list = ['html', 'django', 'machine+learning', 'java+spring', 'docker+kubernetes']

for i in u_list:
    url_dict[i] = url_head + i + url_tail
final_list = []
for book_key, url in url_dict.items():
    book_key = book_key.replace('+', ' ')
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select("#search_list tr ")

    n = 1
    # for i in soup.select('#search_list tr td.image div.cover a img'):
    #     print(i['src'])
    #
    #     img_url = i['src']
    #     with urlopen(img_url) as f:
    #         with open('C:/jupyter/img/' + book_key + str(n) + '.jpg', 'wb') as h:
    #             ima = f.read()
    #             h.write(ima)
    #     n += 1
    #     if n > 10:
    #         break

    cnt = 1
    for book in books:
        book_dic = {}
        book_key = book_key.replace('+', ' ')
        title = book.select('td.detail div.title a strong')[0].text
        author = book.select('td.detail div.author a')[0].text
        lin = book.select('td.detail div.title a')[0]['href']
        price = book.select('td.price div.sell_price strong')
        if not book.select('td.info div.review.klover a b'):
            like = 0
        else:
            like = book.select('td.info div.review.klover a b')[0].text

        if len(price) != 0:
            price = price[0].text
        else:
            price = 0

        kind = book_key.replace(' ','_')
        book_dic['book_title'] = title
        book_dic['book_author'] = author
        book_dic['book_price'] = price
        book_dic['book_like'] = like
        book_dic['book_kind'] = kind
        book_dic['book_link'] = lin
        final_list.append(book_dic)
        print(title)
        cnt += 1
        if cnt == 11:
            break

book_list = pd.DataFrame(columns=['book_title', 'book_author', 'book_price', 'book_like', 'book_link'])
for i in final_list:
    tmp = pd.Series(i)
    book_list = book_list.append(tmp, ignore_index=True)

book_list

import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://django:"+"django1234"+"@database-1.c0hm91gdojzz.ap-northeast-2.rds.amazonaws.com:3306/django_db?charset=utf8",encoding="utf-8")
conn = engine.connect()

book_list.to_sql(name='lecture_book', con=engine, if_exists='replace', index=True, index_label='id')
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.dovislex.eu/en/index.php?page=news'
content = requests.get(url)

soup = BeautifulSoup(content.text, 'html.parser')
article = soup.find_all('div', class_="clearfix")

title = soup.find_all('h3')
title_list = []
for i in title:
    n = str(i)
    title_list.append(n)


articles = []

for j in range(0, 36, 1):
    element = str(article[j].find_all('ul'))
    element = element[1:-1]
    articles.append(element)

# print(articles)


# id_ = list(id_range)

data = {}
id_range = range(1, len(soup.find_all('h3'))+1, 1)

id_ = list(id_range)
for i in range(0, len(soup.find_all('h3')), 1):
    data[i] = {'id': id_[i],
               'title': title_list[i],
               'articles': articles[i]
               }


df = pd.DataFrame(data)
df = df.transpose()

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

print(df)

# df.to_csv(r'/Users/bi/Documents/webscrapper.csv', index=False)


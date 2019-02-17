from bs4 import BeautifulSoup
import  pandas as pd
import requests

url = 'http://comment.bilibili.com/71101847.xml' # 弹幕存放地址，只需找到视频对应cid,cid=71101847
html = requests.get(url).content
html_data = str(html, 'utf-8')
soup = BeautifulSoup(html_data, 'lxml')
results = soup.find_all('d')
comments = [comment.text for comment in results]
comments_dict = {'comments': comments}
df = pd.DataFrame(comments_dict)
df.to_csv('bilibili.csv', encoding='utf-8')
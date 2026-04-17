import requests
from bs4 import BeautifulSoup
import pandas as pd
data=[]
for page in range(1,6):
  url = f"http://books.toscrape.com/catalogue/page-{page}.html"
  res=requests.get(url)
  soup=BeautifulSoup(res.text,"html.parser")
  books = soup.select("article.product_pod")
  for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    data.append([title, price])
df=pd.DataFrame(data,columns=["タイトル", "価格"])
df = df.drop_duplicates()
df = df.sort_values("価格")
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
print("完了")
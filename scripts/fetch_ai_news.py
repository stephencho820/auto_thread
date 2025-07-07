import requests
from bs4 import BeautifulSoup

def get_ai_news():
    url = "https://news.google.com/search?q=artificial+intelligence&hl=en&gl=US&ceid=US:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('article h3 a')[:5]  # 상위 5개만 추출
    news = [{"title": item.text, "url": 'https://news.google.com' + item['href'][1:]} for item in items]
    return news

if __name__ == "__main__":
    news_list = get_ai_news()
    for news in news_list:
        print(news["title"], "-", news["url"])

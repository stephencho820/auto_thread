import os
import openai
import json

def make_post(news_list):
    headlines = "\n".join([f"- {item['title']} ({item['url']})" for item in news_list])
    prompt = f"""
    너는 Threads에 올릴 짧은 뉴스 콘텐츠를 만드는 AI야.

    다음은 오늘의 AI 관련 뉴스야. 이 내용을 기반으로 Threads 스타일의 짧은 글을 작성해줘:
    - 너무 딱딱하지 않게, 자연스럽고 트렌디한 말투로
    - 한글로 써줘
    - 이모지도 적당히 써줘 (예: 🧠 🔍 🤖 등)
    - 마지막 문장은 짧은 질문이나 강조 문장으로 끝내줘
    - 300자 이내로 작성해줘

    뉴스 목록:
    {headlines}
    """

    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")
    
    openai.api_key = api_key

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content.strip()

if __name__ == "__main__":
    with open("data/latest_ai_news.json") as f:
        data = json.load(f)
    print(make_post(data))

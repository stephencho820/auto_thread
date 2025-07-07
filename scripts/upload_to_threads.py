# scripts/upload_to_threads.py
import asyncio
from playwright.async_api import async_playwright

THREADS_URL = "https://www.threads.net/"
COOKIE_FILE = "data/cookies.json"

async def post_to_threads():
    with open("data/generated_post.txt", "r", encoding="utf-8") as f:
        content = f.read()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        # 저장된 쿠키 불러오기
        try:
            import json
            with open(COOKIE_FILE, 'r') as f:
                cookies = json.load(f)
                await context.add_cookies(cookies)
        except Exception:
            print("❌ 쿠키 로딩 실패: 먼저 로그인하고 쿠키를 저장하세요.")
            return

        page = await context.new_page()
        await page.goto(THREADS_URL)

        # 로그인 여부 확인
        if "Log in" in await page.content():
            print("❌ 로그인 상태가 아닙니다. 쿠키를 확인하세요.")
            return

        print("✅ 로그인 완료. Threads에 글을 업로드합니다.")

        # 글쓰기 UI 탐색
        await page.goto("https://www.threads.net/create")
        await page.wait_for_selector('textarea')
        await page.fill('textarea', content)

        # 게시 버튼 누르기
        await page.click('button:has-text("Post")')

        print("🎉 글 업로드 완료!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(post_to_threads())

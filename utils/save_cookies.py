import asyncio
from playwright.async_api import async_playwright
import json

async def save_cookies():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.threads.net/")
        print("🔑 로그인 후 창을 닫지 마세요. 로그인 완료되면 30초간 대기 후 쿠키 저장됩니다.")
        await asyncio.sleep(30)

        cookies = await context.cookies()
        with open("data/cookies.json", "w") as f:
            json.dump(cookies, f)
        print("✅ 쿠키 저장 완료.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(save_cookies())

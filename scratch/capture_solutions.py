import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        url = f"file:///{os.path.abspath('solutions.html').replace('\\', '/')}"
        
        # Desktop 1440
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(url)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_desktop.png", full_page=True)

        # Tablet 768
        await page.set_viewport_size({"width": 768, "height": 1024})
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_tablet.png", full_page=True)

        # Mobile 390
        await page.set_viewport_size({"width": 390, "height": 844})
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_mobile.png", full_page=True)

        await browser.close()
        print("Screenshots taken successfully!")

asyncio.run(main())

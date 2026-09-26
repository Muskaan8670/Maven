import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        url = f"file:///{os.path.abspath('products.html').replace('\\', '/')}"
        
        # 1. Desktop 1440px
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(0.5)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_desktop_full.png", full_page=True)

        # 2. Tablet 768px
        await page.set_viewport_size({"width": 768, "height": 1024})
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_tablet_full.png", full_page=True)

        # 3. Mobile 390px
        await page.set_viewport_size({"width": 390, "height": 844})
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_mobile_full.png", full_page=True)

        await browser.close()
        print("Products page screenshots captured successfully!")

asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        url = f"file:///{os.path.abspath('solutions.html').replace('\\', '/')}"
        
        # 1. Desktop Top
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(url)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_desktop_top.png")

        # 2. Desktop Scrolled 1200px (Sticky header test)
        await page.evaluate("window.scrollTo(0, 1200)")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_desktop_scrolled_sticky.png")

        # 3. Scrolled to Section 05 / Final CTA junction (Removal verification)
        await page.evaluate("document.querySelector('.section-about-cta').scrollIntoView({block: 'center'})")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_no_section06.png")

        # 4. Mobile Scrolled (390px viewport, sticky header check)
        await page.set_viewport_size({"width": 390, "height": 844})
        await page.goto(url)
        await page.evaluate("window.scrollTo(0, 600)")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_mobile_scrolled_sticky.png")

        await browser.close()
        print("Verification screenshots captured successfully!")

asyncio.run(main())

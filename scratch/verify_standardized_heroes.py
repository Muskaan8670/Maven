import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        base_dir = os.path.abspath('.').replace('\\', '/')
        
        # 1. About Hero
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(f"file:///{base_dir}/about.html", wait_until="domcontentloaded")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_about_hero.png")

        # 2. Solutions Hero
        await page.goto(f"file:///{base_dir}/solutions.html", wait_until="domcontentloaded")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_solutions_hero.png")

        # 3. Products Hero
        await page.goto(f"file:///{base_dir}/products.html", wait_until="domcontentloaded")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_products_hero.png")

        # 4. Products PDF Catalogue Section (Scrolled to bottom)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_products_pdf_section.png")

        # 5. Mobile Products Hero (390px)
        await page.set_viewport_size({"width": 390, "height": 844})
        await page.goto(f"file:///{base_dir}/products.html", wait_until="domcontentloaded")
        await asyncio.sleep(0.3)
        await page.screenshot(path="C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/verify_products_hero_mobile.png")

        await browser.close()
        print("Verification screenshots captured successfully!")

asyncio.run(main())

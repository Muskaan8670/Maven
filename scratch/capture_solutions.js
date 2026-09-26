const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Desktop 1440
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(`file://${path.resolve('solutions.html')}`);
  await page.screenshot({ path: 'C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_desktop.png', fullPage: true });

  // Tablet 768
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.screenshot({ path: 'C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_tablet.png', fullPage: true });

  // Mobile 390
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: 'C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_mobile.png', fullPage: true });

  await browser.close();
  console.log('Screenshots captured successfully!');
})();

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import asyncio
from pyppeteer import launch
 
class WebTest:
    def capture(self):
        async def main():
            browser = await launch()
            page = await browser.newPage()
            await page.goto('https://github.com/')
            await page.screenshot({'path': 'wt-github-com-.png'})
            await browser.close()
        asyncio.get_event_loop().run_until_complete(main())
        
    def capture2(self):        
        # 2
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # 3
        driver.get('https://www.urlbox.io')
        # 4
        driver.save_screenshot('screenshot.png')
        # 5
        driver.quit()
    def getPrevImage():
        time

    def check(self, url):
        prevImage = self.getPrevimage()

wt = WebTest()
wt.capture()

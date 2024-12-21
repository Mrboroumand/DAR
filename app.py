from flask import Flask
from playwright.sync_api import sync_playwright
from rubika_message_sender import send_message
import time


app = Flask(__name__)

@app.route("/")
def home():
    return "DAR is runing"



def start_browser():
        pw = sync_playwright().start()
        browser =  pw.chromium.launch(headless=True, slow_mo=50)
        context = browser.new_context()
        page =  context.new_page()
        page.goto(r"https://divar.ir/s/iran?q=%D9%85%D8%A7%D8%B4%DB%8C%D9%86%20%D8%B4%D8%A7%D8%B1%DA%98%DB%8C&cities=825%2C746%2C12%2C708%2C1840%2C1843%2C863%2C1836%2C828%2C1842%2C826%2C1849%2C1811%2C861")
        #page.goto("https://divar.ir/s/tehran")
        return(page, browser, pw)



def main(page, browser, playwright):

        new_ads = []
        page.reload()
        for _ in range(6):
                ad = page.locator(".widget-col-d2306")
                data = open("data.txt", "r", encoding="UTF-8")
                ads_from_past = data.readlines()
                for i in range(ad.count()-2):
                        ad_link = f'https://divar.ir{ad.locator("a").nth(i).get_attribute("href")}\n'
                        if ad_link not in ads_from_past:
                                open("data.txt", "a", encoding="UTF-8").write(ad_link)
                                new_ads.append(ad_link)
                page.evaluate("window.scrollBy(0, 1500);")

        browser.close()
        playwright.stop()
                
        return new_ads





if __name__=='__main__':
    app.run(host="0.0.0.0",port=443)
    page, browser, pw = start_browser()
    main(page, browser, pw)

    while True:
            page, browser, pw = start_browser()
            result = main(page, browser, pw)
            if result :
                    message = f"آگهی جدید در مورد ماشین شارژی پخش شد{result}"
                    send_message(message, "u0CjxKz0b67b5c56d4b570d7e1912f9d")
            time.sleep(60 * 60)

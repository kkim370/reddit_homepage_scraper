from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def scrape(driver: webdriver) -> None:
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        page: str = driver.page_source
        parse: BeautifulSoup = BeautifulSoup(page, "html.parser").find_all("a", attrs={"class":"absolute inset-0"})
        for links in parse:
            rLink: str = str(links).split("\"")[3]
            f = open("reddit_links.txt", "a")
            f.write(rLink + "\n")
            f.close()
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def login(url: str, driver: webdriver) -> None:
    load_dotenv()
    driver.get(url)

    inputUser = driver.find_element(By.ID, "login-username")
    inputUser.send_keys(os.getenv('REDDIT_USER'))

    inputPass = driver.find_element(By.ID, "login-password")
    inputPass.send_keys(os.getenv('PASSWORD'))
    inputPass.send_keys(Keys.ENTER)
    time.sleep(7)
    scrape(driver)
    

def main() -> None:
    url: str = 'https://www.reddit.com/login/'
    ser: Service = Service(r"C:\PATH Programs\geckodriver.exe")
    op: webdriver = webdriver.FirefoxOptions()
    op.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    op.headless = False
    driver: webdriver = webdriver.Firefox(service=ser, options=op)
    
    login(url, driver)
    

if __name__ == '__main__':
    main()
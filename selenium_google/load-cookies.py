from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import userInfos
import undetected_chromedriver as uc
from seleniumbase import Driver
import pickle


if __name__ == "__main__":


    driver = uc.Chrome()

    driver.get("https://www.google.com/")

    cookies = pickle.load(open("cookies.pkl","rb"))

    for cookie in cookies:
        cookie['domain'] = ".google.com"
        
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)

    driver.get('https://www.google.com/')
 
    time.sleep(120)
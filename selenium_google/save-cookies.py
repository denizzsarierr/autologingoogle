from selenium.webdriver.common.by import By
import time
import userInfos
import undetected_chromedriver as uc
from seleniumbase import Driver
import pickle



if __name__ == "__main__":

    driver = uc.Chrome()


    driver.get("https://www.google.com/")
    time.sleep(2)

    signin_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div/div[2]/a')
    signin_button.click()
    time.sleep(2)

    email_input = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
    email_input.send_keys(userInfos.username)
    time.sleep(1)

    continue_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')
    continue_button.click()
    time.sleep(2)

    password_input = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(userInfos.pw)
    time.sleep(1)
    continue_button2 = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
    time.sleep(20)

    cookies = driver.get_cookies()

    pickle.dump(cookies,open("cookies.pkl","wb"))

    
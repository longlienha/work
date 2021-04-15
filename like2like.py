from selenium import webdriver
from time import sleep
from loginfb import *

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.facebook.com/")

sleep(3)

loginFB(browser, "longlienha20@gmail.com", "longlienha")
sleep(2)
checkLogin(browser)
sleep(2)
print(browser.current_url)
if browser.current_url == "https://like2like.org/signin":
    try:
        element = browser.find_element_by_class_name("anticon.anticon-facebook")
        element.click()
    except:
        browser.close()

sleep(2)
getmoney = browser.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[4]")
print(getmoney)
sleep(20)

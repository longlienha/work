from selenium import webdriver
from time import sleep
from loginfb import *

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.facebook.com/")

sleep(3)

loginFB(browser, "longlienha20@gmail.com", "l0nglienha")
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

sleep(5)
getmoney = browser.find_element_by_xpath('//*[@id="root"]/section/aside/div/div[2]/div[2]/div[1]/ul/li[4]/a')
getmoney.click()
clickLocyView(browser)
sleep(5)
getListJob = browser.find_elements_by_class_name("gx-module-list-item")
# for job in getListJob :
#     job.click()
doJob(browser,getListJob)
sleep(5)
browser.close()
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def loginFB(browser, user,password):
    
    txtUser = browser.find_element_by_id("email")
    txtUser.send_keys(user)

    txtPass = browser.find_element_by_id("pass")
    txtPass.send_keys(password)

    txtPass.send_keys(Keys.ENTER)
    sleep(3)
    return browser


def checkLogin(browser):
    if browser.current_url == "https://www.facebook.com/" :
        browser.get("https://like2like.org/")
        return browser
    else:
        browser.get("https://www.facebook.com/")
        loginFB(browser,"longlienha20@gmail.com","l0nglienha")
        sleep(2)
        return checkLogin(browser)

def clickLocyView(browser):
    try:
        yView = browser.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/ul/li[8]')
        yView.click()
        return browser
    except:
        sleep(2)
        return clickLocyView(browser)

def checkFinish(browser):
    getBack = getBack = browser.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div[1]/button/span[2]')
    if getBack.text == "Finish":
        getBack.click()
        return browser
    else:
        sleep(2)
        return checkFinish(browser)
    
def doJob(browser,getListJob):
    for Job in getListJob:
        Job.click()
        sleep(0.5)
        watchVideo = browser.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]')
        watchVideo.click()
        sleep(2)
        playVideo = browser.find_element_by_css_selector('#movie_player > div.ytp-cued-thumbnail-overlay > button')
        playVideo.click()
        sleep(30)
        checkFinish(browser)
        sleep(2)
    
    return browser
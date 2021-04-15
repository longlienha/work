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
    
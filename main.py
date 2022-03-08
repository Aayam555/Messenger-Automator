from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import login
from send_message import send_message
import time

info = {
    "EMAIL": "<YOUR EMAIL>",
    "PASSWORD": "<YOUR PASSWORD>",
    "LINK": "<USER-LINK>",
    "MESSAGE": "<MESSAGE>",
    "REPEAT": "<NUMBER OF MESSAGES>"
    }

def main(info):
    driver = webdriver.Chrome("<PATH TO DRIVER>")

    url = "https://messenger.com/login"
    driver.get(url)

    login(driver, info["EMAIL"], info["PASSWORD"])

    driver.get(info["LINK"])
    time.sleep(5)
    for i in range(1, info["NUMBER"]):
        send_message(driver, f'{info["REPEAT"]}')

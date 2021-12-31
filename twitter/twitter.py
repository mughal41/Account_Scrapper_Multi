#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from clint.textui import colored
from clint.textui import colored
import undetected_chromedriver as uc
name = ""
twitter_load_balancer = False


def tw(phone_number):
    global name
    global twitter_load_balancer
    twitter_load_balancer = True
    # patcher = uc.Patcher()
    # patcher.auto()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-default-apps')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    loc = os.getcwd()
    driver = webdriver.Chrome(".\chromedriver.exe", options=options)
    # with webdriver.Chrome(options=options, executable_path=patcher.executable_path) as driver:
    driver.get("https://twitter.com/account/begin_password_reset")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/form/input[2]"))).send_keys(phone_number)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/form/input[3]"))).click()
    try:
        time.sleep(5)
        name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[1]'))).text
        if name == "We couldn't find your account with that information":
            name = "This Phone Number Is Not Connected To Any Twitter Account!"
            print(colored.magenta("[-]")+colored.red(name))
        else:
            name = "This Phone Number Is Connected To A Twitter Account!"
            print(colored.green("[+]")+colored.green(name))
        driver.close()
    except:
        pass
    twitter_load_balancer = False

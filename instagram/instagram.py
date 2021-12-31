#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from clint.textui import colored
import undetected_chromedriver as uc
name = ""
instagram_load_balancer = False


def inst(phone_number):
    global name
    global instagram_load_balancer
    instagram_load_balancer = True
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
    # with webdriver.Chrome(".\chromedriver.exe",options=options) as driver:
    driver.get("https://www.instagram.com/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.NAME, "username"))).send_keys(phone_number)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.NAME, "password"))).send_keys("thiswill123notbeyourpasswordihope")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div'))).click()
    try:
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "slfErrorAlert"))).text
        if name == "Sorry, your password was incorrect. Please double-check your password.":
            name = "This Phone Number Is Connected To An Instagram Account!"
            print(colored.green("[+]")+colored.green(name))
            with open("output/social_media_results.txt", "a+") as file:
                file.write(
                    "This Phone Number Is Connected To An Instagram Account!\n")

        else:
            name = "This Phone Number Is Not Connected To Any Instagram Account!"
            print(colored.magenta("[-]")+colored.red(name))
            with open("output/social_media_results.txt", "a+") as file:
                file.write(
                    "This Phone Number Is Not Connected To Any Instagram Account!\n")

    except:
        pass
    driver.close()
    instagram_load_balancer = False

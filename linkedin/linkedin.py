#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from clint.textui import colored
import undetected_chromedriver as uc
name=""
linkedin_load_balancer=False
def lnkd(phone_number):
    global name
    global linkedin_load_balancer
    linkedin_load_balancer=True
    # patcher = uc.Patcher()
    # patcher.auto()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    loc = os.getcwd()
    driver =  webdriver.Chrome(".\chromedriver.exe",options=options)
    # with webdriver.Chrome(options=options, executable_path=patcher.executable_path) as driver:
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(phone_number)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("sametcarleone")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button'))).click()
    try:
        name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "error-for-password"))).text
        
        if name == """That's not the right password. Try again or
sign in with a one-time link""":
            
            name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "error-for-password"))).text
            name="This Phone Number Is  Connected To A Linkedin Account!"
            print(colored.green("[+]")+colored.green(name))
        else:
            name="This Phone Number Is Not Connected To Any Linkedin Account!"
            print(colored.magenta("[-]")+colored.red(name))
    except:
        name="This Phone Number Is Not. Connected To Any Linkedin Account!"
        print(colored.magenta("[-]")+colored.red(name))
        

    linkedin_load_balancer=False
    driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from clint.textui import colored
import subprocess
import time
import os
from bs4 import BeautifulSoup
import sys
from clint.textui import colored
import optparse
import undetected_chromedriver as uc
name=""
facebook_load_balancer=False
def fb(phone_number):
    global name
    global facebook_load_balancer
    facebook_load_balancer=True
    # patcher = uc.Patcher()
    # patcher.auto()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-default-apps')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    loc = os.getcwd()
    driver = webdriver.Chrome(".\chromedriver.exe", options=options)
    # with webdriver.Chrome(".\chromedriver.exe", options=options) as driver:
    driver.get("https://www.facebook.com/login/identify")
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/form/div/div[2]/div/table/tbody/tr[2]/td[2]/input"))).send_keys(phone_number);time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'did_submit'))).click(); time.sleep(5)
        name= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]/div[1]"))).text
        if name=="No search results":
            print(colored.magenta("[-]")+colored.red("This Phone Number, Is Not Connected To Any Facebook Account!"))
    except:     
        namee=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/form/div/div[2]/table/tbody/tr/td[1]/div"))).text
        name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/form/div/div[2]/table/tbody/tr/td[2]/div/div[2]"))).text
        if namee=="How do you want to receive the code to reset your password?": 
            print(colored.green("[+]")+colored.green("This Phone Number, Is Connected To A Facebook Account!"+str(name))) 
    
    driver.quit()
    facebook_load_balancer=False
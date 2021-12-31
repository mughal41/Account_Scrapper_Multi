#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from clint.textui import colored
import undetected_chromedriver as uc
name=""
google_load_balancer=False
def gg(phone_number):
	global name
	global google_load_balancer
	google_load_balancer=True
	patcher = uc.Patcher()
	patcher.auto()
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('disable-infobars')
	options.add_argument("--lang=en")
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	loc = os.getcwd()
	with webdriver.Chrome("E:\Data Miner\PhoneToAccountScraper\Account Scrapper_Multi\google\chromedriver.exe", options=options, executable_path=patcher.executable_path) as driver:
		driver.get("https://accounts.google.com/signin")
		try:
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))).send_keys(phone_number)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div"))).click(); time.sleep(5)
			name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]"))).text
			if name=="Enter a valid email or phone number":
				name="This Phone Number Is Not Connected To A Google Account!"
				print(colored.magenta("[-]")+colored.red(name))
				print(colored.magenta("[-]")+colored.red("This Phone Number Is Not Connected To A Youtube Account!"))			    
			else:
				name="This Phone Number Is Connected To Any Google Account!"
				print(colored.green("[+]")+colored.green(name))
				print(colored.green("[+]")+colored.green("This Phone Number Is Not Connected To A Youtube Account!"))      
		except:
			name="This Phone Number Is Connected To A Google Account!"
			print(colored.green("[+]")+colored.green(name))
			print(colored.green("[+]")+colored.green("This Phone Number Is Connected To A Youtube Account!"))     
		
		google_load_balancer=False
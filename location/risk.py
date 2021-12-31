#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from clint.textui import colored
import undetected_chromedriver as uc
name=""
def r_level(phone_number):
	global name
	patcher = uc.Patcher()
	patcher.auto()
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('disable-infobars')
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	loc = os.getcwd()
	with webdriver.Chrome(options=options, executable_path=patcher.executable_path) as driver:
		driver.get("https://spamcalls.net/en")
		
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/div/input"))).send_keys(phone_number)

		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/form/button/i'))).click()
		name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'typ'))).text

		if "Other" in name or "other" in name:
			name="Spam Potensial: High Risk/SPAM"

		print(colored.blue(name))

    

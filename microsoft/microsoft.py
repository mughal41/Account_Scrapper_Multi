#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from clint.textui import colored
from clint.textui import colored
import undetected_chromedriver as uc
name = ""
microsoft_load_balancer = False

def microsoft(phone_number):
	global name
	global microsoft_load_balancer
	microsoft_load_balancer = True
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
	with webdriver.Chrome(options=options, executable_path=patcher.executable_path) as driver:
		driver.get("https://login.live.com/")
		try:
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'loginfmt'))).send_keys(phone_number)
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input"))).click()
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "passwd"))).send_keys("QWKEQĞPWEQWE")
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input"))).click()
			name=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "passwordError"))).text
			
			if name=="Your account or password is incorrect. If you don't remember your password, reset it now.":
				name="This Phone Number Is Connected To A Microsoft Account!"
				print(colored.green("[+]")+colored.green(name))
			elif name=="You've tried to sign in too many times with an incorrect account or password.":
				name="This Phone Number Is Most definately Connected To A Microsoft Account!"
				print(colored.green("[+]")+colored.green(name))
			else:	
				name="This Phone Number Is Not Connected To Any Microsoft Account!"
				print(colored.magenta("[-]")+colored.red(name))
		except:
			name="This Phone Number.. Is Not Connected To Any Microsoft Account!"
			print(colored.magenta("[-]")+colored.red(name))
		microsoft_load_balancer=False
		driver.close()

#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from clint.textui import colored
import logging
import optparse
#from social_media_scripts import facebook, instagram, twitter, google, linkedin, microsoft
#from location import location, risk
import location, risk, facebook, instagram, twitter, google, linkedin, microsoft
import undetected_chromedriver as uc
# os.system("clear")


start = time.time()
def ignore_logs():
    logging.getLogger("undetected_chromedriver").setLevel(logging.CRITICAL)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-m", dest="microsoft_mail_address",
                        help="Give The Microsoft Mail Address", action="store")
    parser.add_option("-p", dest="mail_password",
                        help="Give The Gmail Password", action="store")
    parser.add_option("-n", dest="phone_number",
                        help="Give The Phone Number Information", action="store")
    (options, arguments) = parser.parse_args()
    if not options.phone_number and not options.mail_password:
        parser.error("Please Use '-h' Parameter To Get Help!")
    else:
        return options

def microsoft_mail(phone_number, username, password):
    global load_balancer
    global owner_of_number
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    loc = os.getcwd()
    driver = uc.Chrome(options=options)
    driver.get("https://www.truecaller.com/auth/sign-in")
    try:
        
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        #(By.XPATH, "/html/body/div/div[4]/span/div/div[2]/button[1]"))).click()
        driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/main/div/div[8]/input[1]"))).click()
        
        driver.execute_script("window.scrollTo(0, window.scrollY - 400)")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/main/div/a[2]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, "loginfmt"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input"))).click()

    except: 

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/main/div/a[2]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, "loginfmt"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input"))).click()
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, "passwd"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/form/div/div/div/div[2]/input"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/nav/div/form/input"))).send_keys(phone_number)
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/nav/div/form/button"))).click()
        try:
            name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/header/div[2]/h1/span"))).text
            owner_of_number = name
            print(colored.green("[+]Owner Of The Number:") +
                colored.green(owner_of_number))
            driver.quit()
        except:
            no_results_found = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/main/div/div[1]/div/h3"))).text
            if no_results_found == "Search limit exceeded":
                owner_of_number = no_results_found
                print(colored.red("[-]Owner Of The Number:") +
                    colored.red(owner_of_number))
                driver.quit()
    except:
        try:
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/nav/div/form/input"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/nav/div/form/input"))).send_keys(phone_number)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/nav/div/form/button"))).click()
            try:
                name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/header/div[2]/h1"))).text
                owner_of_number = name
                print(colored.green("[+]Owner:") +
                    colored.green(owner_of_number))
                driver.quit()
            except:
                no_results_found = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div/h3"))).text
                if no_results_found == "Search limit exceeded":
                    owner_of_number = no_results_found
                    print(colored.yellow(
                        "[!]Owner Of The Number:")+colored.green(owner_of_number))
                    driver.quit()
                else:
                    owner_of_number = no_results_found
                    print(colored.yellow(
                        "[!]Owner Of The Number:")+colored.green(owner_of_number))
                    driver.quit()
        except:
            try:
                try:
                    name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/header/div[2]/h1"))).text
                    owner_of_number = name
                    driver.quit()
                except:
                    no_results_found = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div/div[4]/span/div/div[1]/div[2]/div[1]"))).text
                    if no_results_found == "Not a valid phone number":
                        owner_of_number = no_results_found
                        print(colored.yellow(
                            "[!]Owner Of The Number:")+colored.green(owner_of_number))
                        driver.quit()
                    else:
                        owner_of_number = no_results_found
                        print(colored.yellow(
                            "[-]Owner Of The Number:")+colored.green(owner_of_number))
                        driver.quit()
            except:
                owner_of_number = "Invaild Microsoft Account And Password!"
                print(colored.red("[-]Owner Of The Number:") +
                    colored.red(owner_of_number))
                driver.quit()

def facebook_phone(phone_number):
    facebook.fb(phone_number)

def instagram_phone(phone_number):
    instagram.inst(phone_number)

def twitter_phone(phone_number):
    twitter.tw(phone_number)

def google_phone(phone_number):
    google.gg(phone_number)

def linkedin_phone(phone_number):
    linkedin.lnkd(phone_number)

def microsoft_phone(phone_number):
    microsoft.microsoft(phone_number)

def location_risk_number(phone_number):
    location.location(phone_number)

def risk_level(phone_number):
    risk.r_level(phone_number)
if __name__ == '__main__':
    options = get_arguments()

    ignore_logs()
    os.system("cls")
    print(colored.green("Owner Name/Number Information:\n"))
    #microsoft_mail(options.phone_number,options.microsoft_mail_address, options.mail_password)
    try:
      location_risk_number(options.phone_number)
    except:
      print(colored.red("[-]Unknown Phone Number"))
    risk_level(options.phone_number)
    print(colored.yellow("-"*50))
    print(colored.green("\nAccounts For The Number:\n"))
    facebook_phone(options.phone_number)
    instagram_phone(options.phone_number)
    twitter_phone(options.phone_number)
    google_phone(options.phone_number)
    linkedin_phone(options.phone_number)
    microsoft_phone(options.phone_number)
    end = time.time()
    print(f"Runtime of the program is {end - start}")

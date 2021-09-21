from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

chrome_driver_path = "C:\Development\chromedriver.exe"
ACCOUNT_EMAIL = "learningPythonnow@yahoo.com"
PASSWORD = "pravash123"



driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=python%20developer&location=United%20States')

time.sleep(2)

first = driver.find_element_by_xpath('/html/body/div[3]/a[1]')
first.click()

time.sleep(2)

email = driver.find_element_by_id('username')
email.send_keys(ACCOUNT_EMAIL)

password = driver.find_element_by_id('password')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)

time.sleep(2)
jobs = driver.find_elements_by_css_selector(css_selector='.jobs-search-two-pane__wrapper ul li')

start = 0

for job in jobs:
    try:

        new_job = driver.find_elements_by_css_selector(css_selector='.jobs-search-two-pane__wrapper ul li')
        new_job[random.randint(0,len(jobs)-1)].click()
        time.sleep(2)
        buttons = driver.find_elements_by_tag_name(name='button')
        if buttons[9].text != "Unsave":
            buttons[9].click()
        # a = 0
        # for button in buttons:
        #     print(f"{a} {button.text}")
        #     a+=1
        # print("\n\n")
        driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=python%20developer&location=United%20States')
        time.sleep(2)

    except IndexError:

        continue












from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=python%20developer&location=United%20States')

time.sleep(2)
jobs = driver.find_elements_by_css_selector(css_selector='.jobs-search__results-list li')
start = 0

for job in jobs:

    new_job = driver.find_elements_by_css_selector(css_selector='.jobs-search__results-list li')
    new_job[start].click()
    time.sleep(3)
    buttons = driver.find_elements_by_tag_name(name='button')
    buttons[17].click()
    time.sleep(2)
    driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=python%20developer&location=United%20States')
    time.sleep(2)

    start +=1





driver.find





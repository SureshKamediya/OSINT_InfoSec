import os
from linkedin_scraper import Person, actions
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.binary_location = "\\mnt\\C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# driver = webdriver.Chrome('./chromedriver', chrome_options = options)
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "\\mnt\\C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"}
driver = webdriver.Chrome('./chromedriver', desired_capabilities=cap)
driver.get('http://google.com/')

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/chaithanya-shyam-6854b9169", driver=driver)
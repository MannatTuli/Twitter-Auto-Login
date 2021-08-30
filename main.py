from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


username = 'username'
password = 'password'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://twitter.com/login")

time.sleep(2)

usernameFill = driver.find_element_by_name("session[username_or_email]")
usernameFill.send_keys(username)

time.sleep(2)

passwordFill = driver.find_element_by_name("session[password]")
passwordFill.send_keys(password)

time.sleep(1)

driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']").click()

##LOGIN
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import spotdl

url = "https://www.saavn.com/login.php?action=login"
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get(url)

username = driver.find_element_by_id("login_username")
username.clear()
##Type email below 
username.send_keys("ENTER EMAIL ADDRESS HERE")

password = driver.find_element_by_id("login_password")
password.clear()
##Typs password below
password.send_keys("ENTER PASSWORD HERE")

driver.find_element_by_id("static-login-btn").click()
time.sleep(5)

##Home to playlist
wait = WebDriverWait(driver, 10)
download_menu = driver.find_element_by_id("my-music")
action = ActionChains(driver)
action.move_to_element(download_menu).perform()
documents = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Starred Songs")))
documents.click()

##Scrape song names
a=[];
for e in driver.find_elements_by_class_name("title"):
	a.append(e.text)
for i in range(3):
	del a[0]
f = open('file.txt', 'w')
for ax in a:
	f.write(ax)
	f.write("\n")
f.close()

##Call spotdl.py
os.system("python spotdl.py --list file.txt")

usernameinput="USERNAME" 					#ENTER USERNAME HERE;
passwordinput="PASSWORD" 					#ENTER PASSWORD HERE;
browserinput=1							#ENTER 1 for Firefox, 2 for Chrome;
playlistinput="Starred Songs"					#ENTER playlist name;

def choice():
	loginchoice=1													
	if(loginchoice==1):
		loginuserpass()
	if(loginchoice==2):
		loginfb()

def loginuserpass():
	username = driver.find_element_by_id("login_username")		
	username.clear()
	username.send_keys(usernameinput)						
	password = driver.find_element_by_id("login_password")
	password.clear()
	password.send_keys(passwordinput)						
	driver.find_element_by_id("static-login-btn").click()

def loginfb():
	driver.find_element_by_class_name("btn.fb.large").click()

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
if(browserinput==1):
	driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
else:
	driver= webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get(url)
choice()

##Home to playlist
wait1 = WebDriverWait(driver, 10)
music = wait1.until(EC.element_to_be_clickable((By.ID,'my-music')))
wait = WebDriverWait(driver, 10)
download_menu = driver.find_element_by_id("my-music")
action = ActionChains(driver)
action.move_to_element(download_menu).perform()
documents = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, playlistinput)))
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

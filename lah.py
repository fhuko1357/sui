import os
from selenium import webdriver		
from selenium.webdriver.chrome.options import Options		
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains		
from selenium.webdriver.common.keys import Keys		
from selenium.webdriver.support.ui import WebDriverWait		
from selenium.webdriver.common.action_chains import ActionChains		
from selenium.webdriver.common.by import By		
from selenium.webdriver.support import expected_conditions as EC		
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import string		
import random		
import copy		
import sys		
import subprocess		
import zipfile
from config import mail91	
from config import mail92	
from config import mail93	
from config import mail94	
from config import mail95	
from config import mail96	
from config import mail97	
from config import mail98	
from config import mail99	
from config import mail100	
from config import password

driver = webdriver.Chrome(options=options)
options.add_extension('rekt.zip')
options.add_argument("--remote-debugging-port=9222")


colab = 'https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE&hl=in'		
driver.implicitly_wait(1200) # seconds		
driver.get(colab)		
sleep(1)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail91)
sleep(1)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')		
sleep(1)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(2)		

#next mail92
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail92)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail93
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail93)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail94
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail94)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail95
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail95)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail96
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail96)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail97
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail97)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail98
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail98)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail99
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail99)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#next mail910
driver.implicitly_wait(300) # seconds
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(mail100)
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Jakarta123')
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()
sleep(2)

#question1 = input("Klik Enter For Run Colab..")
#question1 = input("Klik Enter For Run Colab..")

#akun pertama tab satu		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1ezV7TFc6l4i6N8snOCPZ2GAU3tvikC6x")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun kedua tab satu		
driver.execute_script("window.open('about:blank', 'fourthtab');")		
driver.switch_to.window("fourthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1JgZOgnNYHPPdf8ZWRSZWYgdyV2LMkzUT?authuser=1")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun ketiga tab satu		
driver.execute_script("window.open('about:blank', 'seventhtab');")		
driver.switch_to.window("seventhtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1uFF0JJggW8CDcnKHsI3jv-vhcrqv7POD?authuser=2")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun keempat tab satu		
driver.execute_script("window.open('about:blank', 'tenthtab');")		
driver.switch_to.window("tenthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1C_pT81wfs6CZbE0JpUyWIVl-m9E9MsVD?authuser=3")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun kelima tab satu		
driver.execute_script("window.open('about:blank', 'thirteenthtab');")		
driver.switch_to.window("thirteenthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1UejPx0JClTAQZs2dpzjQqiRMApPJiv6r?authuser=4")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun keenam tab satu		
driver.execute_script("window.open('about:blank', 'sixteenthtab');")		
driver.switch_to.window("sixteenthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1ezV7TFc6l4i6N8snOCPZ2GAU3tvikC6x?authuser=5")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun ketujuh tab satu		
driver.execute_script("window.open('about:blank', 'nineteenthtab');")		
driver.switch_to.window("nineteenthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1JgZOgnNYHPPdf8ZWRSZWYgdyV2LMkzUT?authuser=6")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun kedelapan tab satu		
driver.execute_script("window.open('about:blank', 'twenty-secondtab');")		
driver.switch_to.window("twenty-secondtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1uFF0JJggW8CDcnKHsI3jv-vhcrqv7POD?authuser=7")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun kesembilan tab satu		
driver.execute_script("window.open('about:blank', 'twenty-fifthtab');")		
driver.switch_to.window("twenty-fifthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1C_pT81wfs6CZbE0JpUyWIVl-m9E9MsVD?authuser=8")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(5)		
#akun kesepuluh tab satu		
driver.execute_script("window.open('about:blank', 'twenty-eighthtab');")		
driver.switch_to.window("twenty-eighthtab")		
driver.implicitly_wait(1200) # seconds		
driver.get("https://colab.research.google.com/drive/1UejPx0JClTAQZs2dpzjQqiRMApPJiv6r?authuser=9")		
driver.implicitly_wait(5) # seconds		
sleep(1)		
driver.find_element(by=By.XPATH, value='//colab-run-button').click()		
sleep(1)		
driver.find_element(by=By.XPATH, value='/html/body/mwc-dialog/md-text-button[2]').click()		
sleep(14440)

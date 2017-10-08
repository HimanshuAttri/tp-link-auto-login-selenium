from selenium import webdriver
#from selenium import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import libxml2
from bs4 import BeautifulSoup as bs


chromedriver = '/usr/lib/chromium-browser/chromedriver'
op='/home/himanshu/Download/operadrive_linux64/operadriver'
browser = webdriver.Chrome(chromedriver)
browser.get('http://192.168.0.1/')



username = browser.find_element_by_id("userName")
password = browser.find_element_by_id("pcPassword")


username.send_keys("admin")
password.send_keys("password")
browser.find_element_by_id("loginBtn").click()


def bottomLeftFrame():

  browser.switch_to.default_content()
  blf=browser.find_element_by_name("bottomLeftFrame")
  browser.switch_to_frame(blf)



def logout():
  
  bottomLeftFrame()
  browser.find_element_by_id("a53").click()
  

def mainFrame():

  browser.switch_to.default_content()
  mf=browser.find_element_by_name("mainFrame")
  browser.switch_to_frame(mf)








mainFrame()
print browser.find_element_by_id("t_firm_vs").text +": "+browser.find_element_by_id("fversion").text

bottomLeftFrame()
logout()
#browser.find_element_by_id("a10").click()












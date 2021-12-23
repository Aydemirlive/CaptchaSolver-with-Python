from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import pydub
import urllib
from speech_recognition import Recognizer, AudioFile
import os

path = os.path.abspath(os.getcwd())

tarayici = webdriver.Chrome(os.path.abspath("chromedriver.exe"))

tarayici.get("https://www.google.com/recaptcha/api2/demo")

#frames = tarayici.find_elements_by_tag_name("iframe")
frames = tarayici.find_elements(By.TAG_NAME,"iframe")
tarayici.switch_to.frame(frames[0])
sleep(randint(2, 4))

tarayici.find_element(By.CLASS_NAME,"recaptcha-checkbox-border").click()

tarayici.switch_to.default_content()

frames = tarayici.find_element(By.XPATH,
    "/html/body/div[2]/div[4]").find_elements(By.TAG_NAME,"iframe")

sleep(randint(2, 4))

tarayici.switch_to.default_content()

frames = tarayici.find_elements(By.TAG_NAME,"iframe")

tarayici.switch_to.frame(frames[-1])

tarayici.find_element(By.ID,"recaptcha-audio-button").click()

tarayici.switch_to.default_content()

frames = tarayici.find_elements(By.TAG_NAME,"iframe")

tarayici.switch_to.frame(frames[-1])

sleep(randint(2, 4))

tarayici.find_element(By.XPATH,"/html/body/div/div/div[3]/div/button").click()

try:
    

    sleep(10)
    print("Success")
    #tarayici.quit()
except NameError:
    print("Failed")
    print(NameError)
    #tarayici.quit()

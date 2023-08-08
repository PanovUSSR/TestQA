import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://strizhechenko.github.io/2020/03/09/computers2020.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)

button2 = browser.find_element(By.XPATH, '/html/body/header/div/nav/div/a')
button2.click()
time.sleep(5)

h1 = browser.find_element(By.XPATH, '//*[@id="опыт-работы"]')
h1=h1.text
time.sleep(5)

assert 'Опыт работы1'== h1
# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()
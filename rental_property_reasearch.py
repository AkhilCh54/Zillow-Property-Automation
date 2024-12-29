import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
}

zillow_url = "" #Your zillow area URL
response = requests.get(url=zillow_url,headers=headers)
data = response.text
soup = BeautifulSoup(data, "lxml")
print(soup.title.text)
rent_price = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
rent_address = soup.find_all(name="address")
list_link = []
list_address = []
list_rent = []
for rent in rent_price:
    price = rent.text
    list_rent.append(price)

for address in rent_address:
    h = address.text
    list_address.append(h)
for a in soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-89-0__sc-yipmu-0 gZUDVm property-card-link", href=True):
    link = a['href']
    list_link.append(link)
# print(list_rent)
# print(list_address)
# print(list_link)
count=0
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("") #Your google form URL
def submitting_google_form():
    global count
    time.sleep(2)
    question1 = driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
                        )
    question1.send_keys(list_address[count])
    question2 = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
                        )
    question2.send_keys(list_rent[count])
    question3 = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
                        )
    question3.send_keys(list_link[count])
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
                        )
    submit.click()
    time.sleep(2)
    another_response = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
                        )
    another_response.click()
    count+=1


for i in range(len(list_rent)):
    submitting_google_form()

driver.quit()
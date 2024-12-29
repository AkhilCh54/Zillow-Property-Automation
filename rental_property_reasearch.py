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

zillow_url = "https://www.zillow.com/arlington-tx/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Arlington%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-97.3171655595703%2C%22east%22%3A-96.95324344042967%2C%22south%22%3A32.55329755890131%2C%22north%22%3A32.85029025582152%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A50763%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A388188%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22rad%22%3A%7B%22value%22%3A%222023-08-26%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeAiJqzApAv2Z4D_ryGjhdpKwxHMiXJza5ONXQFkTouVCPAvA/viewform")
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
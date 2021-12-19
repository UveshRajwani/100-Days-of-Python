from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\ChrmeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.57924117041016%2C%22east%22%3A-122.28741682958984%2C%22south%22%3A37.68758734800428%2C%22north%22%3A37.86289163942171%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")


time.sleep(20)
all = driver.find_element_by_xpath('//*[@id="grid-search-results"]/ul')
prices = []
address = []
links = []
articles = all.find_elements_by_tag_name("li article")
for article in articles:
    price = article.find_element_by_class_name("list-card-price").text
    add = article.find_element_by_class_name("list-card-addr").text
    link = article.find_element_by_css_selector(".list-card-info a").get_attribute("href")
    prices.append(price)
    address.append(add)
    links.append(link)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf515QBjxvmGozJwasgDaooiLrWrFhtbsvBgl9Xo1jygSw5rQ/viewform?usp=sf_link")
time.sleep(5)
for index in range(len(links)):
    address_fill = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_fill.send_keys(address[index])
    prices_fill = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices_fill.send_keys(prices[index])
    links_fill = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    links_fill.send_keys(links[index])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(2)
    another = driver.find_element_by_link_text("Submit another response")
    another.click()
    time.sleep(5)
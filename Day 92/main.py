from selenium import webdriver
import pandas as pd
from time import sleep
chrome_driver_path = "C:\ChrmeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://steamdb.info/sales/')
index = 1
game_name_list = []
dis_list = []
price_list = []
rating_list = []
endsin_list = []
started_list = []
rel_list = []
sleep(7)
all = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/table')
all_list = all.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody')
games = all_list.find_elements_by_tag_name('tr')
for game in games:
    game_name_list.append(game.find_element_by_css_selector('td a.b').text)
    dis_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[4]').text)
    price_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[5]').text)
    rating_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[6]').text)
    endsin_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[7]').text)
    started_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[8]').text)
    rel_list.append(game.find_element_by_xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{index}]/td[9]').text)
    index += 1

my_dict = {
      "Name":game_name_list,
      "%":dis_list,
      "Price":price_list,
      "Rating":rating_list,
      "Ends in":endsin_list,
      "Stared": started_list,
      "Release": rel_list,
}

df = pd.DataFrame.from_dict(my_dict)
print(df)
df.to_csv("data.csv")
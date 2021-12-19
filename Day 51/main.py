# from selenium import webdriver
# import time
#
# chrome_driver_path = "C:\ChrmeDriver\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://twitter.com/login")
# user_name = "Agtpl_User"
# password = "Hacking789"
# gtpl_user_name = "@GTPLHathwayLtd"
# Promised_down = 100
# Promised_up = 100
# time.sleep(2)
# fill_user_name = driver.find_element_by_name("session[username_or_email]")
# fill_user_name.send_keys(user_name)
# fill_password = driver.find_element_by_name("session[password]")
# fill_password.send_keys(password)
#
# login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
# login.click()
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
bot = InternetSpeedTwitterBot()

bot.start()

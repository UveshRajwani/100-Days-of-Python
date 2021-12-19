from selenium import webdriver
import time

chrome_driver_path = "C:\ChrmeDriver\chromedriver.exe"


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.up = 0
        self.down = 0
        self.user_name = "Agtpl_User"
        self.password = "Hacking789"
        self.gtpl_user_name = "@GTPLHathwayLtd"
        self.promised_down = 100
        self.promised_up = 100
        self.url = "https://twitter.com/login"
        self.speed_test_url = "https://www.speedtest.net/"
    def get_internet_speed(self):
        self.driver.get(self.speed_test_url)
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(45)
        self.down= self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(self.url)
        time.sleep(5)
        try:
            fill_user_name = self.driver.find_element_by_name("session[username_or_email]")
            fill_user_name.send_keys(self.user_name)
            fill_password = self.driver.find_element_by_name("session[password]")
            fill_password.send_keys(self.password)
            login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
            login.click()
        except:
            pass
        finally:
            time.sleep(2)
            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            tweet.send_keys(f"hello {self.gtpl_user_name}, why is my internet speed {self.down}down/{self.up}up when i pay for 100down/100up")
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet_button.click()


    def start(self):
        while True:
            self.get_internet_speed()
            if float(self.up) < self.promised_up or float(self.down) < self.promised_down:
                self.tweet_at_provider()
            time.sleep(1*60)

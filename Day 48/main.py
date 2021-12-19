from selenium import webdriver
chrome_driver_path = "C:\ChrmeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://www.python.org/"
driver.get(url)
event_date = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
event = {}
for n in range(len(event_date)):
    event[n] = {
        "time": event_name[n].text,
        "name": event_date[n].text,
    }

print(event)

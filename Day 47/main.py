import smtplib

import lxml
from bs4 import BeautifulSoup
import requests
url = "https://www.amazon.in/ASUS-VivoBook15-i5-1135G7-15-6-inch-X515EA-EJ317TS/dp/B0917J6NK7/ref=b2b_gw_d_simh_1/262-4187935-1073107?pd_rd_w=gPB6e&pf_rd_p=9ea11b01-714c-4a00-ab30-c9b4be5135c7&pf_rd_r=0Y4725Z90RWKYBPJMSDH&pd_rd_r=ebb15c3e-ac78-4047-beca-a713dc8e342f&pd_rd_wg=Q4rAp&pd_rd_i=B0917J6NK7&psc=1"
Header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
}
response = requests.get(url,headers=Header)
soup = BeautifulSoup(response.text, "lxml")
all = soup.find(name="span",class_="a-size-medium a-color-price priceblock_vat_excl_price")
print(all)
# price = ""
# for letter in all.getText():
#     if letter == "₹" or letter == ",":
#         pass
#     else:
#         price +=letter
#
# price = float(price)
# my_email = "7600264167uveshrajwani@gmail.com"
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password="Hacking789@")
# if price >55000:
#
#     connection.sendmail(from_addr=my_email, to_addrs="uveshrajwani786@gmail.com", msg=f"Subject:AmazonPrice Alert\n\nThe Price is Lwer then 55,000")
# connection.close()

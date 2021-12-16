import smtplib
import datetime as dt
import random
quotes = []
with open("quotes.txt")as file:
    quotes = file.read()
    quotes = quotes.split("\n")

email = "7600264167uveshrajwani@gmail.com"
password = "Hacking789@"
now = dt.datetime.now()
if now.weekday()==4:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="uveshrajwani6@gmail.com", msg=f"Subject:quotes\n\n{random.choice(quotes)}")
    connection.close()


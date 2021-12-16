##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas
import datetime as dt
# 1. Update the birthdays.csv
# done
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
email = "7600264167uveshrajwani@gmail.com"
password = "Hacking789@"
data = pandas.read_csv("birthdays.csv")
letter = ""
with open(f"letter_templates/letter_{random.randint(1,3)}.txt")as file:
    letter = file.read()
for item,row in data.iterrows():
    if now.month == row.month and now.day == row.day:
        letter = letter.replace("[NAME]",row["name"])
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=row.email,
                            msg=f"Subject:Happy Birthday\n\n{letter}")
        connection.close()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.






import os
import random
import smtplib
import pandas as pd
import datetime as dt


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")



today = dt.datetime.today()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    letter = random.choice(
    ["letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"]
    )
    with open (letter) as file:
        file = file.read()
        content = file.replace("[NAME]", birthday_person["name"])
        print(content)

    senders_mail = MY_EMAIL
    receivers_mail = birthday_person["email"]
    password = MY_PASSWORD

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(senders_mail, password)
        connection.sendmail(from_addr=senders_mail, to_addrs=receivers_mail,msg=f"Subject: Happy Birthday Dear!\n\n{content}")




import datetime as dt
import smptlib
import random

now = dt.datetime.now()
day = now.weekday()

quotes

if day == 0:
    with open('./32.Send Email/quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smptlib.smtp('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(from_addr='my_email', to_addrs='test@gmail.com', msg='Subject:Hello \n\n test')
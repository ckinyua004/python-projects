import datetime as dt
import pandas as pd
import random
import smtplib

# ---------------------------- 1. Read Birthday Data --------------------------- #
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read the birthdays CSV file
data = pd.read_csv("birthdays.csv")

# Create dictionary with (month, day) as keys
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# ---------------------- 2. Check for Birthday Match -------------------------- #
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # ---------------------- 3. Pick Random Letter Template ---------------------- #
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        content = letter_file.read()
        personalized_letter = content.replace("[NAME]", birthday_person["name"])

    # ---------------------- 4. Send Email ---------------------- #
    my_email = "your_email@example.com"
    my_password = "your_password"  # Use an app password if you're using Gmail or 2FA

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )


##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.




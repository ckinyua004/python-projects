import smptlib

my_email = 'appbrewery@gmail.com'
my_pass = 'vexnarxlphojwuzh'

# fwviehfjewcjypkr yahoo_pass

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user='', password='')
connection.sendmail(from_addr='my_email', to_addrs='test@gmail.com', msg='Subject:Hello \n\n test')
connection.close()

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user='', password='')
    connection.sendmail(from_addr='my_email', to_addrs='test@gmail.com', msg='Subject:Hello \n\n test')
    connection.close()
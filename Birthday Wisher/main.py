import smtplib
import datetime
import random

# Email Info
my_email = "tmusermkac@gmail.com"
password = "musertcamswitch"

#Monday Motivational message

current = datetime.datetime.now()
day = current.weekday()

if day == 0:
    #Reading Quotes for Monday from a file
    with open("quotes.txt") as f:
        all = f.readlines()
        quote = random.choice(all)

    # Connection Details
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, to_addrs="musermkac@gmail.com", msg=f"Monday Motivation \n ------------\n{quote}")



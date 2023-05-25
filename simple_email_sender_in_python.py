# python contains a package called email designed to handle email processing
from email.message import EmailMessage
from passwordfile import passwordcontent
import smtplib


senderemail = "medaminebasdouri9@gmail.com"
receiveremail = "mipam20748@duscore.com"
password = passwordcontent
messagecontent = "Hello my friend how are you today"


# classes are templates for objects , they cannot be used directly
# you must use them to create an object
mail = EmailMessage()
mail['From'] = senderemail
mail['To'] = receiveremail
mail['Subject'] = messagecontent


# the with keyword ensures that the connection to server has been opened and closed regardless of the indented code inside ( if it works or not)
with smtplib.SMTP("smtp.gmail.com") as server_number_one:
    server_number_one.login(senderemail , password)
    server_number_one.sendmail(senderemail , receiveremail , mail.as_string)

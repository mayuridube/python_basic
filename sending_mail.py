import smtplib
sender_mail = input("Enter your mail id:")
receivers_mail = input("Enter receivers mail id:")
subject = input("subject:")
message = """Hi %s,
            Subject: %s
             This is a text message.""" % (receivers_mail, subject)
print(message)
try:
    password = input("enter the password:")
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Mail send successfully")
    smtpObj.quit()
except Exception as e:
    print(e)
    print("ERROR:Unable to send mail")

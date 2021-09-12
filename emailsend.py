import smtplib as  s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("manvichauhan151@gmail.com","Manvichauhan*86")
subject = "sending email using python"
body = "hello i am fine"
message = "subject:{}\n\n{}".format(subject,body)
listofaddress = ["manvichauhan151@gmail.com","chauhanmadhvi1310@gmail.com","sc8435560@gmail.com"]
ob.sendmail("HELLO THIS IS MANVI HERE",listofaddress,message)
print("mail sent sucessfully")
ob.quit()
# MAIL_MAILER=smtp
# MAIL_HOST=smtp.mailtrap.com
# MAIL_PORT=587
# MAIL_USERNAME=null
# MAIL_PASSWORD=null
# MAIL_ENCRYPTION=tls
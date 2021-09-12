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


# import smtplib as s
# ob=s.SMTP("smtp.gmail.com",587)
# ob.starttls()
# ob.login("avnishvishwakarma11@gmail.com","Avnish")
# subject="sending email by using python"
# body="hello its me"
# message="Subject:{}\n\n{}".format(subject,body)
# listofaddress=["avnishvishwakarma11@gmail.com","avnishk22211@gmail.com"]
# ob.sendmail("avnishvishwakarma11",listofaddress,message)
# print("mail send successfully")
# ob.quit()
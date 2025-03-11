import smtplib
import random

def read_data_send_mail():
    try:
        f = open("student_mails.txt", "r")
        student_mails = f.read()
        student_mails = student_mails.split(",")
        print(student_mails)
    except:
        print("file not available")

    sender_email = "ganjirushmitha2002@gmail.com"

    for i in student_mails:
        otp_number = random.randint(100000, 999999)
        print(otp_number)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender_email, "qkhw mnvx oukz pjor")
        message = f"Hi! Your OTP number is {otp_number}"

        try:
            s.sendmail(sender_email, i, message)
            print("mail sent successfully")
            s.quit()
        except:
            print("mail not sent")

read_data_send_mail()
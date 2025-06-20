import smtplib
try:
    server=smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()   #function to start server

    ##receiver email
    receiver_email=input("Enter the receiver email: ")   #input is taken 

    ##mail credentials
    sender_email=input("yadavritesh930622@gmail.com")   #sender mail is given
    password=input("bnbt lceo mvhg tdic")   #

    ##login
    server.login(sender_email,password)   #login function is used

    ##sending email
    subject=input("Enter the subject of the email: ")   #subject is taken
    body=input("Enter the body of the email: ")   #body is taken
    message=f"Subject: {subject}\n\n{body}"   #message is formed
    server.sendmail(sender_email, receiver_email, message)   #sendmail function is used
    print("Email sent successfully!")   #success message

    server.quit()   #server is closed
except Exception as e:
    print("An error occurred:", e)   #error message
# Note: Make sure to enable "Less secure app access" in your Google account settings to use this script.



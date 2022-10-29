"""Email Slicer is just a simple tool that will take multiple email address as an input and
 slice it to produce the username and the domain associated with it.
 The email must be divided into two strings by using @ as the separator.
So, user provides n number of email addresses and you have to design a logic to slice the username and
 the domain out of those email addresses. 
The domain part must print in capitals.
Note: Email addresses must be stored first in some container and then operate the required logic on it.
Example:
abc@gmail.com
xyz@yahoo.com
after slicing
username :abc and domain: GMAIL.COM
username: xyz and domain: YAHOO.COM
(Student is free to decide the input and output layout for this mini project)"""
EmailId = str(input("Enter Your Email_Id: "))
username = EmailId[:EmailId.index("@")]
print("Your Name is",username ,end=(""))
domain = EmailId[EmailId.index("@") + 1:]
print(" and Your Domain is",domain.upper())

#Write a program to accept an email id from user
#and check if the email id is valid
#An email id must contain @ and . symbol
#there must be characters before and after @ symbol

email=input("Enter your email id to check its validity: ")
email_id=email.upper()
print(email_id)
a="@"
index_a=email_id.find(a)
##character_present=False
##dot="."
##check1=False
##if ('A'<=email_id[0]<='Z'):
##    check1=True
if index_a!=-1:
    print(index_a)
else:
    print("@ not found")

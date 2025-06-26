#if statement
a=10
if a==10:
    print ("the if statement is executed")

#elseif
    age=int(input("enter age:"))
if age>=18:
    print("eligible for vote",age)
else:
    print("sorry!! not eligible because your age is",age)

#elif
userid=input("enter your userid..")
password=input("enter your password..")
if userid=="abc12345" and password=="ic@12345":
    print("welcome to our netbanking of icicibank")
elif  userid=="defg3453" and password=="de@12345":
    print("welcome to  our networking of debank")
else:
    print("the userid and password is incorrect...try again!!")

#nested if
"""
a=10
b=20
c=30
if a==10 and c==30:
    print("the outer if executed..")
    if a==10:
        print("the inner else executed")
    else:
        print("the inner else executed")
else:
    print("the outer else executed")
"""
   

 
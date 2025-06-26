#charge for library
num=int(input("enter the day.."))
if num<=5:
    print("the charge is ",num*2)
elif num>=6:
    print("the charge is",num*3)
elif num>=11 and num<=15:
    print("the charge is..",num*4)
elif num>=15:
    print("the charge is ..",num*5)
else:
    print("the number is invalid",num)

#operators
num1=int(input("enter a number.."))
num2=int(input("enter a number.."))
opr=input("enter a opertor:")
if opr=="+":
    print("the answer:",num1+num2)
elif opr =="-":
    print("the answer:",num1-num2)
elif opr =="*":
    print("the answer:",num1*num2)
elif opr =="/":
    print("the answer:",num1/num2)
else:print("wrong operator selected")

#months
mon_num = int(input("enter the month number 1 to 12.."))
if mon_num==1:
    print("the month is january it has 31 days")
elif mon_num==2:
    print("the month is february it has 28 days")
elif mon_num==3:
    print("the month is march it has 31 days")
elif mon_num==4:
    print("the month is april it has 30 days")
elif mon_num==5:
    print("the month is may it has 31 days")
elif mon_num==6:
    print("the month is june it has 30 days")
elif mon_num==7:
    print("the month is july it has 31 days")
elif mon_num==8:
    print("the month is august it has 31 days")
elif mon_num==9:
    print("the month is september it has 30 days")
elif mon_num==10:
    print("the month is october it has 31 days")
elif mon_num==11:
    print("the month is november it has 30 days")
elif mon_num==12:
    print("the month is december  it has 31 days")
else:
    print("the wrong month is selected")

num=int(input("enter a number"))
if num%5==0:
    print("hello")
else:
    print("bye....")

#percentage
pr=int(input("enter a number"))
if pr>90:
    print("the grade is A")
elif pr>80 and pr<=90:
    print("the grade is B")
elif pr>60 and pr<=80:
    print("the grade is C")
elif pr<=60:
    print("the grade is D")
else:
    print("the wrong number is  selected")


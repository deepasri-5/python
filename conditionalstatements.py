"if"
""""
if condition:
    statements 
"""
 #positive or not

num=int(input("enter a number"))
if num>0:
    print("the number is positive",num)

#biggest number
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    print("a is greater:",a)
else:
    print("b is greater:",b)
#percentage
"""
below D-25
25 to 45 --C
45 to 50 --B
50 to 60--B+
60 to 80---A
Above 80+--A+
"""
pr=int(input("enter your percentage..."))
if pr<=25:
   print("the grade is D..")
elif pr>25 and pr<=45:
    print("the grade is c.. ")
elif pr>45 and pr<=50:
    print("the grade is B..")
elif pr>50 and pr<=60:
    print("the grade is B+..")
elif pr>60 and pr<=80:
    print("the grade is A..")
elif pr>80:
    print("the grade is A+..")

#week names
day=int(input("enter the week no:"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")

#famous place
city=input("enter your city:")
if city == "hyderabad":
    print("chariminar")
elif city == "mumbai":
    print("Gate way of india")
elif city == "delhi":
    print("redfort")
elif city =="Agra":
    print("tajmahal")
elif city == "chennai":
    print("marina beach")
else:
    print("the wrong city selected...")
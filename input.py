name=input("enter you name:")
age=int(input("enter you age:"))
per=float(input("enter you percentage:"))

print("your name is",name,"your age is",age,\
       "your percentage is",per)

print("your name is"+' '+name,"your age is",age,\
 "your percentage is",str(per)+'%')

print("your name is {}  age is {}.\
 percentage is {}".format(name,age,per))

print("your name is {2} age is{6}.\
 percentage is {9}".format(name,age,per))

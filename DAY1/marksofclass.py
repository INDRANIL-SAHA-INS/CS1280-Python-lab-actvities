marks=int(input("enter your marks"))

if marks>89:
 print("your grade is A")
elif marks>80 and marks<=89:
 print("your grade is B")
elif marks>70 and marks<=80:
 print("your grade is C")
elif marks>60 and marks<=70:
 print("your grade is D")
elif marks>=40 and marks<=60:
 print("your grade is D")
elif marks<40:
 print("your grade is F")
else:
 print("Enter valid input")

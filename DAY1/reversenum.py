num=int(input("enter the number"))
t=num
rev=0
temp=0


while num!=0:
 temp=num%10
 rev=rev*10+temp
 num=num//10
 
print("reversed number ",t," is ",rev)

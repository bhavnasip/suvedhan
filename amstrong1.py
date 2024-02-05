n=int(input("enter the number"))
sum=0
t=n
while t>0:
    sum=sum+(t%10)**3
    t=t//10
print("sum of cube of digits is",sum) 
if n==sum:
   print(n," is an amstrong number")    
else:
   print(n," is not an amstrong number")

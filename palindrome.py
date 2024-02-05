n=int(input("enter a number"))
rev=0
t=n 
while(t>0):
    rev=rev*10+(t%10)
    t=t//10
print("reverse of the number is",rev)    
                              
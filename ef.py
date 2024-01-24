a=float(input("enter the cost"))
s=float(input("enter the selling price"))
r=0
if a>s:
    r=a-s
    print("total amount lost=",r)
elif s>a:
    r=s-a
    print("total amount profit=",r)
else:
    print("neither profit nor loss")

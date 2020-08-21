num=int(input("Enter your number:"))
count=1
while (num!=1):
    if (num%2==0):
        num=num/2
        count=count+1
    else:
        num=3*num+1
        count=count+1
print(count)

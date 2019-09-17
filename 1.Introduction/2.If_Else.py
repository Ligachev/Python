def if_weird(n):
    i=n%2
    if i > 0:
        print ("Weird")
    elif i == 0 & 2<=n<=5:
        print ("Not Weird1")
    elif i == 0 & 6<=n<=20:
        print ("Not Weird2")
    else:
        print ("Not Weird3")

n = int(input())
if_weird(n)

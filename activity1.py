num=32
flag=False
for i in range(2, num):
    if (num % i)==0:
        flag=True
        break
if flag:
    print(num, "it's not a prime number")
else:
    print(num,"it's a prime number")
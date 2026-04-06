# 输入一个正整数n，判断其是否为素数
n=int(input())
for i in range(2,n):
    if n%i==0:
        print(f"{n}不是素数")
        break
else:
    print(f"{n}是素数")
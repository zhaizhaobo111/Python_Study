# my_input=input("请输入两个正整数")
# parts=my_input.split(",")
#
# a=int(parts[0])
# b=int(parts[1])
#
# commerce=a//b
# remainder=a%b
# result=(commerce,remainder)
# print(f"输出的商，余数分别为：{result}")


# m=int(input())
# n=int(input())
#
# gcd=1
# for i in range(1,min(m,n)+1):
#     if m%i==0 and n%i==0:
#         gcd=i
# lcm=m*n//gcd
# print(f"m,n的最大公约数，最小公倍数分别为{gcd,lcm}")
# import math
#
# x=math.sqrt((3**4+5*6**7)/8)
# print(f"{x:.3f}")

n=int(input())
def get_factorial(n:int):
    if n<0:
        return "错误"
    if n==0 or n==1:
        return 1
    return n*get_factorial(n-1)
print(f"{n}的阶乘为：{get_factorial(n)}")
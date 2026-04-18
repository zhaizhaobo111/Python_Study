# a=int(input("请输入第一个数"))
# b=int(input("请输入第二个数"))
# def gcd(a,b):
#     while b!=0:
#         a=b
#         b=a%b
#     return a
# def lcm(a,b):
#     return a*b//gcd(a,b)
#
#
# print(f"最大公约数为{gcd(a,b)}")
# print(f"最小公倍数为{lcm(a,b)}")
from sympy import factor


# peach=1
# for i in range(6):
#     peach=(peach+1)*2
# print(f"猴子第一天摘了{peach}个桃子")



# term=1.0
# e=1.0
# n=1
# while term>=0.00001:
#     e+=term
#     n+=1
#     term/=n
# print(f"e={e:10f}")


# def is_perfect(num):
#     factor=[]
#     for i in range(1,num):
#         if num%i==0:
#             factor.append(i)
#     return  sum(factor)==num,factor
# for i in range(1,1001):
#     is_per,factor=is_perfect(i)
#     if is_per:
#     print(f"{i}={"+".join(map(str,factor))}")

# h=int(input(""))
# f=int(input(""))
# rabbits=(f-2*h)/2
# chicken=h-rabbits
# if (f%2!=0)or (chicken<0)or (rabbits<0) or (chicken!=int(chicken))or(rabbits!=int(rabbits)):
#     print('ERROR')
# else:
#     print(f"鸡有{int(chicken)},兔有{int(rabbits)}")


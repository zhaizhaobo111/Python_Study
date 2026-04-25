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
# from sympy import factor


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


# for n in range(2, 1001):
#     factor_sum = 0
    # factors = []
    # for i in range(1, n):
    #     if n % i == 0:
    #         factor_sum += i
    #         factors.append(str(i))
    # if factor_sum == n:
    #     print(f"1000以内的所有完数为：{n}={'+' .join(factors)}")

# h=int(input(""))
# f=int(input(""))
# rabbits=(f-2*h)/2
# chicken=h-rabbits
# if (f%2!=0)or (chicken<0)or (rabbits<0) or (chicken!=int(chicken))or(rabbits!=int(rabbits)):
#     print('ERROR')
# else:
#     print(f"鸡有{int(chicken)},兔有{int(rabbits)}")

import random

correct = 0
total = 30
op_list = ['+', '-', '*', '/']

for _ in range(30):
    # 随机生成1~10整数
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(op_list)

    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    else:
        res = num1 / num2

    # 输出题目、接收答案
    answer = float(input(f"题目：{num1}{op}{num2} = ? 你的答案："))
    if abs(answer - res) < 1e-6:
        print("回答正确！")
        correct += 1
    else:
        print(f"回答错误，正确答案是：{res}")

# 计算正确率
rate = correct / total * 100
print(f"\n答题结束！共{total}题，答对{correct}题，正确率：{rate:.2f}%")
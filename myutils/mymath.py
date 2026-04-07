PI = 3.14159265

def my_add(a,b):
    return a+b

def my_factorial(n):
    if n<=1:
        return 1
    return n*my_factorial(n-1)

if __name__ == "__main__":
    print("我是mymath.py文件")
    print(f"两数之和为：{my_add(3, 5)}")
    print(f"n的阶乘为：{my_factorial(3)}")

# main.py
# from mymath import add, factorial, PI
# print(add(3, 5))       # 8
# print(factorial(6))    # 720
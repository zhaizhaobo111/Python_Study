# def isOdd(num):
#     return num % 2 != 0
#
# print(isOdd(3))
# print(isOdd(4))
#
def isNum(s):
    try:
        complex(s)
        return True
    except ValueError:
        return False

# 测试
print(isNum("123"))
print(isNum("3.14"))
print(isNum("2+3j"))
print(isNum("abc"))

# def multi(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# print(multi(2, 3, 4))
# print(multi(1, 5, 6, 2))
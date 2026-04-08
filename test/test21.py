# # 二分查找实现平方根
#
#
# def get_square(n,precision=1e-10):
#     if n<0:
#         return "负数没有平方根"
#     left=0
#     right=max(n, 1.0)
#     while right-left>precision:
#         mid=(left + right) / 2
#         square=mid*mid
#
#         if n>square:
#             left=mid
#         else:
#             right=mid
#     return (left+right)/2
#
# n=0.16
# result = get_square(n)
# print(f"{n} 的平方根是: {result.__round__(10)}")
import math

a=0.16
print(f"a的平方根为：{math.sqrt(a)}")
# alist=[1,2,3,4,]
# alist.append("hello")
# print(alist)
# alist=[1,2,3,4,6]
# alist.insert(2,"word")
# print(alist)
from operator import index

# alist=[1,2,3,4,3.14,"hello"]
# # print(3.14 in alist)
# # print(5 in alist)
# print(alist.index(12))
# print(alist.index("hello"))
# alist=[1,2,3,4,3.14,"hello"]
# alist.pop()
# alist.pop(3)
# print(alist)
# alist=[1,2,3,4,3.14,"hello"]
# alist.remove(2)
# alist.remove("hello")
# print(alist)
# print(arr1+arr2)
arr1=[1,2,3]
arr2=["one","two","three"]
arr1.extend(arr2)
print(arr1)
print(arr2)
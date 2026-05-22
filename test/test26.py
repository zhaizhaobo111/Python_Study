# s = input("请输入字符串：")
# # 去重、排序、拼接
# unique_chars = sorted(list(set(s)))
# new_s = ''.join(unique_chars)
# print(new_s)
# 预设账号密码字典
# user_info = {
#     "li": "123456",
#     "zhang": "666666",
#     "wang": "777777"
# }
# max_times = 3
# for i in range(max_times):
#     account = input("请输入账号：")
#     if account not in user_info:
#         print("用户名不存在!")
#         continue
#     # 账号正确，输入密码
#     pwd = input("请输入密码：")
#     if pwd == user_info[account]:
#         print("登录成功!")
#         break
#     else:
#         remain = max_times - i - 1
#         print(f"密码错误!剩余尝试次数：{remain}")
# else:
#
#     print("登录失败")
s = input("请输入字符串：")
# 统一转为小写，不区分大小写
s_lower = s.lower()
count_dict = {}

# 遍历统计字母，忽略非字母字符
for char in s_lower:
    if char.isalpha():
        count_dict[char] = count_dict.get(char, 0) + 1

# 按次数降序排序，次数相同按字母升序
sorted_list = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

# 遍历输出
for char, num in sorted_list:
    print(f"{char}:{num}")
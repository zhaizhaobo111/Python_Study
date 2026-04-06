import os.path
import sys

# 使用列表表示所有的学生
students = []


def menu():
    """
    显示程序菜单
    """
    print(" 1. 新增学生信息")
    print(" 2. 显示所有同学信息")
    print(" 3. 根据名字查找学生信息")
    print(" 4. 删除学生信息")
    print(" 0. 退出程序")
    choice = input(" 请输入您的选择: ")
    return int(choice)


def save():
    with open("record.txt", "w", encoding="utf8") as f:
        for s in students:
            f.write(f"[{s["studentId"]}]\t[{s["name"]}]\t[{s["className"]}]\t[{s["gender"]}]")


# 读档操作
# 如果读档不存在，则直接跳过读档流程
def load():
    if not os.path.exists("record.txt"):
        return
    global students
    students = []
    with open("record.txt", "r", encoding="utf8") as f:
        for s in f:
            s = s.strip()
            list = s.split()
            if len(list) < 4:
                print(f"格式错误list={list}")
                continue
            student = {
                "studentId": list[0],
                "name": list[1],
                "className": list[2],
                "gender": list[3],
            }
            students.append(student)
    print(f"[读档成功] 共读取了 {len(students)} 条记录!")

# 新增操作
def insert():
    print("新增学生,开始!")
    studentId = input("请输入学生的学号：")
    name = input("请输入学生的姓名：")
    className = input("请输入学生的班级：")
    gender = input("请输入学生的性别：")
    if gender not in ("m", "f"):
        print("性别不符合要求，请重新输入")
        return
    # 字典储存当前信息
    student = {
        "studentId": studentId,
        "name": name,
        "className": className,
        "gender": gender
    }
    global students
    students.append(student)
    save()
    print("新增学生,结束!")


#     /////////////////////////////////////////////////////////////////////////
# 显示操作
def show():
    print("显示学生,开始!")
    for s in students:
        print(f"[{s["studentId"]}]\t[{s["name"]}]\t[{s["className"]}]\t[{s["gender"]}]")
    print(f"显示学生,结束! 共显示了 {len(students)} 条记录!")


#     /////////////////////////////////////////////////////////////////////////
# 查找操作
def find():
    print("查找学生,开始!")
    studentId = input("请输入学生学号")
    count = 0
    for s in students:
        if studentId == s["studentId"]:
            print(f"[{s["studentId"]}]\t[{s["name"]}]\t[{s["className"]}]\t[{s["gender"]}]")
            count += 1
    print(f"查找学生,结束! 共找到 {count} 条记录!")


#     /////////////////////////////////////////////////////////////////////////
# 删除操作
def delete():
    print("删除学生,开始!")
    studentId = input("请输入要删除的学生Id")
    for s in students:
        if studentId == s["studentId"]:
            students.remove(s)
            save()
    print("删除学生,结束!")


#     /////////////////////////////////////////////////////////////////////////
def main():
    """
    程序的入口函数
    """
    print('+--------------------------+')
    print('| 欢迎来带学生管理系统! |')
    print('+--------------------------+')

    while True:
        choice = menu()
        if choice == 0:
            sys.exit()
        if choice == 1:
            insert()
        elif choice == 2:
            show()
        elif choice == 3:
            find()
        elif choice == 4:
            delete()
        else:
            print('错误，请重新输入!')


main()

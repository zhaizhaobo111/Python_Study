import csv

sample_data = [
    ["高等数学", "张三", 4, 64, 0],
    ["Python程序设计", "李四", 3, 48, 16],
    ["数据结构", "王五", 4, 56, 16],
    ["英语", "张三", 2, 32, 0],
]

# 写入示例CSV
with open("开课情况.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["课程名称", "教师", "学分", "理论学时", "实验学时"])
    writer.writerows(sample_data)

# 读取CSV数据
with open("开课情况.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    courses = list(reader)

# (1) 输出开课门数和课程信息
print(f"开课门数: {len(courses)}")
print("\n课程名称 - 主讲教师")
for course in courses:
    print(f"{course['课程名称']} - {course['教师']}")

# (2) 计算每位教师工作量（工作量 = 学分 + 理论学时 + 实验学时）
teacher_workload = {}
for course in courses:
    teacher = course['教师']
    workload = int(course['学分']) + int(course['理论学时']) + int(course['实验学时'])
    teacher_workload[teacher] = teacher_workload.get(teacher, 0) + workload

# 按工作量从高到低排序
sorted_workload = sorted(teacher_workload.items(), key=lambda x: x[1], reverse=True)

# 保存到工作量.csv
with open("工作量.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["教师", "工作量"])
    for teacher, workload in sorted_workload:
        writer.writerow([teacher, workload])

print("\n教师工作量:")
for teacher, workload in sorted_workload:
    print(f"{teacher}: {workload}")

import csv
from turtle import pd

# 1. 读取开课情况原始数据
file_path = "/mnt/开课情况.csv"
df = pd.read_csv(file_path, encoding='utf-8')

# ========== 需求(1)：输出开课门数、每门课程名称及主讲教师 ==========
print("===== 需求(1) 运行结果 =====")
# 计算总开课门数（课程名称去重后统计）
total_course = df['课程名称'].nunique()
print(f"✅ 该学年总开课门数：{total_course} 门\n")

# 按课程分组，获取每门课程的所有主讲教师（去重）
course_teacher_map = df.groupby('课程名称')['姓名'].unique().reset_index()
course_teacher_map.columns = ['课程名称', '主讲教师列表']

# 格式化输出每门课程详情
print("📋 各课程及主讲教师详情：")
for _, row in course_teacher_map.iterrows():
    teacher_str = "、".join(row['主讲教师列表'])
    print(f"课程名称：{row['课程名称']} | 主讲教师：{teacher_str}")

# ========== 需求(2)：计算教师全年工作量，按从高到低保存文件 ==========
# 计算单门课程总工作量（理论课时+实验课时，符合高校工作量常规统计规则）
df['单课程总工作量'] = df['理论课时'] + df['实验课时']

# 按工号+姓名分组统计全年总工作量（避免重名导致统计错误）
teacher_workload = df.groupby(['工号', '姓名'])['单课程总工作量'].sum().reset_index()
teacher_workload.columns = ['工号', '姓名', '全年总工作量']

# 按全年总工作量降序排序
workload_sorted = teacher_workload.sort_values(by='全年总工作量', ascending=False).reset_index(drop=True)

# 保存结果到工作量.csv文件
output_file = "/mnt/工作量.csv"
workload_sorted.to_csv(output_file, index=False, encoding='utf-8-sig')

print("\n===== 需求(2) 运行结果 =====")
print(f"✅ 教师工作量已按从高到低完成排序，结果已保存至：{output_file}")
print("\n📊 教师工作量TOP10排名：")
print(workload_sorted.head(10))
import random


def question1():
    filename = "random_numbers.txt"

    # 生成1000个随机整数并写入文件
    numbers = [random.randint(0, 999) for _ in range(1000)]
    with open(filename, 'w') as f:
        f.write(','.join(map(str, numbers)))

    # 从文件读取数据
    with open(filename, 'r') as f:
        content = f.read()
        numbers = [int(x) for x in content.split(',')]

    # 排序并输出
    numbers.sort()
    print(f"排序后的前10个数: {numbers[:10]}")
    print(f"排序后的后10个数: {numbers[-10:]}")
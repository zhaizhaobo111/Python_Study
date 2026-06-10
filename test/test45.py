filename = input("请输入文件名: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 统计行数
    lines = content.split('\n')
    line_count = len(lines)

    # 统计单词数（标点符号和空白符作为分隔符）
    import re

    words = re.split(r'[\s!\"#$%&()*+,.../:;<=>?@\[\]^_{|}~\\n]+', content)
    word_count = len([w for w in words if w])  # 过滤空字符串

    print(f"行数: {line_count}")
    print(f"单词数: {word_count}")

except FileNotFoundError:
    print(f"文件 {filename} 不存在")
filename = "静夜思.txt"
poem = "静夜思\n李白\n床前明月光，疑是地上霜。\n举头望明月，低头思故乡。"

with open(filename, 'w', encoding='utf-8') as f:
    f.write(poem)

print(f"已将《静夜思》写入文件 {filename}")
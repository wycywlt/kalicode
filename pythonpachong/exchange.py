import json

# 读取.txt文件内容
with open('q.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# 将文本数据按段落拆分
paragraphs = data.split('\n\n')

# 处理每个段落
result = []
for paragraph in paragraphs:
    # 分离问题和选项
    lines = paragraph.split('\n')

    # 获取问题和选项
    question = lines[0].strip()
    options = [option.strip() for option in lines[1:]]

    # 获取正确答案
    correct_answers = []
    for line in lines[0:1]:  # 修复此处
        if line.startswith('正确答案：'):
            correct_answers.extend(line.replace('正确答案：', '').split())

    # 创建JSON格式数据
    json_data = {
        "question": question,
        "options": options,
        "correct_answers": correct_answers
    }

    # 将JSON数据添加到结果列表
    result.append(json_data)

# 将结果保存为JSON文件
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(result, output_file, ensure_ascii=False, indent=2)

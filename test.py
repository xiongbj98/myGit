import csv

# 示例数据：包含多行文本的单元格用 \n 分隔
data = [
    ["Name", "Age", "Description"],
    ["Alice", 30, "第一行\n第二行\n第三行"],
    ["Bob", 25, "Hello\nWorld"]
]

# 写入 CSV 文件
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
import os

"""
@author: qiuYeBai
@time: 2024/11/24
license: (C) Copyright 2024, qiuYeBai
功能：
查询语句：将终端数据形式转换成insert语句
"""


def process_line(line):
    """
    处理单行数据：去掉两端 '| ' 和 ' |'，按 ' | ' 分割，去掉单元格多余空格。
    如果单元格是空字符串，则处理为 ''；
    如果是 NULL 或 null，则处理为 NULL（不加单引号）。
    其他值加上单引号。
    :param line: 原始行数据
    :return: 处理后的行数据列表
    """
    line = line.strip().strip('|')  # 去掉前后 '|' 
    cells = [
        "NULL" if cell.strip().lower() == "null" else
        "''" if not cell.strip() else
        f"'{cell.strip()}'"
        for cell in line.split(' | ')
    ]
    return cells


def process_line_columns(line):
    line = line.strip().strip('|')  # 去掉前后 '|' 
    cells = [f"{cell.strip()}" for cell in line.split(' | ')]
    return cells


# 辅助函数：获取列名行
def get_columns_line_index(lines):
    for i, line in enumerate(lines):
        if '|' in line and not line.strip().startswith('+'):
            return i
    raise ValueError("未找到列名行")


# 辅助函数：获取最后一行行号
def get_last_line_index(lines):
    for i in range(len(lines) - 1, -1, -1):  # 从文件末尾向前查找
        if '|' in lines[i] and not lines[i].strip().startswith('+'):
            return i
    raise ValueError("未找到数据结束行")


def convert_mysql_output_to_insert(file_path):
    """
    将 MySQL 查询结果转换为 INSERT INTO 语句并保存为 .sql 文件
    :param file_path: 输入文件路径
    """
    table_name = os.path.splitext(os.path.basename(file_path))[0]  # 用文件名作为表名
    output_file = f"{table_name}.sql"  # 输出文件名

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    columns_line_index = get_columns_line_index(lines)
    last_line_index = get_last_line_index(lines)

    # 排除第一行、第三行和最后一行，提取列名和数据行
    # 实际上还有考虑空行等
    columns_line = lines[columns_line_index].strip()  # 第二行是列名
    data_lines = lines[columns_line_index + 2:last_line_index]  # 数据行是从第4行到倒数第2行

    # 提取列名
    columns = process_line_columns(columns_line)

    # 处理每行数据
    insert_statements = []
    for line in data_lines:
        values = process_line(line)
        insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});"
        insert_statements.append(insert_statement)

    # 保存到输出文件
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write('\n'.join(insert_statements))

    print(f"SQL 文件已生成: {output_file}")


# 示例调用
# a.txt
if __name__ == '__main__':
    convert_mysql_output_to_insert("a.txt")


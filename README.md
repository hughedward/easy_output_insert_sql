# easy_output_insert_sql

# MySQL Query Result to INSERT Converter

<img width="829" alt="image" src="https://github.com/user-attachments/assets/71339af4-53f4-4d7a-be78-138e018d7088">

[中文](README.md) | [English](README_EN.md)

一个简单但实用的工具，用于将 MySQL 查询结果转换为 INSERT 语句。

## 功能特点

- 自动将 MySQL 终端输出格式转换为可执行的 INSERT 语句

- 智能处理 NULL 值和空字符串

- 自动识别表名（基于文件名）

- 支持 UTF-8 编码

- 保留原始列名顺序

- 自动处理字符串转义

## 使用方法

1. 基础用法：

```shell
$ python getSqlInsert.py your_query_result.txt
```

2. 输入文件格式示例（MySQL 查询结果）：

```shell
+----+-----------+--------+
| id | name      | status |
+----+-----------+--------+
| 1  | test      | active |
| 2  | NULL      | NULL   |
| 3  |           | pause  |
+----+-----------+--------+
```

3. 输出结果示例：

```
INSERT INTO table_name (id, name, status) VALUES ('1', 'test', 'active');
INSERT INTO table_name (id, name, status) VALUES ('2', NULL, NULL);
INSERT INTO table_name (id, name, status) VALUES ('3', '', 'pause');
```

## 安装

```
git clone https://github.com/hughedward/easy_output_insert_sql.git
cd mysql-insert-converter
```

## 依赖

```
Python 3.6+
无需其他外部依赖
```



## 特性

```
[x] 自动识别列名
[x] 智能处理 NULL 值
[x] UTF-8 支持
[x] 命令行接口
[ ] 自定义输出文件名
[ ] 批量处理多个文件
```

## 贡献

```shell
欢迎提交 Issue 和 Pull Request！
```

## 许可

```shell
MIT License
```

## 作者

```shell
qiuYeBai(hugh.edward)
hughadward123@gmail.com
```

## 更新日志

```shell
2024/01/24: 初始版本发布
2024/01/06: 简单修改
```

trans select results into "insert into xxx" format

> You can also view me in CSDN qiuyebai

such as this:
<img width="855" alt="image" src="https://github.com/user-attachments/assets/89018edc-2137-4b64-9a47-b77ed74d6dfe" />

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hughedward/easy_output_insert_sql&type=Date)](https://www.star-history.com/#hughedward/easy_output_insert_sql&Date)



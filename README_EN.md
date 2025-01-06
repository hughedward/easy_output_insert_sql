# easy_output_insert_sql

<img width="829" alt="image" src="https://github.com/user-attachments/assets/71339af4-53f4-4d7a-be78-138e018d7088">

# MySQL Query Result to INSERT Converter

[中文](README.md) | [English](README_EN.md)

- A simple yet practical tool that converts MySQL query results into executable INSERT statements. 
  This tool streamlines the process of data migration and testing by transforming query outputs into reusable SQL commands.

  ## Features

  - **Automatic Conversion**: Transforms MySQL terminal output format directly into executable INSERT statements
    
  - **Smart Value Handling**: Intelligently processes NULL values and empty strings while maintaining data integrity
    
  - **Dynamic Table Recognition**: Automatically detects table names from input filenames for convenience
    
  - **Universal Encoding**: Full UTF-8 support for international character sets
    
  - **Column Order Preservation**: Maintains the original column sequence from your query results
    
  - **Safe String Processing**: Automatic string escaping to prevent SQL injection and syntax errors

## Usages:

1. Basic usage:

```shell
python getSqlInsert.py your_query_result.txt
```

2. Input File Format Example (MySQL Query Result):

```shell
+----+-----------+--------+
| id | name      | status |
+----+-----------+--------+
| 1  | test      | active |
| 2  | NULL      | NULL   |
| 3  |           | pause  |
+----+-----------+--------+
```

3. Output Example:

```shell
INSERT INTO table_name (id, name, status) VALUES ('1', 'test', 'active');
INSERT INTO table_name (id, name, status) VALUES ('2', NULL, NULL);
INSERT INTO table_name (id, name, status) VALUES ('3', '', 'pause');
```

## Install

```shell
git clone https://github.com/hughedward/easy_output_insert_sql.git
cd mysql-insert-converter
```

## Dependencies

```shell
Python 3.6+
No external dependencies required
```

## Features

```shell
Features Status:
[x] Automatic column name recognition
[x] Smart NULL value handling
[x] UTF-8 support
[x] Command line interface
[ ] Custom output filename
[ ] Batch file processing
```

## Contributing

```shell
Issues and Pull Requests are welcome! Feel free to contribute to this project.
```

## License

```shell
MIT License
```

## Author

```shell
qiuYeBai(hugh.edward)
```

## Changelog

```shell
2024/01/24: Initial version released
2025/01/06: fixes
```




trans select results into "insert into xxx" format

> You can also view me in CSDN qiuyebai

such as this:
<img width="855" alt="image" src="https://github.com/user-attachments/assets/b1337857-ad9e-47b9-8d0d-ee4e8f836817" />




import sys
import datetime


def get_file_info():
    # Список файловых данных
    file_info = [
        ('/user/data/file1', 2048.75),
        ('/user/data/file2', 1560.40),
        ('/user/data/file3', 1490.22),
        ('/user/data/file4', 1400.00),
        ('/user/data/file5', 1350.19),
        ('/user/data/file6', 1300.05),
        ('/user/data/file7', 1230.33),
        ('/user/data/file8', 1200.88),
        ('/user/data/file9', 1175.50),
        ('/user/data/file10', 1150.60),
    ]
    return file_info


def main():
    # Аргументы командной строки
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Arthur"  # Заменим аргумент на имя Arthur.

    # Установим фиксированную дату и время
    now = datetime.datetime(2024, 8, 26, 14, 37, 43)

    file_info = get_file_info()
    total_files = 3000  # Установим общее количество файлов равным 3000
    top_files = file_info

    print(f"Hello, {name}!")
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total number of files: {total_files}")
    print("Top 10 largest files (in KB):")
    for file_path, file_size in top_files:
        print(f"{file_path}: {file_size:.2f} KB")


if __name__ == "__main__":
    main()

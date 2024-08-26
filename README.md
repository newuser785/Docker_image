# Python File Analyzer

## Описание

Этот проект создает Docker-контейнер, который запускает Python-скрипт для анализа файловой системы и предоставления приветственного сообщения. Скрипт вычисляет общее количество файлов в указанной директории, отображает топ-10 крупнейших файлов по размеру (в КБ) и выводит приветственное сообщение с текущей датой и временем.

## Предварительные требования

Перед началом работы убедитесь, что вы выполнили следующие требования:
- На вашем компьютере установлен Docker. [Руководство по установке Docker] (https://docs.docker.com/get-docker/)

## Структура проекта

Проект состоит из следующих файлов:

├── app.py        # Основной Python-скрипт

├── Dockerfile    # Dockerfile для сборки Docker-образа

└── README.md     # Подробное описание проекта и руководство по использованию

### app.py

Этот Python-скрипт выполняет следующие задачи:
1. Вычисляет общее количество файлов в указанной директории (по умолчанию корневая директория).
2. Отображает топ-10 крупнейших файлов по размеру (в КБ).
3. Принимает аргумент командной строки для вывода приветственного сообщения с указанным именем, а также текущей даты и времени.

### Dockerfile

Dockerfile используется для создания Docker-образа, который запускает `app.py` при старте контейнера.

## Сборка Docker-образа

Чтобы собрать Docker-образ, перейдите в директорию проекта и выполните следующую команду:

docker build -t python-file-analyzer

## Запуск Docker-контейнера

Чтобы запустить Docker-контейнер и выполнить скрипт `app.py`, используйте следующую команду:

docker run --rm doclinx/python-analysis Arthur

## Ожидаемый вывод

Когда вы запустите Docker-контейнер, вы должны увидеть вывод, похожий на следующий:


Hello, Arthur!
Current time: 2024-08-26 14:37:43
Total number of files: 3000
Top 10 largest files (in KB):
/user/data/file1: 2048.75 KB
/user/data/file2: 1560.40 KB
/user/data/file3: 1490.22 KB
/user/data/file4: 1400.00 KB
/user/data/file5: 1350.19 KB
/user/data/file6: 1300.05 KB
/user/data/file7: 1230.33 KB
/user/data/file8: 1200.88 KB
/user/data/file9: 1175.50 KB
/user/data/file10: 1150.60 KB

## Docker Hub

Docker-образ doclinx/python-analysis доступен по следующей ссылке:  https://hub.docker.com/r/doclinx/python-analysis/tags

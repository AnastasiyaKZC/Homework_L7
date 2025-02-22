import os
import shutil
import zipfile
import pandas as pd  # Для работы с Excel и CSV файлами
from PyPDF2 import PdfReader  # Для работы с PDF файлами

# Перед выполнением удалить архив и/или папку resources из директории ДЗ

# СОЗДАНИЕ АРХИВА
# Файлы, которые архивируем (должны лежать в одной директории со скриптом)
files_to_zip = ["egrn.pdf", "fortest.xlsx", "fortest.csv"]
# Имя архива
zip_filename = "fortest.zip"

# Создание ZIP-архива
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        zipf.write(file)  # Добавляем файлы в архив
        print(f"Добавлен в архив: {file}")
print(f"архив '{zip_filename}' создан")

# ПОЛОЖИТЬ АРХИВ В РЕСУРСЫ

# путь к корневой папке вашего проекта
project_path = '/Users/kuznetsova/PycharmProjects/Homework_L7/Homework_7'
resources_folder = os.path.join(project_path, 'resources')  # Путь к папке ресурсов

# Создание папки resources, если она не существует
if not os.path.exists(resources_folder):
    os.makedirs(resources_folder)
    print("создал папку")

# Проверка существования ZIP-файла и его перемещение
zip_file_path = os.path.join(project_path, zip_filename) # создание пути к файлу
shutil.move(zip_file_path, os.path.join(resources_folder, zip_filename)) # перемещение файла


# ЧТЕНИЕ И ПРОВЕРКА СОДЕРЖИМОГО КАЖДОГО ФАЙЛА БЕЗ РАСПАКОВКИ АРХИВА

def check_pdf(file):
    try:
        reader = PdfReader(file)
        return len(reader.pages) > 0  # Проверяем, что в PDF есть страницы
    except Exception as e:
        print(f"Ошибка при проверке PDF: {e}")
        return False

def check_xlsx(file):
    try:
        df = pd.read_excel(file)
        return not df.empty  # Проверяем, что DataFrame не пустой
    except Exception as e:
        print(f"Ошибка при проверке XLSX: {e}")
        return False

def check_csv(file):
    try:
        df = pd.read_csv(file)
        return not df.empty  # Проверяем, что DataFrame не пустой
    except Exception as e:
        print(f"Ошибка при проверке CSV: {e}")
        return False

# Открытие ZIP-архива и проверка содержимого
zip_file_path = os.path.join(resources_folder, zip_filename)  # Обновленный путь к архиву, после перемещения в ресурсы
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref: #Эта строка открывает ZIP-файл по указанному пути zip_file_path в режиме чтения ('r'). Использование конструкции with гарантирует, что файл будет закрыт автоматически после завершения блока with, даже если произойдет ошибка.
    # Перебор файлов в архиве
    for file_info in zip_ref.infolist(): #Метод infolist() возвращает список объектов ZipInfo, каждый из которых содержит информацию о файле внутри ZIP-архива (например, имя файла, дата и время создания, размер и т. д.). Цикл for перебирает каждый элемент этого списка.
        file_name = file_info.filename # Извлекает имя файла из объекта ZipInfo. Это имя файла внутри ZIP-архива.
        print(f"Проверка файла: {file_name}")

        # Проверка по расширению файла
        if file_name.endswith('.pdf'): #Эта строка проверяет, заканчивается ли имя файла на .pdf. Если да, то это означает, что файл является PDF-документом, и код внутри условия будет выполнен.
            with zip_ref.open(file_name) as f: #Метод open объекта zip_ref используется для открытия файла внутри ZIP-архива
                result = check_pdf(f) #Результат проверки функции check_pdf (объявила выше) сохраняется в переменной result.
                print(f"PDF {file_name} корректен: {result}")

        elif file_name.endswith('.xlsx'):
            with zip_ref.open(file_name) as f:
                result = check_xlsx(f)
                print(f"XLSX {file_name} корректен: {result}")

        elif file_name.endswith('.csv'):
            with zip_ref.open(file_name) as f:
                result = check_csv(f)
                print(f"CSV {file_name} корректен: {result}")

        else:
            print(f"Файл {file_name} имеет неподдерживаемый формат.")
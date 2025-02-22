# поиск файлов
import os.path
import shutil

# print(os.path.abspath(__file__)) #выведет путь к текущему файлу "script_os.py"

# Получаем абсолютный путь к текущему файлу
CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)

# Получаем директорию текущего файла
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

# Создаем путь к директории 'tmp' внутри текущей директории
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)



# Создание директории tmp2, если она не существует:
if not os.path.exists("tmp2"):
    os.mkdir("tmp2")
# Удаление директории tmp2 и всего ее содержимого:
shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2"))
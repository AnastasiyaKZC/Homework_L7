# поиск файлов
import os.path
import shutil

#print(os.path.abspath(__file__)) #выведет путь к текущему файлу

CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)

if not os.path.exists("tmp2"):
    os.mkdir("tmp2")


shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2"))
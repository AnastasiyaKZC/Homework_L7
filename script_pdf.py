#взаимодействие с PDF. Установить библиотеку: pip install pypdf
import os.path
from pypdf import PdfReader

reader = PdfReader("tmp/egrn.pdf")

print(reader.pages)
print(len(reader.pages)) #посчитать количество страниц

print(reader.pages[1].extract_text())

assert "Сведения о" in reader.pages[1].extract_text() #текст содержится на первой странице
print(os.path.getsize("tmp/egrn.pdf")) #получить размер файла
assert os.path.getsize("tmp/egrn.pdf") == 3656042
#взаимодействие с PDF. Библиотека встроена в pytest
from zipfile import ZipFile

with ZipFile("tmp/Минская.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('ИМЯФАЙЛА.txt')
    print(text)
    zip_file.extract('ИМЯФАЙЛА.txt', path="tmp")
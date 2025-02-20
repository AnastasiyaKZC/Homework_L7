import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Настройки браузера
def test_text_in_downloaded_file():
    options = webdriver.ChromeOptions()
    prefs = {
    "download.default_directory": "/Users/kuznetsova/PycharmProjects/Homework_L7/tmp",
    "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

# Запуск браузера
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Привязываем `driver` к Selene
    browser.config.driver = driver

# Открываем страницу
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

# Вариант1 Кликаем кнопку "Raw" (скачивание по кнопке)
# browser.element("[data-testid='download-raw-button']").click()

# Вариант2 скачивание по ссылке
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    print(download_url)
    content = requests.get(url=download_url).content
    with open("tmp/readme2.rst", 'wb') as file:
        file.write(content)
    with open("tmp/readme2.rst") as file:
        file_content_str = file.read()
        assert "test_answer" in file_content_str

# Ждем 4 секунды (опционально)
    time.sleep(10)






import time
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Настройки браузера
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

# Кликаем кнопку "Raw"
browser.element("[data-testid='download-raw-button']").click()

# Ждем 4 секунды (опционально)
time.sleep(10)



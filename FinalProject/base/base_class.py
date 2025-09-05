from datetime import datetime
import os
from pathlib import Path

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод проверки url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий адрес страницы: " + get_url)

    """Метод проверки слова"""
    def asset_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Ключевое слово/фраза для проверки совпадает")

    """Метод создания скриншота"""
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #формат даты
        name_screenshot = f"Скриншот {now_date}.png" #имя файла + дата создания
        self.driver.save_screenshot(f"./screens/{name_screenshot}") #Сохранение скрина в опред папку
        print(f"Скриншот сохранён как: {name_screenshot}")

    """Метод проверки по url"""
    def asset_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Текущий адрес страницы совпадает с требуемым")

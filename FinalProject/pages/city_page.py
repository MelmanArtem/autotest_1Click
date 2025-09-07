import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger


class City_Page(Base):

    url = 'https://1click.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Выбор города"""

    # Locators - локаторы элементов, которые находятся на главной странице
    choice_city = "//a[@class='header__top-city-link js-city']"
    city_name = "//input[@class='form-control js-city-selector-input']"
    confirmation_city = "//a[@class='item js-set-city']"
    city_check = "//span[@class='header__top-city-link-name']"

    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.
    def get_choice_city(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.choice_city)))

    def get_city_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.city_name)))

    def get_confirmation_city(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.confirmation_city)))

    def get_city_check(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.city_check)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию.
    def click_choice_city(self):
        self.get_choice_city().click()
        time.sleep(1)
        print("Клик по полю ввода города")

    def input_city_name(self, city_name):
        self.get_city_name().send_keys(city_name)
        time.sleep(1)
        print("Ввод названия города")

    def click_confirmation_city(self):
        self.get_confirmation_city().click()
        time.sleep(1)
        print("Подтверждение введенного города")

    # Methods - метод, содержащий список Actions, представленных в виде действий данном случае осуществляется выбор города
    def city_choice(self):
        with allure.step("City choice"):
            Logger.add_start_step(method="city_choice")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_choice_city()
            self.input_city_name("москва")
            self.click_confirmation_city()
            self.asset_word(self.get_city_check(), "Москва") #Проверка, что введенный город выбрался
            Logger.add_end_step(url=self.driver.current_url, method="city_choice")



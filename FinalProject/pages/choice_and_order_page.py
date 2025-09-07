import allure
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger


class Order_Pay(Base):

    """Выбор продукта и заказ"""

    # Locators - локаторы элементов, которые находятся на главной странице
    dropdown = "//*[@id='content']/main/div[2]/div[2]/div[2]/div[1]/div/span"
    cheap_at_first = "(//a[@class='ui-dropdown__item'])[5]"
    buy_button = "(//button[@class='product__buy-basket'])[7]"
    confirm_order = "//a[@class='basket-small__btn btn btn-yellow']"
    input_name = "//input[@id='PROPS_NAME_ID']"
    input_last_name = "//input[@id='PROPS_LAST_NAME_ID']"
    input_tel_number = "//input[@id='PROPS_MOB_ID']"
    input_mail = "(//input[@id='PROPS_EMAIL_ID'])[1]"
    submit_order = "//button[@class='order__basket-total-btn btn btn-yellow d-none d-lg-flex order-add']"
    verification_word = "//a[@class='order-success__basket-item-name']"

    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.
    def get_dropdown(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.dropdown)))

    def get_cheap_at_first(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cheap_at_first)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_confirm_order(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.confirm_order)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_last_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.input_last_name)))

    def get_input_tel_number(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.input_tel_number)))

    def get_input_mail(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.input_mail)))

    def get_submit_order(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.submit_order)))

    def get_verification_word(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.verification_word)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию.
    def click_dropdown(self):
        self.get_dropdown().click()
        time.sleep(1)
        print("Клик по выпадающему списку")

    def click_cheap_at_first(self):
        self.get_cheap_at_first().click()
        time.sleep(1)
        print("Клик по категории 'Сначала дешевые'")

    def click_buy_button(self):
        self.get_buy_button().click()
        time.sleep(1)
        print("Клик по кнопке 'Купить'")

    def click_confirm_order(self):
        self.get_confirm_order().click()
        time.sleep(1)
        print("Клик по кнопке 'Оформить заказ'")

    def input_my_name(self):
        self.get_input_name().send_keys("Иван")
        time.sleep(1)
        print("Ввод имени")

    def input_my_last_name(self):
        self.get_input_last_name().send_keys("Иванов")
        time.sleep(1)
        print("Ввод фамилии")

    def input_number(self):
        self.get_input_tel_number().send_keys("9999999999")
        time.sleep(1)
        print("Ввод номера телефона")

    def input_email(self):
        self.get_input_mail().send_keys("mail@yandex.ru")
        print("Ввод электронной почты")

    def input_submit_order(self):
        self.get_submit_order().click()
        time.sleep(1)
        print("Оформление заказа")

    # Methods - метод, содержащий список Actions, представленных в виде действий данном случае осуществляется выбор города
    def choice_and_order(self):
        with allure.step("Choice and order"):
            Logger.add_start_step(method="choice_and_order")
            self.click_dropdown()
            self.click_cheap_at_first()
            self.click_buy_button()
            self.click_confirm_order()
            self.asset_url("https://1click.ru/order/")  # проверка, что перешел на страницу заказа
            self.input_my_name()
            self.input_my_last_name()
            self.input_number()
            self.input_email()
            self.input_submit_order()
            self.asset_word(self.get_verification_word(), "Google Pixel 9a 8/128Gb Peony (JP) Sim+eSim") #проверка на ключевую фразу
            self.get_screenshot() #скрин заказа
            Logger.add_end_step(url=self.driver.current_url, method="choice_and_order")
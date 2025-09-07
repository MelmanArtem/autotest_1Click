import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger


class Product_Find(Base):

    url = 'https://1click.ru/catalogue/phones/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Поиск продукта по фильтрам"""

    # Locators - локаторы элементов, которые находятся на главной странице
    catalog_items = "//div[@class='header__bottom-catalog']"
    smart_category = "(//div[@data-id='29'])[1]"
    available_only = "//label[@for='AVAILABLE']"
    price_value = "(//span[@class='irs-line'])[2]"
    brands = "(//a[@class='ui-filter__block-title js-title'])[2]"
    brand_google = "//label[@for='F_782562']"
    memory = "(//a[@class='ui-filter__block-title js-title'])[3]"
    memory_item_128 = "//label[@for='F_2bd451']"
    memory_item_256 = "//label[@for='F_12114d']"
    sim_card = "(//a[@class='ui-filter__block-title js-title'])[6]"
    nano_sim = "//label[@for='F_9c3b6a']"
    operating_system = "(//a[@class='ui-filter__block-title js-title'])[7]"
    android_system = "//label[@for='F_bfd92b']"
    operative_memory = "(//a[@class='ui-filter__block-title js-title'])[8]"
    six_gb_memory = "//label[@for='F_0097e5']"
    eight_gb_memory = "//label[@for='F_128f42']"
    nfc = "(//a[@class='ui-filter__block-title js-title'])[9]"
    nfc_yes = "//label[@for='F_7cb7c7']"
    accept_all = "//div[@class='ui-filter__result js-result']"
    verification_word = "//*[@id='content']/main/div[2]/div[1]/h1"

    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.
    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_items)))

    def get_smartphones(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.smart_category)))

    def get_availability(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.available_only)))

    def get_price_change(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_value)))

    def get_brands(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.brands)))

    def get_brand_google(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.brand_google)))

    def get_memory(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.memory)))

    def get_memory_item_128(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.memory_item_128)))

    def get_memory_item_256(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.memory_item_256)))

    def get_operating_system(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.operating_system)))

    def get_android_system(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.android_system)))

    def get_operative_memory(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.operative_memory)))

    def get_six_gb_memory(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.six_gb_memory)))

    def get_eight_gb_memory(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.eight_gb_memory)))

    def get_nfc(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.nfc)))

    def get_nfc_yes(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.nfc_yes)))

    def get_accept_all(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.accept_all)))

    def get_verification_word(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.verification_word)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию.
    def click_catalog(self):
        self.get_catalog().click()
        time.sleep(1)
        print("Клик по полю Каталог товаров")

    def click_smartphones_category(self):
        self.get_smartphones().click()
        time.sleep(1)
        print("Клик по категории Смартфоны")

    def click_availability(self):
        self.get_availability().click()
        time.sleep(1)
        print("Клик по чекбоксу 'Только в наличии'")

    def move_price_slider(self):
        slider = self.get_price_change()
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(20, 0).release().perform()
        time.sleep(1)
        print("Перемещение слайдера цены")

    def click_brands(self):
        self.get_brands().click()
        time.sleep(1)
        print("Клик по категории Бренды")

    def click_smartphone_google(self):
        self.get_brand_google().click()
        time.sleep(1)
        print("Клик по чекбоксу смартфонов Google")

    def click_memory(self):
        self.get_memory().click()
        time.sleep(1)
        print("Клик по категории Память")

    def click_memory_value_one(self):
        self.get_memory_item_128().click()
        time.sleep(1)
        print("Клик по чекбоксу памяти 128гб")

    def click_memory_value_two(self):
        self.get_memory_item_256().click()
        time.sleep(1)
        print("Клик по чекбоксу памяти 256гб")

    def click_operating_system(self):
        self.get_operating_system().click()
        time.sleep(1)
        print("Клик по категории Операционная система")

    def click_android_system(self):
        self.get_android_system().click()
        time.sleep(1)
        print("Клик по чекбоксу Андройд")

    def click_operative_memory(self):
        self.get_operative_memory().click()
        time.sleep(1)
        print("Клик по категории Оперативная память")

    def click_six_gb_memory(self):
        self.get_six_gb_memory().click()
        time.sleep(1)
        print("Клик по чекбоксу 6gb")

    def click_eight_gb_memory(self):
        self.get_eight_gb_memory().click()
        time.sleep(1)
        print("Клик по чекбоксу 8gb")

    def click_get_nfc(self):
        self.get_nfc().click()
        time.sleep(1)
        print("Клик по категории NFC")

    def click_get_nfc_yes(self):
        self.get_nfc_yes().click()
        time.sleep(1)
        print("Клик по чекбоксу nfc есть")

    def click_get_accept_all(self):
        self.get_accept_all().click()
        time.sleep(1)
        print("Клик по кнопке применения фильтров")

    # Methods - метод, содержащий список Actions, представленных в виде действий данном случае осуществляется выбор города
    def product_criteria(self):
        with allure.step("Product criteria"):
            Logger.add_start_step(method="product_criteria")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_catalog()
            self.click_smartphones_category()
            self.click_availability()
            self.move_price_slider()
            self.click_brands()
            self.click_smartphone_google()
            self.click_memory()
            self.click_memory_value_one()
            self.click_memory_value_two()
            self.click_operating_system()
            self.click_android_system()
            self.click_operative_memory()
            self.click_six_gb_memory()
            self.click_eight_gb_memory()
            self.click_get_nfc()
            self.click_get_nfc_yes()
            self.click_get_accept_all()
            self.asset_word(self.get_verification_word(), "Смартфоны в Москве") #проверка на ключевую фразу
            Logger.add_end_step(url=self.driver.current_url, method="product_criteria")



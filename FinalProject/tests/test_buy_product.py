from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.city_page import City_Page
from pages.product_find_page import Product_Find
from pages.choice_and_order_page import Order_Pay

def test_1(set_up, set_group): #тест с выбором города и отбором товара по критериям
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test")

    city = City_Page(driver)
    city.city_choice()

    selection = Product_Find(driver)
    selection.product_criteria()

    print("End test")
    driver.quit()

def test_2(set_up, set_group): #тест с отбором товара по критериям и заказом товара
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test")

    selection = Product_Find(driver)
    selection.product_criteria()

    order = Order_Pay(driver)
    order.choice_and_order()

    print("End test")
    driver.quit()

def test_3(set_up, set_group): #тест с выбором города, отбором товара по критериям и заказом товара
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start full test")

    city = City_Page(driver)
    city.city_choice()

    selection = Product_Find(driver)
    selection.product_criteria()

    order = Order_Pay(driver)
    order.choice_and_order()

    print("End full test")
    driver.quit()
import pytest

@pytest.fixture() #касается каждого теста
def set_up():
    print("Start test") #текст в начале теста
    yield #сам тест
    print("Finish test")  #текст в конце теста

@pytest.fixture(scope="module") #относится к группе тестов
def set_group():
    print("Enter system") #текст в начале группы тестов
    yield #группа тестов
    print("Exit system") #текст в конце группы тестов
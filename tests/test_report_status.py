import allure
import pytest


@allure.feature('Проверка статусов тестов')
def test_success():
    assert True


@allure.feature('Проверка статусов тестов')
def test_failure():
    assert False


@allure.feature('Проверка статусов тестов')
def test_skip():
    pytest.skip('...')


@allure.feature('Проверка статусов тестов')
def test_broken():
    raise Exception('Oops...')  # Raise для создания искусственной ошибки
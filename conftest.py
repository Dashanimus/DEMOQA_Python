from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000, height=600)
    yield driver
    driver.quit()

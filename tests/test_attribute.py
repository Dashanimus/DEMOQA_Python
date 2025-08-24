from pages.text_box import TextBox
import allure


@allure.feature('Check attribute')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    place = TextBox(browser)
    place.visit()
    assert place.full_name.get_dom_attribute('placeholder') == 'Full Name'

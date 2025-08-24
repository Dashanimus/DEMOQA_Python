from pages.text_box import TextBox
import time


def test_text_box(browser):
    tex_box = TextBox(browser)
    tex_box.visit()

    tex_box.full_name.send_keys('Scott Cawton')
    tex_box.current_address.send_keys('Houston')
    tex_box.btn_submit.click_force()
    time.sleep(2)

    assert tex_box.full_name_assert.get_text() == 'Name:Scott Cawton'
    assert tex_box.current_address_assert.get_text() == 'Current Address :Houston'

import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_availability_basket(browser):
    browser.get(link)
    time.sleep(10)
    button_text = 'Добавить в корзину'
    actual_button_text = browser.find_element_by_css_selector('.btn-add-to-basket').text
    assert button_text == actual_button_text, f"expected {button_text}, got {actual_button_text}"
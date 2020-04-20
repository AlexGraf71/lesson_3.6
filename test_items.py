import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_availability_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_text = 'Добавить в корзину'
    actual_button_text = browser.find_element_by_css_selector('.btn-add-to-basket').text
    assert button_text == actual_button_text
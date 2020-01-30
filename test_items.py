import time

import pytest
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    btn = browser.find_element_by_css_selector('button.btn-add-to-basket')
    assert btn

if __name__ == '__main__':
    pytest.main(['--language','ru'])
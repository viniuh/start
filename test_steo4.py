import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lis', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lis):
    link = f"https://stepik.org/lesson/{lis}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    inp = browser.find_element_by_css_selector(".ember-text-area")
    inp.send_keys(str(answer))
    sub = browser.find_element_by_css_selector(".submit-submission")
    sub.click()
    time.sleep(3)
    z = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert z == "Correct!", "Look at here!"

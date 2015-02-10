import yaml
import textwrap

from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import selenium.webdriver.support.ui as ui


driver = webdriver.Firefox()
driver.implicitly_wait(8)

docs = yaml.load(open('./page-elements/test.yml'))


@step ("I browse to '{url}'")
def step_impl(context, url):
    driver.get(url)
    # wait = ui.WebDriverWait(driver, 15)
    #
    # try:
    #     wait.until(lambda driver : driver.current_url.find(url) != -1)
    #     return True
    # except:
    #     log_fail(driver.current_url, url, "Page load timeout (15 sec).")
    #     return False

@step ("I browse to [{path}]")
def step_impl(context, path):
    url = get_selector_from_docs(docs, path)
    driver.get(url)


@step ("I enter '{value}' to ['{selector}']")
def step_impl(context, value, selector):
    element = driver.find_element_by_css_selector(selector)
    element.send_keys(value)


@step ("I click ['{selector}']")
def step_impl(context, selector):
    element = driver.find_element_by_css_selector(selector)
    element.click()


@step ("I see '{expect}' text in ['{selector}']")
def step_impl(context, expect, selector):
    element = driver.find_element_by_css_selector(selector)
    actual = element.text

    if expect not in actual:
        log_fail(actual, expect)


@step ("I see '{expect}' value in [{selector}]")
def step_impl(context, expect, selector):
    selector = get_selector(selector)
    element = find_element(selector)
    #element = driver.find_element_by_css_selector(selector)
    actual = element.get_attribute('value')

    if expect not in actual:
        log_fail(actual, expect)


def log_fail(actual, expect, message=""):
    content = """
    assertion fail
    actual: '%s'
    expect: '%s'
    error message: %s
    """ % (actual, expect, message)

    print(textwrap.dedent(content))
    raise AssertionError


def get_selector(selector):
    if selector.startswith("'") and selector.endswith("'"):
        selector = selector[1:-1]
    else:
        selector = get_selector_from_docs(docs, selector)
    return selector


def get_selector_from_docs(docs, selector):
    nodes = selector.split('.')
    for node in nodes:
        if node != nodes[-1]:
            docs = docs[node]
        else:
            selector = docs[node]
    return selector


def find_element(selector):
    print(selector)
    if selector.startswith('//'):
        element = driver.find_element_by_xpath(selector)
    else:
        element = driver.find_element_by_css_selector(selector)
    return element



# def wait_element(selector):
#     for n in range(0, 5 * 2):
#         element = driver.find_element_by_css_selector(selector)
#
#         if element is not None:
#             return True
#         time.sleep(0.5)
#
#     return False

import yaml

from behave import *
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select as to_select

from ..log import *
from ..world import *


@step ("I browse to '{url}'")
def step_impl(context, url):
    try:
        world.driver.get(url)
    except TimeoutException:
        log.fail(message="page load timeout")


@step ("I browse to [{ref}]")
def step_impl(context, ref):
    url = world.get_ref_value(ref)
    world.driver.get(url)


@step ("I enter '{value}' to [{ref}]")
def step_impl(context, value, ref):
    element = world.find_element(ref)
    element.send_keys(value)


@step ("I click [{ref}]")
def step_impl(context, ref):
    element = world.find_element(ref)
    try:
        element.click()
    except TimeoutException:
        log.fail(message="page load timeout")


@step ("I check [{ref}]")
def step_impl(context, ref):
    element = world.find_element(ref)
    if not element.is_selected():
        element.click()


@step ("I uncheck [{ref}]")
def step_impl(context, ref):
    element = world.find_element(ref)
    if element.is_selected():
        element.click()


@step ("I select '{text}' text in [{ref}]")
def step_impl(context, text, ref):
    element = world.find_element(ref)
    try:
        to_select(element).select_by_visible_text(text)
    except NoSuchElementException:
        log.fail(message="not found option with text '%s'" % text)


@step ("I select '{value}' value in [{ref}]")
def step_impl(context, value, ref):
    element = world.find_element(ref)
    try:
        to_select(element).select_by_value(value)
    except NoSuchElementException:
        log.fail(message="not found option with value '%s'" % value)


### checking ###

@step ("I see browser url contains '{expect}'")
def step_impl(context, expect):
    actual = world.driver.current_url
    if expect not in actual:
        log.fail(actual, expect)


@step ("I see {count} items of [{ref}]")
def step_impl(context, count, ref):
    elements = world.find_elements(ref)
    actual = len(elements)
    expect = int(count)

    if actual != expect:
        log.fail(actual, expect)


@step ("I see [{ref}] text not contains '{expect}'")
def step_impl(context, ref, expect):
    element = world.find_element(ref)
    actual = element.text

    if expect in actual:
        log.fail(actual, expect)


@step ("I see [{ref}] text contains '{expect}'")
def step_impl(context, ref, expect):
    element = world.find_element(ref)
    actual = element.text

    if expect not in actual:
        log.fail(actual, expect)


@step ("I see [{ref}] @{attr} not contains '{expect}'")
def step_impl(context, ref, attr, expect):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if expect in actual:
        log.fail(actual, expect)


@step ("I see [{ref}] @{attr} contains '{expect}'")
def step_impl(context, ref, attr, expect):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if expect not in actual:
        log.fail(actual, expect)


@step ("I see [{ref}] text is empty")
def step_impl(context, ref):
    element = world.find_element(ref)
    actual = element.text

    if actual != "":
        log.fail(actual)


@step ("I see [{ref}] @{attr} is empty")
def step_impl(context, ref, attr):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if actual != "":
        log.fail(actual)


@step ("I see [{ref}] is checked")
@step ("I see [{ref}] is selected")
def step_impl(context, ref):
    element = world.find_element(ref)
    if not element.is_selected():
        log.fail('unchecked', 'checked')


@step ("I see [{ref}] is unchecked")
@step ("I see [{ref}] is not selected")
def step_impl(context, ref):
    element = world.find_element(ref)
    if element.is_selected():
        log.fail('checked', 'unchecked')

import yaml

from behave import *
from ..world import *


@step ("I browse to '{url}'")
def step_impl(context, url):
    world.driver.get(url)


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
    element.click()


@step ("I see browser url contains '{expect}'")
def step_impl(context, expect):
    actual = world.driver.current_url
    if expect not in actual:
        world.log_fail(actual, expect)


@step ("I see [{ref}] text contains '{expect}'")
def step_impl(context, ref, expect):
    element = world.find_element(ref)
    actual = element.text

    if expect not in actual:
        world.log_fail(actual, expect)


@step ("I see [{ref}] @{attr} not contains '{expect}'")
def step_impl(context, ref, attr, expect):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if expect in actual:
        world.log_fail(actual, expect)


@step ("I see [{ref}] @{attr} contains '{expect}'")
def step_impl(context, ref, attr, expect):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if expect not in actual:
        world.log_fail(actual, expect)


@step ("I see [{ref}] @{attr} is empty")
def step_impl(context, ref, attr):
    element = world.find_element(ref)
    actual = element.get_attribute(attr)

    if actual != "":
        world.log_fail(actual)

from .world import *
from .steps.basic import *


def before_all(context):
    world.load_elements('./repositories/*.yml')

def before_feature(context, feature):
    world.open_browser()

def after_feature(context, feature):
    world.close_browser()

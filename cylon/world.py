import glob
import yaml

from selenium import webdriver


class world:
    driver = None
    refs = None

    @classmethod
    def open_browser(cls, browser="firefox"):
        if browser == "chrome":
            cls.driver = webdriver.Chrome()
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        else:
            print("The '%s' browser is not supported." % browser)
            return

        cls.driver.implicitly_wait(8)
        cls.driver.set_page_load_timeout(15)


    @classmethod
    def close_browser(cls):
        if cls.driver is None:
            return
        for handle in cls.driver.window_handles:
            cls.driver.switch_to_window(handle)
            cls.driver.close()


    @classmethod
    def load_elements(cls, files):
        cls.refs = {}
        for filename in glob.glob(files):
            doc = yaml.load(open(filename))
            cls.refs.update(doc)


    @classmethod
    def find_element(cls, ref):
        selector = cls.get_ref_value(ref)

        if selector.startswith('//'):
            element = cls.driver.find_element_by_xpath(selector)
        else:
            element = cls.driver.find_element_by_css_selector(selector)

        return element


    @classmethod
    def get_ref_value(cls, ref):
        if ref.startswith("'") and ref.endswith("'"):
            value = ref[1:-1]
        else:
            nodes = ref.split('.')
            refs = cls.refs

            for node in nodes:
                if node != nodes[-1]:
                    refs = refs[node]
                else:
                    value = refs[node]
        return value


    @classmethod
    def log_fail(cls, actual="", expect="", message=""):
        content = ""

        if actual or expect:
            content = "actual: '%s' \nexpect: '%s'" % (actual, expect)
        if message:
            content += "\nmessage: %s" % (message)

        print(content)
        raise AssertionError

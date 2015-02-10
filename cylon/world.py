from selenium import webdriver

class world:
    driver = None

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

    @classmethod
    def close_browser(cls):
        if cls.driver is None:
            return
        for handle in cls.driver.window_handles:
            cls.driver.switch_to_window(handle)
            cls.driver.close()

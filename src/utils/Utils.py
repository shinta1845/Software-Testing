from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Utils:
    browser = None
    url = None
    driver = None

    @classmethod
    def getDriver(cls, browser, url):
        cls.browser = browser
        cls.url = url
        if cls.browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome(service=service)
        elif cls.browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            cls.driver = webdriver.Firefox(service=service)
        elif cls.browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            cls.driver = webdriver.Edge(service=service)
        else:
            raise Exception("Browser is not supported")
        # cls.driver.set_window_size(1920, 1080)
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

class SeleniumDriver():
    _driver: WebDriver
    
    def init(self):
        self._driver = webdriver.Chrome(options=self.get_options())
        return self._driver
        
    def get_options(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("incognito")
        return options
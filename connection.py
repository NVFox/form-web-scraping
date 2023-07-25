from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from google import GoogleHelper

class GoogleConnection():
    _helper: GoogleHelper
    
    def __init__(self, helper: GoogleHelper) -> None:
        self._helper = helper
        
    def init(self):
        self._helper.log_in()
        
    def get(self, url: str):
        driver = self._helper._driver
        driver.get(url)
        
        try:
            WebDriverWait(driver, 3).until_not(EC.url_contains("signin"))
        except TimeoutException:
            self.init()
            
        return driver
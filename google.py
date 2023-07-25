from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

class GoogleCredentials():
    _email: str
    _password: str
    
    def __init__(self, email: str, password: str) -> None:
        self._email = email
        self._password = password

class GoogleHelper():
    _driver: WebDriver
    _credentials: GoogleCredentials
    
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        
    def set_credentials(self, credentials: GoogleCredentials):
        self._credentials = credentials
        
    def log_in(self):
        username = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
        username.clear()
        username.send_keys(self._credentials._email)
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[./span = 'Siguiente']"))).click()

        user_password = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
        user_password.clear()
        user_password.send_keys(self._credentials._password)
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[./span = 'Siguiente']"))).click()
        
        WebDriverWait(self._driver, 120).until_not(EC.url_contains("signin"))
        

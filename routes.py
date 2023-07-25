from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from typing import List

class RouteScraper():
    _driver: WebDriver
    
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
    
    def get_route(self):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.meR3Qc")))
        
        title_container = self._driver.find_element(By.CLASS_NAME, "T4tcpe")
        title_names = title_container.find_elements(By.CLASS_NAME, "YVvGBb")
        
        names = [title.text for title in title_names]
        
        return {
            "name": names[0],
            "chapter": names[1].upper().replace("CHAPTER", "").strip()
        }
    
    def get_story_forms(self) -> List[WebElement]: 
        tab_menu = self._driver.find_element(By.CSS_SELECTOR, "div.meR3Qc")
        tab_menu.find_element(By.CSS_SELECTOR, "a[guidedhelpid='classworkTab']").click()
        
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Tema Seguimiento']")))
        
        return self._driver.find_elements(By.XPATH, "//div[contains(@aria-label, 'Tema Seguimiento')]/descendant::li")
        
class KnowledgeScraper():
    _driver: WebDriver
    
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        
    def get_knowledge(self, container: WebElement):
        knowledge_container = container.find_element(By.CSS_SELECTOR, ".ssX1Bd.KZt9Tc")
        knowledge = knowledge_container.find_elements(By.CLASS_NAME, "OIC90c")
        
        return [element.text for element in knowledge]

class StoryScraper():
    _driver: WebDriver
    _knowledge_scrapper: KnowledgeScraper
    
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._knowledge_scrapper = KnowledgeScraper(driver)
    
    def get_stories(self):
        story_containers = self._driver.find_elements(By.XPATH, "//div[contains(@class, 'ufh7vf')]/ancestor::div[contains(@role, 'listitem')]")
        user_stories = []
        
        for container in story_containers:
            name = container.find_element(By.CLASS_NAME, "M7eMe").text
            story_type = container.find_element(By.CSS_SELECTOR, ".wzWPxe.OIC90c").text
            knowledge_names = self._knowledge_scrapper.get_knowledge(container)

            user_stories.append({
                "name": name + " [" + story_type + "]",
                "knowledge": [{"name": name} for name in knowledge_names]
            })
        
        return user_stories
from connection import GoogleConnection, EC
from drivers import SeleniumDriver, WebDriver
from google import GoogleCredentials, GoogleHelper, WebDriverWait
from routes import StoryScraper, WebElement, By

from typing import List

class RouteService():
    _driver: WebDriver
    
    def __init__(self, url: str) -> None:
        self._driver = self.connect_to_form(url)        
    
    def connect_to_form(self, url: str):
        setup = SeleniumDriver()
        
        google_helper = GoogleHelper(setup.init())
        google_helper.set_credentials(GoogleCredentials("andres.tellez@pragma.com.co", "PRA2415david"))
        
        connection = GoogleConnection(google_helper)
        return connection.get(url)

    def get_route_from_forms(self, prev: dict):
        story_scraper = StoryScraper(self._driver)

        return {
            "name": prev["name"],
            "chapter": prev["chapter"],
            "userStories": [{"name": story["name"] + f"[{prev['chapter']}]", 
                             "knowledge": story["knowledge"]} for story in story_scraper.get_stories()]
        }

    def get_final_routes(self, route: dict, prev: List[WebElement]):
        routes = []

        for form in prev:
            windows_len = len(self._driver.window_handles)

            form.click()
            WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
                "//li[contains(@class, 'lXuxY')]/descendant::a[contains(@href, 'docs') and contains(@class, 'maXJsd')]"))).click()

            WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(windows_len + 1))
            self._driver.switch_to.window(self._driver.window_handles[len(self._driver.window_handles) - 1])

            routes.append(self.get_route_from_forms(route))

            self._driver.close()
            WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(1))
            self._driver.switch_to.window(self._driver.window_handles[0])

        return routes

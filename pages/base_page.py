from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    # Базовая страница
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Увеличенный таймаут ожидания

    # Дождаться загрузки страницы
    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self):
        # Ждем пока страница полностью загрузится
        # Ждем, пока документ будет готов (состояние readyState равно 'complete')
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        try:
            # Ждем пока будет доступен элемент с id="root"
            self.wait.until(EC.presence_of_element_located(("id", "root")))
        except TimeoutException:
            pass  # Продолжаем даже если элемент не найден

    # Найти элемент
    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator):
        self.wait_for_page_load()
        return self.wait.until(EC.presence_of_element_located(locator))

    # Кликнуть по элементу
    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Получить текст элемента
    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        self.wait_for_page_load()
        element = self.find_element(locator)
        return element.text
        
    # Найти несколько элементов
    @allure.step("Поиск нескольких элементов {locator}")
    def find_elements(self, locator):
        self.wait_for_page_load()
        return self.driver.find_elements(*locator)
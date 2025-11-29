from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    # Базовая страница
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Увеличенный таймаут ожидания

    # Дождаться загрузки страницы
    def wait_for_page_load(self):
        # Ждем пока страница полностью загрузится
        time.sleep(2)  # Небольшая пауза для загрузки JS
        try:
            # Ждем пока будет доступен элемент с id="root"
            self.wait.until(EC.presence_of_element_located(("id", "root")))
        except TimeoutException:
            pass  # Продолжаем даже если элемент не найден

    # Найти элемент
    def find_element(self, locator):
        self.wait_for_page_load()
        return self.wait.until(EC.presence_of_element_located(locator))

    # Кликнуть по элементу
    def click_element(self, locator):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Получить текст элемента
    def get_text(self, locator):
        self.wait_for_page_load()
        element = self.find_element(locator)
        return element.text
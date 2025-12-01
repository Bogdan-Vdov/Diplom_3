from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
from pages.components.navigation import NavigationComponent
import allure

class MainPage(BasePage):
    # Элементы главной страницы
    # Выбираем конкретный ингредиент для тестов
    INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/following-sibling::p")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='close' or @class='Modal_modal__close__button']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/"
        # Создаем экземпляр NavigationComponent
        self.navigation = NavigationComponent(driver)
        
    # Открыть страницу
    @allure.step("Открытие главной страницы")
    def open(self):
        self.driver.get(self.url)
        # Ждем загрузки страницы
        self.wait_for_page_load()
        
    # Клик по конструктору
    @allure.step("Клик по ссылке 'Конструктор'")
    def click_constructor(self):
        self.navigation.click_constructor()
        
    # Клик по ленте заказов
    @allure.step("Клик по ссылке 'Лента заказов'")
    def click_order_feed(self):
        self.navigation.click_order_feed()
        
    # Клик по ингредиенту
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(self.INGREDIENT)
        
    # Закрыть модальное окно
    @allure.step("Закрытие модального окна")
    def close_modal(self):
        try:
            self.click_element(self.MODAL_CLOSE_BUTTON)
        except (TimeoutException, NoSuchElementException):
            # Если кнопка закрытия не найдена, пробуем закрыть ESC
            try:
                from selenium.webdriver.common.keys import Keys
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            except:
                pass  # Игнорируем ошибки закрытия
        
    # Получить счетчик ингредиента
    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        try:
            counter_text = self.get_text(self.INGREDIENT_COUNTER)
            # Пытаемся преобразовать в число, если это возможно
            try:
                return int(counter_text)
            except ValueError:
                return counter_text
        except (TimeoutException, NoSuchElementException) as e:
            # Возвращаем значение по умолчанию
            return 0
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.navigation import NavigationComponent

class MainPage(BasePage):
    # Элементы главной страницы
    # Выбираем конкретный ингредиент для тестов
    INGREDIENT = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]/following-sibling::p[1]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')] | //button[@class='close']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/"
        # Создаем экземпляр NavigationComponent
        self.navigation = NavigationComponent(driver)
        
    # Открыть страницу
    def open(self):
        self.driver.get(self.url)
        # Ждем загрузки страницы
        self.wait_for_page_load()
        
    # Клик по конструктору
    def click_constructor(self):
        self.navigation.click_constructor()
        
    # Клик по ленте заказов
    def click_order_feed(self):
        self.navigation.click_order_feed()
        
    # Клик по ингредиенту
    def click_ingredient(self):
        self.click_element(self.INGREDIENT)
        
    # Закрыть модальное окно
    def close_modal(self):
        self.click_element(self.MODAL_CLOSE_BUTTON)
        
    # Получить счетчик ингредиента
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
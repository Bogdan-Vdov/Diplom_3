from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NavigationComponent(BasePage):
    """
    Компонент навигации.
    """
    # Элементы навигации
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента') and contains(text(),'заказов')]")
    
    # Клик по конструктору
    def click_constructor(self):
        self.click_element(self.CONSTRUCTOR_LINK)
        
    # Клик по ленте заказов
    def click_order_feed(self):
        self.click_element(self.ORDER_FEED_LINK)
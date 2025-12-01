from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
import allure

class NavigationComponent(BasePage):
    """
    Компонент навигации.
    """
    # Элементы навигации
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента заказов']")
    
    # Клик по конструктору
    @allure.step("Клик по ссылке 'Конструктор' в навигации")
    def click_constructor(self):
        self.click_element(self.CONSTRUCTOR_LINK)
        
    # Клик по ленте заказов
    @allure.step("Клик по ссылке 'Лента заказов' в навигации")
    def click_order_feed(self):
        self.click_element(self.ORDER_FEED_LINK)
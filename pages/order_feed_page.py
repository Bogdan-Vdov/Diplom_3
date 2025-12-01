from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
import allure

class OrderFeedPage(BasePage):
    # Элементы страницы ленты заказов
    ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Список заказов в работе
    ORDER_IN_WORK = (By.XPATH, "//ul[@class='OrderFeed_orderList__ready']//li | //ul[@class='OrderFeed_orderList__inWork']//li")
    
    # Счетчик за всё время
    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        # Возможно, нужно добавить обработку ошибок
        try:
            return int(self.get_text(self.ALL_TIME_COUNTER))
        except (TimeoutException, NoSuchElementException, ValueError):
            return 0
        
    # Счетчик за сегодня
    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        # Возможно, нужно добавить обработку ошибок
        try:
            return int(self.get_text(self.TODAY_COUNTER))
        except (TimeoutException, NoSuchElementException, ValueError):
            return 0
        
    # Заказы в работе
    @allure.step("Получение списка заказов в работе")
    def get_orders_in_work(self):
        elements = self.driver.find_elements(*self.ORDER_IN_WORK)
        # TODO: Добавить фильтрацию заказов
        return [element.text for element in elements]
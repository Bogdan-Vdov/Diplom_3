from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    # Элементы страницы ленты заказов
    ALL_TIME_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за всё время:')]/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::p")
    # Список заказов в работе
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__')]//li | //div[@class='order-list']//li")
    
    # Счетчик за всё время
    def get_all_time_counter(self):
        # Возможно, нужно добавить обработку ошибок
        return int(self.get_text(self.ALL_TIME_COUNTER))
        
    # Счетчик за сегодня
    def get_today_counter(self):
        # Возможно, нужно добавить обработку ошибок
        return int(self.get_text(self.TODAY_COUNTER))
        
    # Заказы в работе
    def get_orders_in_work(self):
        elements = self.driver.find_elements(*self.ORDER_IN_WORK)
        # TODO: Добавить фильтрацию заказов
        return [element.text for element in elements]
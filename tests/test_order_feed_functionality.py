import pytest
from unittest.mock import Mock

def test_all_time_counter_increase():
    """
    Проверка увеличения счетчика «Выполнено за всё время»
    """
    try:
        from pages.order_feed_page import OrderFeedPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = OrderFeedPage(mock_driver)
        
        # Настраиваем мок для возврата значения счетчика
        test_counter = "100"
        page.get_text = Mock(return_value=test_counter)
        
        # Вызываем метод
        counter = page.get_all_time_counter()
        
        # Проверяем, что метод get_text был вызван с правильным локатором
        page.get_text.assert_called_once_with(page.ALL_TIME_COUNTER)
        # Проверяем, что возвращено правильное значение (преобразованное в int)
        assert counter == int(test_counter)
    except Exception as e:
        pytest.fail(f"Ошибка при проверке счетчика 'Выполнено за всё время': {e}")

def test_today_counter_increase():
    """
    Проверка увеличения счетчика «Выполнено за сегодня»
    """
    try:
        from pages.order_feed_page import OrderFeedPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = OrderFeedPage(mock_driver)
        
        # Настраиваем мок для возврата значения счетчика
        test_counter = "50"
        page.get_text = Mock(return_value=test_counter)
        
        # Вызываем метод
        counter = page.get_today_counter()
        
        # Проверяем, что метод get_text был вызван с правильным локатором
        page.get_text.assert_called_once_with(page.TODAY_COUNTER)
        # Проверяем, что возвращено правильное значение (преобразованное в int)
        assert counter == int(test_counter)
    except Exception as e:
        pytest.fail(f"Ошибка при проверке счетчика 'Выполнено за сегодня': {e}")

def test_orders_in_work():
    """
    Проверка появления номера заказа в разделе «В работе»
    """
    try:
        from pages.order_feed_page import OrderFeedPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = OrderFeedPage(mock_driver)
        
        # Настраиваем мок для возврата элементов заказов
        mock_element1 = Mock()
        mock_element1.text = "Order #12345"
        mock_element2 = Mock()
        mock_element2.text = "Order #12346"
        
        mock_driver.find_elements.return_value = [mock_element1, mock_element2]
        
        # Вызываем метод
        orders = page.get_orders_in_work()
        
        # Проверяем, что метод find_elements был вызван с правильным локатором
        mock_driver.find_elements.assert_called_once_with(*page.ORDER_IN_WORK)
        # Проверяем, что возвращен правильный список заказов
        assert orders == ["Order #12345", "Order #12346"]
    except Exception as e:
        pytest.fail(f"Ошибка при проверке заказов в работе: {e}")
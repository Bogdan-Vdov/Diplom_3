import pytest
import requests
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.suite("Заказы")
class TestOrders:
    """Тесты функциональности заказов"""
    
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    def setup_method(self):
        """Подготовка к тесту - получение ингредиентов"""
        # Получаем список ингредиентов
        response = requests.get(f"{self.BASE_URL}/ingredients")
        assert response.status_code == 200
        self.ingredients = response.json()["data"]
    
    @allure.story("Создание заказа")
    @allure.title("Попытка создания заказа неавторизованным пользователем")
    def test_create_order_unauthorized(self):
        """Проверка, что неавторизованный пользователь не может создать заказ"""
        # Берем первые два ингредиента для создания заказа
        if len(self.ingredients) >= 2:
            ingredient_ids = [self.ingredients[0]["_id"], self.ingredients[1]["_id"]]
            
            # Пытаемся создать заказ без авторизации
            response = requests.post(
                f"{self.BASE_URL}/orders",
                json={
                    "ingredients": ingredient_ids
                }
            )
            
            # Проверяем, что получили ошибку 401
            assert response.status_code == 401
            response_data = response.json()
            assert response_data["success"] is False
            assert "You should be authorised" in response_data["message"]
    
    @allure.story("Создание заказа")
    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_authorized(self):
        """Проверка успешного создания заказа авторизованным пользователем"""
        # Сначала регистрируем пользователя
        import time
        email = f"test_order_user_{int(time.time())}@example.com"
        password = "password123"
        name = "Test Order User"
        
        # Регистрация
        reg_response = requests.post(
            f"{self.BASE_URL}/auth/register",
            json={
                "email": email,
                "password": password,
                "name": name
            }
        )
        
        assert reg_response.status_code == 200
        reg_data = reg_response.json()
        
        # Авторизация
        login_response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )
        
        assert login_response.status_code == 200
        login_data = login_response.json()
        access_token = login_data["accessToken"]
        
        # Берем первые два ингредиента для создания заказа
        if len(self.ingredients) >= 2:
            ingredient_ids = [self.ingredients[0]["_id"], self.ingredients[1]["_id"]]
            
            # Создаем заказ с авторизацией
            response = requests.post(
                f"{self.BASE_URL}/orders",
                headers={
                    "Authorization": access_token
                },
                json={
                    "ingredients": ingredient_ids
                }
            )
            
            # Проверяем успешность создания заказа
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
            assert "order" in response_data
            assert "number" in response_data["order"]
    
    @allure.story("Лента заказов")
    @allure.title("Получение общей ленты заказов")
    def test_get_all_orders_feed(self):
        """Проверка получения общей ленты заказов"""
        response = requests.get(f"{self.BASE_URL}/orders/all")
        
        # Проверяем успешность получения ленты заказов
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert "orders" in response_data
        assert "total" in response_data
        assert "totalToday" in response_data
    
    @allure.story("Лента заказов")
    @allure.title("Получение ленты заказов пользователя")
    def test_get_user_orders_feed(self):
        """Проверка получения ленты заказов пользователя"""
        # Сначала регистрируем и авторизуем пользователя
        import time
        email = f"test_orders_user_{int(time.time())}@example.com"
        password = "password123"
        name = "Test Orders User"
        
        # Регистрация
        reg_response = requests.post(
            f"{self.BASE_URL}/auth/register",
            json={
                "email": email,
                "password": password,
                "name": name
            }
        )
        
        assert reg_response.status_code == 200
        
        # Авторизация
        login_response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )
        
        assert login_response.status_code == 200
        login_data = login_response.json()
        access_token = login_data["accessToken"]
        
        # Получаем ленту заказов пользователя
        response = requests.get(
            f"{self.BASE_URL}/orders",
            headers={
                "Authorization": access_token
            }
        )
        
        # Проверяем успешность получения ленты заказов
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert "orders" in response_data
        assert "total" in response_data
        assert "totalToday" in response_data
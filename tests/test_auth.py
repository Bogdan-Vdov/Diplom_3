import pytest
import requests
import allure
from pages.main_page import MainPage


@allure.suite("Авторизация")
class TestAuth:
    """Тесты функциональности авторизации"""
    
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    @allure.story("Регистрация")
    @allure.title("Успешная регистрация нового пользователя")
    def test_successful_registration(self):
        """Проверка успешной регистрации нового пользователя"""
        # Генерируем уникальный email для теста
        import time
        email = f"test_user_{int(time.time())}@example.com"
        password = "password123"
        name = "Test User"
        
        # Отправляем запрос на регистрацию
        response = requests.post(
            f"{self.BASE_URL}/auth/register",
            json={
                "email": email,
                "password": password,
                "name": name
            }
        )
        
        # Проверяем успешность регистрации
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert "accessToken" in response_data
        assert "refreshToken" in response_data
        assert response_data["user"]["email"] == email
        assert response_data["user"]["name"] == name
    
    @allure.story("Авторизация")
    @allure.title("Успешная авторизация пользователя")
    def test_successful_login(self):
        """Проверка успешной авторизации пользователя"""
        # Сначала регистрируем пользователя
        import time
        email = f"test_user_login_{int(time.time())}@example.com"
        password = "password123"
        name = "Test User"
        
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
        
        # Затем авторизуемся
        login_response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )
        
        # Проверяем успешность авторизации
        assert login_response.status_code == 200
        response_data = login_response.json()
        assert response_data["success"] is True
        assert "accessToken" in response_data
        assert "refreshToken" in response_data
        assert response_data["user"]["email"] == email
        assert response_data["user"]["name"] == name
    
    @allure.story("Авторизация")
    @allure.title("Попытка авторизации с неверными данными")
    def test_failed_login(self):
        """Проверка авторизации с неверными данными"""
        response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json={
                "email": "wrong@example.com",
                "password": "wrongpassword"
            }
        )
        
        # Проверяем, что авторизация не удалась
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False
        assert "email or password are incorrect" in response_data["message"]
    
    @allure.story("Выход из системы")
    @allure.title("Успешный выход из системы")
    def test_successful_logout(self):
        """Проверка успешного выхода из системы"""
        # Сначала регистрируем и авторизуем пользователя
        import time
        email = f"test_user_logout_{int(time.time())}@example.com"
        password = "password123"
        name = "Test User"
        
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
        
        # Выход из системы
        logout_response = requests.post(
            f"{self.BASE_URL}/auth/logout",
            json={
                "token": login_data["refreshToken"]
            }
        )
        
        # Проверяем успешность выхода
        assert logout_response.status_code == 200
        response_data = logout_response.json()
        assert response_data["success"] is True
        assert "Successful logout" in response_data["message"]
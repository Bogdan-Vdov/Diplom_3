#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт для запуска тестов.
"""

import subprocess
import sys
import os

def run_tests():
    # Запуск тестов с генерацией Allure-отчета
    try:
        # Запускаем тесты
        result = subprocess.run([sys.executable, '-m', 'pytest', '--alluredir=allure-results'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return result.returncode
    except Exception as e:
        print(f"Ошибка при запуске тестов: {e}", file=sys.stderr)
        return 1

def generate_allure_report():
    # Генерация Allure-отчета
    try:
        # Проверяем, установлен ли Allure
        result = subprocess.run(['allure', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Allure установлен, генерируем отчет
            print("Генерация Allure-отчета...")
            subprocess.run(['allure', 'serve', 'allure-results'])
        else:
            print("Allure не установлен. Пропускаем генерацию отчета.")
            print("Для установки Allure следуйте инструкциям на официальном сайте.")
    except FileNotFoundError:
        print("Allure не найден в системе. Пропускаем генерацию отчета.")
        print("Для установки Allure следуйте инструкциям на официальном сайте.")
    except Exception as e:
        print(f"Ошибка при генерации Allure-отчета: {e}", file=sys.stderr)

def main():
    # Основная функция
    print("Запуск тестов...")
    exit_code = run_tests()
    
    if exit_code == 0:
        print("Тесты успешно завершены.")
        # Предлагаем сгенерировать отчет
        generate_report = input("Сгенерировать Allure-отчет? (y/n): ").lower().strip()
        if generate_report in ['y', 'yes', 'да']:
            generate_allure_report()
    else:
        print("Тесты завершены с ошибками.", file=sys.stderr)
    
    return exit_code

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
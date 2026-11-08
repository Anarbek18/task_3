# Автотесты Stellar Burgers

Стек: Python, Selenium, pytest, Allure. Паттерн: Page Object Model.

## Запуск
```
pip install -r requirements.txt
pytest
allure serve allure_results
allure generate allure_results -o allure_report --clean
```
Тесты автоматически запускаются в Chrome и Firefox.

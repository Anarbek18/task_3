import uuid

import allure
import requests

import config


@allure.step("Создать пользователя через API")
def create_user():
    suffix = uuid.uuid4().hex[:10]
    payload = {
        "email": f"burger_{suffix}@example.com",
        "password": "Password123",
        "name": f"user_{suffix}",
    }
    response = requests.post(config.API_REGISTER, json=payload)
    response.raise_for_status()
    payload["token"] = response.json()["accessToken"]
    return payload


@allure.step("Удалить пользователя через API")
def delete_user(token):
    requests.delete(config.API_USER, headers={"Authorization": token})


@allure.step("Создать заказ через API")
def create_order(token):
    ingredients = requests.get(config.API_INGREDIENTS).json()["data"]
    bun = next(item["_id"] for item in ingredients if item["type"] == "bun")
    main = next(item["_id"] for item in ingredients if item["type"] == "main")
    response = requests.post(
        config.API_ORDERS,
        json={"ingredients": [bun, main, bun]},
        headers={"Authorization": token},
    )
    response.raise_for_status()
    return response.json()["order"]["number"]

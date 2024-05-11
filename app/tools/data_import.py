import json

from app.cls.car import Car
from app.cls.customer import Customer
from app.cls.shop import Shop


def data_import() -> tuple[list[Customer], list[Shop], float]:
    with open("app/config.json", "r") as conf:
        data = json.load(conf)

    for customer in data["customers"]:
        customer["car"] = Car(*customer["car"].values())

    customers = [Customer(*customer.values())
                 for customer in data["customers"]]

    shops = [Shop(*shop.values()) for shop in data["shops"]]
    return customers, shops, data["FUEL_PRICE"]

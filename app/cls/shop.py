from app.cls.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict = None
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def distance_to_customer(self, customer: Customer) -> float:
        return (
            (customer.location[0] - self.location[0]) ** 2
            + (customer.location[1] - self.location[1]) ** 2
        ) ** 0.5

    def calc_shop_path(
            self,
            customer: Customer,
            fuel_price: float
    ) -> float:
        distance = self.distance_to_customer(customer)
        price = distance / 100 * customer.car.fuel_consumption * fuel_price * 2
        return round(price, 2)

    def calc_cost_cart(self, customer: Customer) -> float:
        return round(
            sum(
                [self.products[product] * customer.product_cart[product]
                 for product in customer.product_cart]
            )
            , 2
        )

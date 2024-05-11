import datetime

from app.tools.data_import import data_import
from app.tools.shop_proposals import propose


def shop_trip() -> None:
    customers, shops, fuel_price = data_import()

    for customer in customers:
        customer.print_has_money()

        best_shop, path_price, bill = propose(customer, shops, fuel_price)

        if customer.money >= path_price + bill:
            print(f"{customer.name} rides to {best_shop.name}\n")
            home_location = customer.location.copy()
            customer.location = best_shop.location

            date = datetime.datetime.now()
            print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():

                print(f"{quantity} {product}s for"
                      f"{quantity * best_shop.products[product]: g} dollars")

            print(f"Total cost is {bill} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has "
                  f"{customer.money - bill - path_price} dollars\n")

        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")

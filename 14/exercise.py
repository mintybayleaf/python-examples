import sys

MENU = {
    "Sandwich": 10,
    "Burger": 20,
    "Steak": 35,
    "Burrito": 12,
    "Risotto": 15
}

def resturant():
    total = 0
    while order := input("Order: "):
        if order.strip():
            menu_item = MENU.get(order, None)
            if menu_item:
                total += menu_item
                print(f"{order} costs {menu_item}, total is {total}")
            else:
                print(f"we are freshn out of {order} today!")

    print(f"your total is {total}")

if __name__ == "__main__":
    resturant()
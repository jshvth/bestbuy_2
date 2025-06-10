import products
import store
import promotions

def display_menu():
    """Displays the store menu."""
    print("\n   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def list_products(store_instance):
    """Prints all active products."""
    print("------")
    for idx, product in enumerate(store_instance.get_all_products(), start=1):
        print(f"{idx}. {product.show()}")
    print("------")

def show_total_quantity(store_instance):
    """Displays the total quantity of items in the store."""
    total = store_instance.get_total_quantity()
    print(f"\nTotal of {total} items in store")

def make_order(store_instance):
    """Handles the ordering process from the store."""
    active_products = store_instance.get_all_products()
    list_products(store_instance)

    shopping_list = []
    while True:
        product_input = input("Which product # do you want?  ").strip()
        if product_input == "":
            break

        if not product_input.isdigit():
            print("Please enter a valid product number.")
            continue

        prod_index = int(product_input) - 1
        if prod_index < 0 or prod_index >= len(active_products):
            print("Invalid product number.")
            continue

        quantity_input = input("What amount do you want? ").strip()
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Please enter a valid positive quantity.")
            continue

        quantity = int(quantity_input)
        shopping_list.append((active_products[prod_index], quantity))
        print("Product added to list!")

    if shopping_list:
        try:
            total_price = store_instance.order(shopping_list)
            print(f"Order completed! Total price: ${total_price}")
        except Exception as e:
            print(f"Error processing order: {e}")

def start(store_instance):
    """Starts the store interface loop."""
    while True:
        display_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store_instance)
        elif choice == "2":
            show_total_quantity(store_instance)
        elif choice == "3":
            make_order(store_instance)
        elif choice == "4":
            print("Thank you for visiting Best Buy! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")

if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Promotions zuweisen
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)

import sys

if __name__ == '__main__':
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        values = arg.split(':')
        if len(values) == 2:
            item = values[0]
            quantity_str = values[1]
            if item in inventory.keys():
                print(f"Redundant item '{item}' - discarding")
            else:
                try:
                    inventory[item] = int(quantity_str)
                except ValueError as e:
                    print(f"Quantity error for '{item}': {e}")
        else:
            print(f"Error - invalid parameter '{arg}'")

    inventory_values = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} "
          f"items: {inventory_values}")

    for item, quantity in inventory.items():
        percentage = round((quantity / inventory_values) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    if inventory:
        items = list(inventory.items())
        max_item, max_quantity = items[0]
        min_item, min_quantity = items[0]

        for item, quantity in items[1:]:
            if quantity > max_quantity:
                max_item, max_quantity = item, quantity
            if quantity < min_quantity:
                min_item, min_quantity = item, quantity

        print(f"Item most abundant: {max_item} with quantity {max_quantity}")
        print(f"Item least abundant: {min_item} with quantity {min_quantity}")
    else:
        print("No items to analyze: inventory is empty!")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
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

    for item in inventory.keys():
        if inventory_values > 0:
            percentage = round((inventory[item] / inventory_values) * 100, 1)
        else:
            percentage = 0.0
        print(f"Item {item} represents {percentage}%")

    if inventory:
        item_names = list(inventory.keys())
        max_item = item_names[0]
        min_item = item_names[0]

        for item in item_names[1:]:
            if inventory[item] > inventory[max_item]:
                max_item = item
            if inventory[item] < inventory[min_item]:
                min_item = item

        print(f"Item most abundant: {max_item} "
              f"with quantity {inventory[max_item]}")
        print(f"Item least abundant: {min_item} "
              f"with quantity {inventory[min_item]}")
    else:
        print("No items to analyze: inventory is empty!")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

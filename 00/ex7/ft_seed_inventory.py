def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknown unit type")
        return

    seed_type_cap: str = seed_type.capitalize()
    match seed_type:
        case "tomato":
            print(f"{seed_type_cap} seeds: {quantity} {unit} available")
        case "carrot":
            print(f"{seed_type_cap} seeds: {quantity} {unit} total")
        case "lettuce":
            print(f"{seed_type_cap} seeds: covers {quantity} square meters")

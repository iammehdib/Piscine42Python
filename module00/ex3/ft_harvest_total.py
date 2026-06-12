def ft_harvest_total() -> None:
    harvest_total: int = 0
    for i in [1, 2, 3]:
        input_value: str = input(f"Day {i} harvest: ")
        harvest_total += int(input_value)
    print(f"Total harvest: {harvest_total}")

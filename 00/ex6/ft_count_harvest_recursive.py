def ft_count_harvest_recursive(day: int = 1, day_limit: int = 1) -> None:
    if day_limit == 1:
        day_input: str = input("Days until harvest: ")
        day_limit = int(day_input)

    if day_limit <= 0:
        print("Harvest time!")
        return

    print(f"Day {day}")

    if day >= day_limit:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(day + 1, day_limit)

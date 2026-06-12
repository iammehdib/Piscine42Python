def ft_count_harvest_iterative() -> None:
    day_input: str = input("Days until harvest: ")
    day_limit: int = int(day_input)
    day_count: int = 1
    for day in range(day_limit):
        print(f"Day {day_count}")
        day_count += 1
    print("Harvest time!")

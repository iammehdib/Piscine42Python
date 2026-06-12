def ft_water_reminder() -> None:
    value_input: str = input("Days since last watering: ")
    value = int(value_input)
    if value > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

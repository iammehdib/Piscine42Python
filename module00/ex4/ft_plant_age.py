def ft_plant_age() -> None:
    plant_age_input: str = input("Enter plant age in days: ")
    plant_age: int = int(plant_age_input)
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = round(height, 1)
        self.days = round(days)

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

if __name__ == "__main__":
    dict_plants = [
        ["Rose", 25.0, 30],
        ["Oak", 200.0, 365],
        ["Cactus", 5.0, 90],
        ["Sunflower", 80.0, 45],
        ["Fern", 15.0, 120],
    ]
    print("=== Plant Factory Output ===")
    for plant in dict_plants:
        plant = Plant(*plant)
        print("Created: ", end="")
        plant.show()
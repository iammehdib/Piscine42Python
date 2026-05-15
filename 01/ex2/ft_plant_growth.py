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
    rose = Plant("Rose", 25, 30)
    start_grow = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for i in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {i} ===")
        rose.show()

    print(f"Growth this week: {round(rose.height - start_grow, 1)}cm")
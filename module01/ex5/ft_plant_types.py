class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name

        if height > 0.0:
            self._height = height
        else:
            self._height = 0.0

        if days > 0.0:
            self._days = days
        else:
            self._days = 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = round(height, 1)
        print(f"Height updated: {self._height}cm")

    def set_age(self, days: int) -> None:
        if days < 0.0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._days = round(days)
        print(f"Age updated: {self._days} days")

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self._has_bloom = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self._has_bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a "
              f"shade of {self.get_height()}cm "
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print(" ")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print(" ")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10,
                       "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()

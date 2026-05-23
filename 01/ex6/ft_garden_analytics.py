class Plant:

    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def show(self):
            print(f"[statistics for {self.name}]")
            print(f"""Stats: {self.grow_count} grow,
                {self.age_count} age, {self.show_count} show""")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name

        if height > 0.0:
            self._height = height
        else:
            self._height = 0.0

        if age > 0.0:
            self._age = age
        else:
            self._age = 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = round(height, 1)
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0.0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = round(age)
        print(f"Age updated: {self._age} days")

    def grow(self) -> None:
        self.Stats.grow_count += 1
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self.Stats.age_count += 1
        self._age += 1

    def show(self) -> None:
        self.Stats.show_count += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    @staticmethod
    def has_older_one_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plan", 0.0, 0)


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._has_bloom = False

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self._has_bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloom:
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    class Stats:
        def __init__(self):
            self.shade_count = 0

        def show(self):
            super().show()
            print(f"Seeds: {self.count_seeds}")

    def produce_shade(self) -> None:
        self.Stats.shade_count += 0
        print(f"Tree {self.name} now produces a "
              f"shade of {self.get_height()}cm "
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str):
        super().__init__(name, height, age, color)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a "
              f"shade of {self.get_height()}cm "
              f"long and {self.trunk_diameter}cm wide.")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.has_older_one_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.has_older_one_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.Stats.show()
    rose.bloom()
    rose.show()

    print(" ")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.get_stats()
    print("[asking the oak to produce shade]")
    oak.get_stats()
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

    print("=== Anonymous")
    anonymous = Plant.create_anonymous_plant()
    anonymous.show()
    anonymous.get_stats()

class Plant:

    class Stats:
        def __init__(self, plant: "Plant") -> None:
            self._grow_count = 0
            self._day_count = 0
            self._show_count = 0
            self._plant = plant

        def show(self) -> None:
            print(f"[statistics for {self._plant.name}]")
            print(f"Stats: {self._grow_count} grow, " +
                  f"{self._day_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name

        if height > 0.0:
            self._height = round(height, 1)
        else:
            self._height = 0.0

        if days > 0:
            self._days = days
        else:
            self._days = 0

        self._stats = self.Stats(self)

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
        if days < 0:
            print(f"{self.name}: Error, day can't be negative")
            print("day update rejected")
            return
        self._days = round(days)
        print(f"day updated: {self._days} days")

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._stats._day_count += 1
        self._days += 1

    def show(self) -> None:
        self._stats._show_count += 1
        print(f"{self.name}: {self._height}cm, {self._days} days old")

    @staticmethod
    def has_older_one_year(day: int) -> bool:
        return day > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self._has_bloom = False

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + 8.0, 1)

    def bloom(self) -> None:
        self._has_bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):

    class Stats(Plant.Stats):
        def __init__(self, tree: "Tree") -> None:
            super().__init__(tree)
            self._shade_count = 0

        def show(self) -> None:
            super().show()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats: "Tree.Stats" = self.Stats(self)

    def produce_shade(self) -> None:
        self._stats._shade_count += 1
        print(f"Tree {self.name} now produces a "
              f"shade of {self.get_height()}cm "
              f"long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


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


class Seed(Flower):

    class Stats(Flower.Stats):
        def __init__(self, flower: "Flower") -> None:
            super().__init__(flower)
            self._seed_count = 0

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self._stats: "Seed.Stats" = self.Stats(self)

    def bloom(self) -> None:
        super().bloom()
        self._stats._seed_count = 42

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 1)
        self._stats._grow_count += 1

    def age(self) -> None:
        super().age()
        self._days += 19

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._stats._seed_count}")


def show_stats(plant: Plant) -> None:
    plant._stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.has_older_one_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.has_older_one_year(400)}")
    print(" ")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)
    print(" ")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)
    print(" ")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print(" ")
    print("=== Anonymous")
    unknown = Plant.create_anonymous_plant()
    unknown.show()
    show_stats(unknown)

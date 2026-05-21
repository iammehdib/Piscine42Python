class Plant:
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
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    @staticmethod
    def has_older_one_year(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def anonymous(cls) -> "Plant":
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

    def produce_shade(self) -> None:
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
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
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

#=== Garden statistics ===
#=== Check year-old
#Is 30 days more than a year? -> False
#Is 400 days more than a year? -> True
#
#=== Flower
#Rose: 15.0cm, 10 days old
#Color: red
#Rose has not bloomed yet
#[statistics for Rose]
#Stats: 0 grow, 0 age, 1 show
#[asking the rose to grow and bloom]
#Rose: 23.0cm, 10 days old
#Color: red
#Rose is blooming beautifully!
#[statistics for Rose]
#Stats: 1 grow, 0 age, 2 show
#
#=== Tree
#Oak: 200.0cm, 365 days old
#Trunk diameter: 5.0cm
#[statistics for Oak]
#Stats: 0 grow, 0 age, 1 show
#0 shade
#[asking the oak to produce shade]
#Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
#[statistics for Oak]
#Stats: 0 grow, 0 age, 1 show
#1 shade
#
#=== Seed
#Sunflower: 80.0cm, 45 days old
#Color: yellow
#Sunflower has not bloomed yet
#Seeds: 0
#[make sunflower grow, age and bloom]
#Sunflower: 110.0cm, 65 days old
#Color: yellow
#Sunflower is blooming beautifully!
#Seeds: 42
#[statistics for Sunflower]
#Stats: 1 grow, 1 age, 2 show
#
#=== Anonymous
#Unknown plant: 0.0cm, 0 days old
#[statistics for Unknown plant]
#Stats: 0 grow, 0 age, 1 show

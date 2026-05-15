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
            self._age = 0.0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = round(height, 1)
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: float) -> None:
        if age < 0.0:
            print(f"{self.name}: Error, age can't be negative")
            print(f"Age update rejected")
            return
        self._age = round(age)
        print(f"Age updated: {self._age} days")

    def grow(self) -> None:
        self.height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
    rose_plant = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print(f"Plant created: Rose: {rose_plant.get_height()}cm, {rose_plant.get_age()} days old")
    print(" ")
    rose_plant.set_height(25)
    rose_plant.set_age(30)
    print(" ")
    rose_plant.set_height(-1)
    rose_plant.set_age(-1)
    print(" ")
    print(f"Current state: ", end="")
    rose_plant.show()

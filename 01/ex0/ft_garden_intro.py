class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    plant = Plant("Rose", 35, 30)
    print(f"""
    === Welcome to My Garden ===
    Plant: {plant.name}
    Height: {plant.height}cm
    Age: {plant.age} days
    === End of Program ===
    """)

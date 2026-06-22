class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    plant_name_cap = plant_name.capitalize()
    if plant_name == plant_name_cap:
        print(f'Watering {plant_name_cap}: [OK]')
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print('Testing valid plants...')
    try:
        print('Opening watering system')
        for plant in ['Tomato', 'Lettuce', 'Carrots']:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print('.. ending tests and returning to main')
        return
    finally:
        print('Closing watering system')

    print()

    print('Testing invalid plants...')
    try:
        print('Opening watering system')
        for plant in ['Tomato', 'lettuce', 'Carrots']:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print('.. ending tests and returning to main')
        return
    finally:
        print('Closing watering system')


if __name__ == "__main__":
    print('=== Garden Watering System ===')
    print()
    test_watering_system()
    print()
    print('Cleanup always happens, even with errors!')

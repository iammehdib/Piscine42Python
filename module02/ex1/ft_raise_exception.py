def input_temperature(temp_str: str) -> int:
    int_value: int = int(temp_str)
    if int_value > 40:
        raise ValueError(
            f"{int_value}°C is too hot for plants (max 40°C)"
        )
    if int_value < 0:
        raise ValueError(
            f"{int_value}°C is too cold for plants (min 0°C)"
        )
    return int_value


def test_temperature() -> None:
    print('=== Garden Temperature Checker ===')
    print()

    for value in ['25', 'abc', '100', '-50']:
        print(f"Input data is '{value}'")
        try:
            print(f"Temperature is now {input_temperature(value)}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

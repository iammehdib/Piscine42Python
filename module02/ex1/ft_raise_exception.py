def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    print('=== Garden Temperature ===')
    print()

    for value in ['25', 'abc', '100', '-50']:
        print(f"Input data is '{value}'")
        try:
            int_value = input_temperature(value)
            if int_value > 40:
                print(
                    f"Caught input_temperature error: "
                    f"{int_value}°C "
                    f"is too hot for plants (max 40°C)"
                )
            if int_value < 0:
                print(
                    f"Caught input_temperature error: {int_value}°C is "
                    f"too cold for plants (min 0°C)"
                )
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

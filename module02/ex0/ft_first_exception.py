def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature():
    print('=== Garden Temperature ===')
    print()

    for value in ['25', 'abc']:
        print(f"Input data is '{value}'")
        try:
            print(f"Temperature "
                  f"is now {input_temperature(value)}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
    test_temperature()

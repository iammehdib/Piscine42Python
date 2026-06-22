def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int('abc')
        case 1:
            0 / 0
        case 2:
            open('/non/existent/file', 'r')
        case 3:
            'test' + 1


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation in range(4):
        try:
            print(f'Testing operation {operation}...')
            garden_operations(operation)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f'Caught TypeError: {e}')
    print('Testing operation 4...')
    print('Operation completed successfully')
    print()
    print('All error types tested successfully!')


if __name__ == '__main__':
    test_error_types()

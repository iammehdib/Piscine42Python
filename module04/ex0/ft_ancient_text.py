import sys
import typing

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            print('=== Cyber Archives Recovery ===')
            file_path: str = sys.argv[1]
            print(f"Accessing file '{file_path}'")
            file: typing.IO = open(file_path, 'r')
            print('---')
            print()
            print(file.read())
            print()
            print('---')
            file.close()
            print(f"File '{file_path}' closed.")
        else:
            raise ValueError(f"Usage: {sys.argv[0]} <file>")
    except ValueError as e:
        print(e)
        sys.exit(1)
    except (KeyboardInterrupt):
        print("\nKeyboard interrupt by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")
        sys.exit(1)
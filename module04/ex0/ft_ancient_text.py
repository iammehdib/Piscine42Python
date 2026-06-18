import sys
import typing

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print('=== Cyber Archives Recovery ===')
        file_path: str = sys.argv[1]
        print(f"Accessing file '{file_path}'")
        try:
            file: typing.IO = open(file_path, 'r')
            print('---')
            print()
            print(file.read())
            print()
            print('---')
            file.close()
            print(f"File '{file_path}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{file_path}': {e}")
    else:
        print('Usage: ft_ancient_text.py <file>')

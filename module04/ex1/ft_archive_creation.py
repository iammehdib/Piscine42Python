import sys
import typing

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError(f"Usage: {sys.argv[0]} <file>")

        print('=== Cyber Archives Recovery & Preservation ===')
        file_path: str = sys.argv[1]
        print(f"Accessing file '{file_path}'")
        try:
            file: typing.IO = open(file_path, 'r')
            file_content: str = file.read()
            file.close()
        except OSError as e:
            print(f"Error opening file '{file_path}': {e}")
            sys.exit(1)

        print('---')
        print()
        print(file_content, end='')
        print()
        print('---')
        print(f"File '{file_path}' closed.")

        new_file_content: str = ''
        for line in file_content.split('\n'):
            if line == '':
                continue
            new_file_content += line + "#\n"
        print('Transform data:')
        print('---')
        print()
        print(new_file_content, end='')
        print()
        print('---')

        new_file_path: str = input('Enter new file name (or empty): ')
        if new_file_path:
            print(f"Saving data to '{new_file_path}'")
            try:
                new_file: typing.IO = open(new_file_path, 'w')
                new_file.write(new_file_content)
                new_file.close()
                print(f"Data saved in file '{new_file_path}'.")
            except OSError as e:
                print(f"Error opening file '{new_file_path}': {e}")
                sys.exit(1)
        else:
            print('Not saving data.')

    except ValueError as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt by user")
        sys.exit(1)
    except EOFError:
        print("\nEOF error")
        sys.exit(1)
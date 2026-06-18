import sys
import typing

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print('=== Cyber Archives Recovery ===')
        file_path: str = sys.argv[1]
        print(f"Accessing file '{file_path}'")
        try:
            file: typing.IO = open(file_path, 'r')
            file_content: str = file.read()
            print('---')
            print()
            print(file_content)
            print()
            print('---')
            file.close()
            print(f"File '{file_path}' closed.")

            new_file_content: str = ''
            for line in file_content.split('\n'):
                if line == '':
                    continue
                new_file_content += line + "#\n"
            print('Transform data:')
            print('---')
            print()
            print(new_file_content)
            print()
            print('---')

            new_file_path: str = input('Enter new file name (or empty): ')
            if new_file_path != '':
                print(f"Saving data to '{new_file_path}'")
                new_file: typing.IO = open(new_file_path, 'w')
                new_file.write(new_file_content)
                new_file.close()
                print(f"Data saved in file '{new_file_path}'.")
            else:
                print('Not saving data.')
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{file_path}': {e}")
    else:
        print('Usage: ft_ancient_text.py <file>')

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
            print(f"[STDERR] Error opening file '{file_path}': {e}",
                  file=sys.stderr)
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

        print('Enter new file name (or empty): ', end='')
        sys.stdout.flush()
        new_file_path: str = sys.stdin.readline().rstrip('\n')
        if new_file_path:
            print(f"Saving data to '{new_file_path}'")
            try:
                new_file: typing.IO = open(new_file_path, 'w')
                new_file.write(new_file_content)
                new_file.close()
                print(f"Data saved in file '{new_file_path}'.")
            except OSError as e:
                print(f"[STDERR] Error opening file '{new_file_path}': {e}",
                      file=sys.stderr)
                print('Data not saved.')
        else:
            print('Not saving data.')

    except ValueError as e:
        print(f"[STDERR] {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[STDERR] Keyboard interrupt by user", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("\n[STDERR] EOF error", file=sys.stderr)
        sys.exit(1)

import sys

if __name__ == '__main__':
    print('=== Command Quest ===')
    print(f'Program name: {sys.argv[0]}')
    argv_count: int = len(sys.argv) - 1
    if argv_count == 0:
        print('No arguments provided!')
    else:
        print(f'Arguments received: {argv_count}')
        index: int = 1
        for arg in sys.argv[1:]:
            print(f'Argument {index}: {arg}')
            index += 1
    print(f'Total arguments: {argv_count + 1}')

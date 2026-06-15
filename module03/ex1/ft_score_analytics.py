import sys

if __name__ == '__main__':
    print('=== Player Score Analytics ===')

    int_list: list[int] = []

    for arg in sys.argv[1:]:
        try:
            int_list.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(int_list) != 0:
        print(f'Scores processed: {int_list}')
        print(f'Total players: {len(int_list)}')
        print(f'Total score: {sum(int_list)}')
        print(f'Average score: {sum(int_list) / len(int_list)}')
        print(f'High score: {max(int_list)}')
        print(f'Low score: {min(int_list)}')
        print(f'Score range: {max(int_list) - min(int_list)}')
    else:
        print(
            'No scores provided. Usage: '
            'python3 ft_score_analytics.py <score1> <score2> ...'
        )

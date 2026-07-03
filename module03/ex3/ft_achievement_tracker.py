import random

ALL_ACHIEVEMENTS: list[str] = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Strategist', 'Speed Runner', 'Survivor',
    'Treasure Hunter', 'First Steps', 'Sharp Mind',
    'Unstoppable', 'Hidden Path Finder'
]
PLAYERS: list[str] = ['Alice', 'Bob', 'Charlie', 'Dylan']


def gen_player_achievements() -> set[str]:
    count = random.randint(3, len(ALL_ACHIEVEMENTS) - 1)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


if __name__ == '__main__':
    print('=== Achievement Tracker System ===')
    print()

    player_sets: list[set[str]] = []
    for name in PLAYERS:
        player_sets.append(gen_player_achievements())

    i = 0
    for name in PLAYERS:
        print(f'Player {name}: {player_sets[i]}')
        i += 1

    print()
    all_distinct: set[str] = set()
    for achievements in player_sets:
        all_distinct = all_distinct.union(achievements)
    print(f'All distinct achievements: {all_distinct}')

    print()
    common: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in player_sets:
        common = common.intersection(achievements)
    print(f'Common achievements: {common}')

    print()
    i = 0
    for name in PLAYERS:
        others: set[str] = set()
        j = 0
        for other in player_sets:
            if j != i:
                others = others.union(other)
            j += 1
        print(f'Only {name} has: {player_sets[i].difference(others)}')
        i += 1

    print()
    i = 0
    for name in PLAYERS:
        print(f'{name} is missing: {all_distinct.difference(player_sets[i])}')
        i += 1

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
    achievements: set[str] = set()
    while len(achievements) < count:
        achievements.add(random.choice(ALL_ACHIEVEMENTS))
    return achievements


if __name__ == '__main__':
    print('=== Achievement Tracker System ===')
    print()

    players: dict[str, set[str]] = {}
    for name in PLAYERS:
        players[name] = gen_player_achievements()

    for name, achievements in players.items():
        print(f'Player {name}: {achievements}')

    print()
    all_distinct: set[str] = set()
    for achievements in players.values():
        all_distinct = all_distinct.union(achievements)
    print(f'All distinct achievements: {all_distinct}')

    print()
    common: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f'Common achievements: {common}')

    print()
    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        print(f'Only {name} has: {achievements.difference(others)}')

    print()
    for name, achievements in players.items():
        print(f'{name} is missing: {all_distinct.difference(achievements)}')
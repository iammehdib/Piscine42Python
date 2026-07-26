from typing import TypeAlias

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy,
    AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError
)

Opponent: TypeAlias = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()
                print()
                print("* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print(" now fight!")
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    try:
        normal = NormalStrategy()
        aggressive = AggressiveStrategy()
        defensive = DefensiveStrategy()

        print("Tournament 0 (basic)")
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        battle([
            (FlameFactory(), normal),
            (HealingCreatureFactory(), defensive),
        ])

        print()
        print("Tournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle([
            (FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive),
        ])

        print()
        print("Tournament 2 (multiple)")
        print(" [ (Aquabub+Normal), (Healing+Defensive), "
              "(Transform+Aggressive) ]")
        battle([
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ])
    except Exception as error:
        print(f"Error: {error}")

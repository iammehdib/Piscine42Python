from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    print("Testing battle")
    challenger = first.create_base()
    opponent = second.create_base()
    print(challenger.describe())
    print(" vs.")
    print(opponent.describe())
    print(" fight!")
    print(challenger.attack())
    print(opponent.attack())


if __name__ == "__main__":
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()

        test_factory(flame_factory)
        print()
        test_factory(aqua_factory)
        print()
        test_battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"Error: {e}")

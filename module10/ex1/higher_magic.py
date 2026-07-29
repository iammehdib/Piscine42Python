from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def spell_call(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return spell_call


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:

    def power_call(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return power_call


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:

    def conditional_call(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_call


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:

    def spell_call(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]

    return spell_call


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    def enough_power(target: str, power: int) -> bool:
        return power >= 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 10)}")
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")
    print("Testing conditional caster...")
    safe_cast = conditional_caster(enough_power, fireball)
    print(safe_cast("Dragon", 5))
    print(safe_cast("Dragon", 15))
    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 20))

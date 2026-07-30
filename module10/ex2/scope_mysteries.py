from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(add_power: int) -> int:
        nonlocal power
        power += add_power
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant_item(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant_item


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(counter(), counter(), counter())

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(10)
    print(accumulator(5), accumulator(15))

    print("Testing enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("spell_power", 42)
    print(vault["recall"]("spell_power"))
    print(vault["recall"]("unknown"))

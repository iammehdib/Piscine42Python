from collections.abc import Callable


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

    def enchant_item(item_name: str):
        return enchantment_type + ' ' + item_name

    return enchant_item

def memory_vault() -> dict[str,
    Callable[[str, int]] |
    Callable[[str], int | str]
]:

    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        nonlocal memory
        memory[key] = value
        return

    def recall(key: str) -> int | str:
        nonlocal memory
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}

import functools, operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operators: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    reducer = operators.get(operation)
    if reducer is None:
        raise ValueError(f"Invalid operation: {operation}")
    return functools.reduce(reducer, spells)


def partial_enchanter(
    base_enchantment: Callable[..., str]
) -> dict[str, Callable[..., str]]:
    return {
        "fire": functools.partial(base_enchantment, element="fire"),
        "ice": functools.partial(base_enchantment, element="ice"),
        "lightning": functools.partial(base_enchantment, element="lightning")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @dispatch.register(str)
    def dispatch_str(spell: str) -> str:
        return f"Casting spell: {spell}"

    @dispatch.register(int)
    def dispatch_int(spell: int) -> str:
        return f"Casting spell with power {spell}"

    @dispatch.register(list)
    def dispatch_list(spell: list[Any]) -> str:
        return f"Casting spell combo: {', '.join(map(str, spell))}"

    return dispatch


if __name__ == "__main__":
    def enchant(power: int, element: str, target: str) -> str:
        return f"{target} enchanted with {element} ({power} power)"

    print("Testing spell reducer...")
    print(spell_reducer([10, 20, 30], "add"))
    print(spell_reducer([2, 3, 4], "multiply"))
    print(spell_reducer([15, 42, 8], "max"))
    print("Testing partial enchanter...")
    enchanters = partial_enchanter(enchant)
    print(enchanters["fire"](power=50, target="Sword"))
    print(enchanters["ice"](power=30, target="Shield"))
    print("Testing memoized fibonacci...")
    print([memoized_fibonacci(n) for n in range(10)])
    print(f"fib(50) = {memoized_fibonacci(50)}")
    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(cast("fireball"))
    print(cast(42))
    print(cast(["fireball", "heal"]))
    print(cast(3.14))

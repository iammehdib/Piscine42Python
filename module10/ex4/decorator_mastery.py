import functools
import time
from collections.abc import Callable

Spell = Callable[[str, int], str]
SpellDecorator = Callable[[Spell], Spell]


def spell_timer(func: Spell) -> Spell:

    @functools.wraps(func)
    def wrapper(target: str, power: int) -> str:
        start = time.perf_counter()
        result = func(target, power)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result

    return wrapper


def spell_logger(func: Spell) -> Spell:

    @functools.wraps(func)
    def wrapper(target: str, power: int) -> str:
        print(f"Casting {func.__name__} on {target} with {power} power")
        result = func(target, power)
        print(f"Result: {result}")
        return result

    return wrapper


def power_validator(min_power: int) -> SpellDecorator:

    def decorator(func: Spell) -> Spell:

        @functools.wraps(func)
        def wrapper(target: str, power: int) -> str:
            if power < min_power:
                return f"Spell fizzled: needs {min_power} power"
            return func(target, power)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> SpellDecorator:

    def decorator(func: Spell) -> Spell:

        @functools.wraps(func)
        def wrapper(target: str, power: int) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(target, power)
                except Exception as error:
                    print(f"Attempt {attempt} failed: {error}")
            return "Spell failed"

        return wrapper

    return decorator


if __name__ == "__main__":
    attempts = 0

    @spell_timer
    @spell_logger
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power"

    @power_validator(10)
    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    @retry_spell(3)
    def portal(target: str, power: int) -> str:
        global attempts
        attempts += 1
        if attempts < 3:
            raise RuntimeError("portal collapsed")
        return f"Portal opened to {target}"

    print("Testing spell timer and logger...")
    print(fireball("Dragon", 50))
    print("Testing power validator...")
    print(heal("Alex", 25))
    print(heal("Alex", 5))
    print("Testing retry spell...")
    print(portal("Astral Plane", 10))
    print(f"Name preserved: {fireball.__name__}")

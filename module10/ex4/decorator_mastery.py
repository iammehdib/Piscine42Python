import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power", args[-1])
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and char != " ":
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.1)
        return f"Fireball hits {target} with {power} power"

    @power_validator(10)
    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    @retry_spell(3)
    def portal(target: str, power: int) -> str:
        raise RuntimeError("portal collapsed")

    @retry_spell(3)
    def waaagh(target: str, power: int) -> str:
        return "Waaaaaaagh spelled !"

    print("Testing spell timer...")
    print(f"Result: {fireball('Dragon', 50)}")
    print(f"Name preserved: {fireball.__name__}")
    print()

    print("Testing power validator...")
    print(heal("Alex", 25))
    print(heal("Alex", 5))
    print()

    print("Testing retrying spell...")
    print(portal("Astral Plane", 10))
    print(waaagh("Dragon", 20))
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

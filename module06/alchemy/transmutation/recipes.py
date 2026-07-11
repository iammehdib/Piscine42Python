from alchemy.potions import create_air, strength_potion
from ..potions import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")

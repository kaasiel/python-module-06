from ..potions import strength_potion
from alchemy import create_fire, create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
            f" and {strength_potion()} mixed with {create_fire()}")

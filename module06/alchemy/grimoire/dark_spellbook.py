from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = dark_validate_ingredients(ingredients)
    verb = "recorded" if "INVALID" not in validation else "rejected"
    return f"Spell {verb}: {spell_name} ({validation})"

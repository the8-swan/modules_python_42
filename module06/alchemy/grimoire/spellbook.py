from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)
    status = "rejected"
    if result == f"{ingredients} - VALID":
        status = "recorded"
    return f"Spell {status}: {spell_name} ({result})"

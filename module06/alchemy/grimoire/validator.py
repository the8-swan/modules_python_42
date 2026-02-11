def validate_ingredients(ingredients: str) -> str:
	elements = ["fire", "water", "earth", "air"]
	if any(element in ingredients for element in elements):
		return f"{ingredients} - VALID"
	else:
		return f"{ingredients} - INVALID" 
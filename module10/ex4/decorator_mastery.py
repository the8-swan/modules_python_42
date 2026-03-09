from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end-start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[2] < min_power:
                raise ValueError("Insufficient power for this spell")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"({attempt+1}/{max_attempts})")
            return "Spell casting failed after max_attempts attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        counter = 0
        for char in name:
            if char.isalpha():
                counter += 1
            elif char == " ":
                pass
            else:
                return False
        if counter < 3:
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def casting(name: str) -> str:
    return f"{name} cast !"


def main():
    print("Testing spell timer...")
    print(f"Result: {casting('Fireball')}")

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(f"{mage.validate_mage_name('swans')}")
    print(f"{mage.validate_mage_name('swans8')}")

    try:
        print(f"{mage.cast_spell('Lightning', 15)}")
    except ValueError as e:
        print("Error:", e)

    try:
        print(f"{mage.cast_spell('Lightning', 5)}")
    except ValueError as e:
        print("Error:", e)


main()

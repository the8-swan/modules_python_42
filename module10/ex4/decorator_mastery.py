#functools.wraps, staticmethod, print()
from functools import wraps

#@staticmethod

# def spell_timer(func: callable) -> callable
# def power_validator(min_power: int) -> callable
# def retry_spell(max_attempts: int) -> callable
# class MageGuild:
# @staticmethod
# def validate_mage_name(name: str) -> bool
# def cast_spell(self, spell_name: str, power: int) -> str

def spell_timer(func: callable) -> callable:
    print(f"wraps {func.__name__}")
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("Spell completed in time seconds")
    return wrapper


@spell_timer
def addition(a: int, b: int):
    return a+b


print(addition(5 ,6))
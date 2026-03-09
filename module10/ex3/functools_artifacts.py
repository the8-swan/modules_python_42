from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
            "fire_enchant": partial(base_enchantment,  power=50,
                                    element="fire"),
            "ice_enchant": partial(base_enchantment,  power=50, element="ice"),
            "lightning_enchant": partial(base_enchantment,  power=50,
                                         element="light")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    prev = 0
    current = 1
    for _ in range(n):
        tmp = current + prev
        prev = current
        current = tmp
    return prev


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(arg):
        ...

    @spell.register(int)
    def _(arg: int) -> str:
        return f"spell's damage is {arg}"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"spell's enchantment is {arg}"

    @spell.register(list)
    def _(arg: list) -> str:
        result: str = ''
        for ar in arg:
            result += f"{ar} "
        return result
    return spell


def main():
    spell_powers = [31, 24, 42, 26, 21, 16]

    print("Testing spell reducer...")
    add = spell_reducer(spell_powers, "add")
    print(f"Sum: {add}")
    product = spell_reducer(spell_powers, "multiply")
    print(f"Product: {product}")
    maxv = spell_reducer(spell_powers, "max")
    print(f"Max: {maxv}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15):{memoized_fibonacci(15)}")
    print("")


main()

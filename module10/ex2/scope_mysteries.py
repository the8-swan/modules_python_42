# def mage_counter() -> callable
# def spell_accumulator(initial_power: int) -> callable
# def enchantment_factory(enchantment_type: str) -> callable
# def memory_vault() -> dict[str, callable]

def mage_counter():
    counter = 0
    def counting():
        nonlocal counter
        counter += 1
    return counting

def main():
    ...


main()

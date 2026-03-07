def mage_counter():
    counter = 0

    def counting() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counting


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulates_power(x) -> int:
        nonlocal power
        power += x
        return power
    return accumulates_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    data = {}

    def store(key: any, value: any) -> None:
        data[key] = value

    def recall(key: any) -> any:
        if key in data.keys():
            if data[key]:
                return data[key]
            else:
                return "Memory not found"
        else:
            return "key not found"

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting enchantment factory...")
    enchantment = enchantment_factory('Flaming')
    print(f"{enchantment('Sword')}")

    enchantment2 = enchantment_factory('Frozen')
    print(f"{enchantment2('Shield')}")


main()

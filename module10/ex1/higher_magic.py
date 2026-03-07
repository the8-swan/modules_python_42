
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combiner(x):
        result1 = spell1(x)
        result2 = spell2(x)
        return (result1, result2)
    return (combiner)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def combiner(x):
        return multiplier * base_spell(x)
    return (combiner)


def conditional_caster(condition: callable, spell: callable) -> callable:
    def combiner(x):
        if condition(x):
            return spell(x)
        return "Spell fizzled"
    return (combiner)


def spell_sequence(spells: list[callable]) -> callable:
    def cast(x):
        for spell in spells:
            x = spell(x)
        return x
    return cast

def fireball(x) -> str:
    return "Fireball hits Dragon"

def dragon(x) -> str:
    return "Heals Dragon"

def main():
    n = 3
    test_values = [15, 8, 17]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print("Testing spell combiner...")
    combiner = spell_combiner(fireball, dragon)
    print(f"Combined spell result: {combiner(0)}")

    print("\nTesting power amplifier...")

main()

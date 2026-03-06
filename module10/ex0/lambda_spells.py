

artifacts = [{'name': 'Wind Cloak', 'power': 64, 'type': 'accessory'},
             {'name': 'Wind Cloak', 'power': 117, 'type': 'weapon'},
             {'name': 'Lightning Rod', 'power': 112, 'type': 'weapon'},
             {'name': 'Light Prism', 'power': 99, 'type': 'weapon'}]

mages = [{'name': 'Zara', 'power': 63, 'element': 'lightning'},
         {'name': 'Ember', 'power': 69, 'element': 'wind'},
         {'name': 'Morgan', 'power': 96, 'element': 'light'},
         {'name': 'Rowan', 'power': 53, 'element': 'water'},
         {'name': 'Alex', 'power': 100, 'element': 'light'}]

spells = ['tornado', 'flash', 'meteor', 'heal']

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    new_artifacts = sorted(artifacts,
                           key=lambda artifact: artifact["power"],
                           reverse=True)
    return new_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtred_mages = list(
                filter(lambda mages: mages["power"] >= min_power, mages))
    return filtred_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spell = list(
                    map(lambda spells: "*"+spells+"*", spells))
    return transformed_spell


def mage_stats(mages: list[dict]) -> dict:
    data = {}
    sum = 0
    avg = 0
    data["max_power"] = max(mages,key=lambda mages:mages["power"])["power"]
    data["min_power"] = min(mages,key=lambda mages:mages["power"])["power"]
    sum = sum(mages, key=lambda mages:mages["power"])
    avg = mages.__len__()
    data["avg_power"] = sum/avg
    return data


def main() -> None:
    artifacts_sorted = artifact_sorter(artifacts)
    print(artifacts_sorted)
    filtred_mages = power_filter(mages, 65)
    print(filtred_mages)
    transformed_spell = spell_transformer(spells)
    print(transformed_spell)
    data= mage_stats(mages)
    print("max values is : ", data["max_power"])
    print("min values is : ", data["min_power"])

main()

data = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
        "first_blood"
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
    "diana": [
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
        "combo_king",
        "combo_king",
        "level_master",
    ],
    "eve": [
        "level_master",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
    ],
    "frank": [
        "explorer",
        "boss_hunter",
        "first_blood",
        "explorer",
        "first_blood",
        "boss_hunter",
    ],
}


def achievement_tracker():
    """ Achievement Hunter using sets  for handling
    unique collections"""
    print("=== Achievement Tracker System ===\n")
    print("Player alice achievements:", set(data["alice"]))
    print("Player bob achievements:", set(data["bob"]))
    print("Player charlie achievements:", set(data["charlie"]))
    print("")
    print("=== Achievement Analytics ===")
    alice_achiev = set(data["alice"])
    bob_achiev = set(data["bob"])
    charlie_achiev = set(data["charlie"])
    unique_achiev = alice_achiev.union(bob_achiev, charlie_achiev)
    print("all unique achievemens:", unique_achiev)
    print(f"Total unique achievements: {unique_achiev.__len__()} \n")

    common_achiev = alice_achiev.intersection(bob_achiev, charlie_achiev)
    print("Common to all players: ", common_achiev)
    print("Rare achievement:\n")

    print("Alice vs Bob common:", alice_achiev.intersection(bob_achiev))
    print("Alice unique:", alice_achiev.difference(bob_achiev))
    print("Bob unique:", bob_achiev.difference(alice_achiev))


achievement_tracker()

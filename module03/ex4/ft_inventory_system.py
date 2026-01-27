data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 5,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {
            "type": "material", "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


def inventory_analytics(data):
    players = data['players']
    catalog = data['catalog']
    # Most valuable player
    total_value = 0
    vplayer = ''
    for player, values in players.items():
        if values['total_value'] > total_value:
            total_value = values['total_value']
            vplayer = player
    print(f"Most valuable player: {vplayer} ({total_value} gold)")
    # Most items
    total_items = 0
    mplayer = ''
    for player, values in players.items():
        if values['item_count'] > total_items:
            total_items = values['item_count']
            mplayer = player
    print(f"Most items: {mplayer} ({total_items} items)")
    # Rarest items
    print("Rarest items: ", end="")
    for item, value in catalog.items():
        if value['rarity'] == 'rare':
            print(item, end="")
    print("")


def storage_system():
    print("=== Player Inventory System ===\n")
    players = data['players']
    catalog = data['catalog']
    count_categorie = {}
    index = 0
    print("=== Alice's Inventory ===")
    for item, quantity in players["alice"]["items"].items():
        print(
            f"{item} ({catalog[item]['type']}, {catalog[item]['rarity']}) "
            f"{quantity}x @ {catalog[item]['value']} gold each = "
            f"{catalog[item]['value'] * quantity} gold"
            )
        if catalog[item]['type'] in count_categorie:
            count_categorie[catalog[item]['type']] += quantity
        else:
            count_categorie[catalog[item]['type']] = quantity

    print("")
    print(f"Inventory value: {players['alice']['total_value']} gold")
    print(f"Item count: {players['alice']['item_count']} items")
    print("Categories: ", end="")
    for categorie, count in count_categorie.items():
        index += 1
        if index == len(count_categorie):
            print(f"{categorie}({count})\n")
        else:
            print(f"{categorie}({count}), ", end="")
    print("=== Transaction: Alice gives Bob 2 potions ===")
    potions = count_categorie["consumable"]
    gived = 2
    if potions < gived:
        print("Transaction failed \nalice doesn't have enough potions\n")
    else:
        print("Transaction successful !\n")
        players["alice"]["items"]['health_byte'] -= gived
        if 'health_byte' in players["bob"]["items"]:
            players["bob"]["items"]['health_byte'] += gived
        else:
            players["bob"]["items"]['health_byte'] = gived
    print("=== Updated Inventories ===")
    print(f"Alice potions: {players['alice']['items']['health_byte']}")
    if 'health_byte' in players["bob"]["items"]:
        print(f"bob potions: {players['bob']['items']['health_byte']}\n")
    else:
        print("bob potions: 0")
    print("=== Inventory Analytics ===")
    inventory_analytics(data)


storage_system()

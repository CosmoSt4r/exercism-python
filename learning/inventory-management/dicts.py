from collections import Counter, defaultdict


def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    return dict(Counter(items))


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    inventory = defaultdict(int, inventory)
    for item in items:
        inventory[item] += 1
    return dict(inventory)


def delete_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    """

    inventory = defaultdict(int, inventory)
    for item in items:
        inventory[item] -= 1 if inventory[item] != 0 else 0
    return dict(inventory)


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [item for item in inventory.items() if item[1] != 0]

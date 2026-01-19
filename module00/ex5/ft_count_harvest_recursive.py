def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_recursive(1, days)
    print("Harvest time!")


def count_recursive(index: int, days: int):
    if index > days:
        return
    print("Day:", index)
    count_recursive(index+1, days)

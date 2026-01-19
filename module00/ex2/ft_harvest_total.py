def ft_harvest_total():
    i = 1
    counter = 0
    while i <= 3:
        counter += int(input(f"Day {i} harvest: "))
        i += 1
    print("Total harvest:", counter)

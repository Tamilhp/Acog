def rabbits(months, offsprings):

    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    print(child)
    return child

rabbits(6,3)
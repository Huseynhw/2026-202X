def total_score(*points, bonus=0):
    total = sum(points) + bonus
    if total <= 0:
        total = 0

    return total


print(total_score(10, -15, 20, bonus=5))
print(total_score(5, -20, bonus=0))

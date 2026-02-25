def unique_numbers(numbers):
    numbers = sorted(numbers)
    idx = 0
    unique = 0
    while idx < len(numbers):
        current = numbers[idx]
        ndx = idx + 1
        while ndx < len(numbers) and numbers[ndx] == current:
            ndx += 1
        unique += 1
        idx = ndx
    return unique


print(unique_numbers([1, 2, 3, 3, 3, 4]))
print(unique_numbers([1, 1, 1, 3, 2, 4, 6, 1, 2, 2, 3, 7]))

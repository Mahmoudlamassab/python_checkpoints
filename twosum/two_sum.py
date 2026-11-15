def two_sum(numbers, target):
    
    for i, num in enumerate(numbers):
        for j, nb in enumerate(numbers[i + 1:], start=i + 1):
            if num + nb == target and i != j:
                return [i, j]

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
print("Checkpoint OK")
def unique_sorted(numbers):
    res=[]
    for num in numbers:
        if num not in res:
            res.append(num)
    return sorted(res)
    
assert unique_sorted([3, 1, 3, 2]) == [1, 2, 3]
assert unique_sorted([]) == []
assert unique_sorted([5, 5, 5]) == [5]
assert unique_sorted([-1, 0, -1]) == [-1, 0]
print("Checkpoint OK")
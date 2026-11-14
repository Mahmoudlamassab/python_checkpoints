def unique_sorted(numbers):
    res=[]
    for num in numbers:
        if num not in res:
            res.append(num)
    return sorted(res)
    
assert unique_sorted([3, 1, 3, 2]) == [1, 2, 3]
print("Checkpoint OK")
set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference1 = set1 - set2
print("Set Difference (set1 - set2):", difference1)

difference2 = set2 - set1
print("Set Difference (set2 - set1):", difference2)

union = set1 | set2
print("Union of Sets (set1 | set2):", union)

symmetric_difference = set1 ^ set2
print("Symmetric Difference (set1 ^ set2):", symmetric_difference)

intersection = set1 & set2
print("Set Intersection (set1 & set2):", intersection)

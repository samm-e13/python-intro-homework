list1 = ["r", "python", "java", "c++"]
list2 = ["r", "c", "swift", "python"]

list1 = set(list1)
list2 = set(list2)

print(list1.union(list2))
print(list1.intersection(list2))
print(list1.difference(list2))


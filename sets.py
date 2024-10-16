# Create a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Add a single element
my_set.add(6)
print("After Adding 6:", my_set)

# Add multiple elements
my_set.update([7, 8, 9])
print("After Adding Multiple Elements:", my_set)

# Remove a single element
my_set.remove(5)
print("After Removing 5:", my_set)

# Remove multiple elements
my_set.difference_update([6, 7, 8])
print("After Removing Multiple Elements:", my_set)

# Modify (no direct modification, but can clear and update)
my_set.clear()
my_set.update([10, 11, 12])
print("After Modification (Clear and Update):", my_set)
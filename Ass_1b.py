# Creating lists
fruits = ['apple', 'banana', 'cherry', 'date']
print("Original list:", fruits)
# Accessing elements
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
# Modifying elements
fruits[1] = 'blueberry'
print("Modified list:", fruits)
# Adding elements
fruits.append('elderberry')
print("List after append:", fruits)
fruits.insert(1, 'blackberry')
print("List after insert:", fruits)
# Removing elements
fruits.remove('cherry')
print("List after remove:", fruits)
fruits.pop(2)
print("List after pop:", fruits)
del fruits[1]
print("List after del:", fruits)
# Concatenating lists
vegetables = ['carrot', 'broccoli']
all_items = fruits + vegetables
print("Concatenated list:", all_items)
# Repeating lists
repeated_fruits = fruits * 2
print("Repeated list:", repeated_fruits)
# Checking membership
print("Is 'apple' in fruits?", 'apple' in fruits)
print("Is 'banana' in fruits?", 'banana' in fruits)
# Finding length
print("Length of fruits list:", len(fruits))
# List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original numbers list:", numbers)
# Basic slicing
slice_1 = numbers[2:6]
print("Sliced list (2:6):", slice_1)
# Omitting start or stop
slice_2 = numbers[:5]
print("Sliced list (:5):", slice_2)
slice_3 = numbers[5:]
print("Sliced list (5:):", slice_3)
# Using negative indices
slice_4 = numbers[-5:-2]
print("Sliced list (-5:-2):", slice_4)
# Using a step
slice_5 = numbers[1:9:2]
print("Sliced list (1:9:2):", slice_5)
# Reversing a list
reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

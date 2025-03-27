# --- List Basics: Creation and Type ---

# Lists can hold elements of the same type or mixed types.
my_list = ["A", "B", "C"]
print(type(my_list))
my_list2 = ["A", 3, 4.3]
print(type(my_list2))

# --- List Length ---
# Shows how to get the number of items in a list using len().
result = len(my_list)
print(result)

# --- Accessing Elements (Indexing) ---
# Accessing a single element using its zero-based index.
result = my_list[0]
print(result)

# --- Slicing Lists ---
# Extracting a portion (sub-list) of the list using slicing.
# Note: The end index (1) is exclusive.
result = my_list[0:1]
print(result) # Output: ['A']

# --- List Concatenation ---
# Joining two lists together to create a new list.
my_list3 = ["D", "F", "G"]
result = my_list + my_list3
print(result)

# --- Modifying List Elements ---
# Changing the value of an element at a specific index. Lists are mutable.
my_list[0] = "Change"
print(my_list)

# --- Adding Elements (append) ---
# Adding a new item to the very end of the list.
my_list3.append("H")
print(my_list3)

# --- Removing Elements (pop without index) ---
# Removing and returning the *last* item from the list.
my_list3.pop()
print(my_list3)

# --- Removing Elements (pop with index) ---
# Removing and returning the item at a specific index.
my_list3.pop(1)
print(my_list3)

# --- Pop Return Value ---
# Demonstrates that pop() returns the element that was removed.
print(my_list)
pop_variable = my_list.pop(1)
print(pop_variable)
print(my_list)

# --- Sorting Lists (sort) ---
# Sorting the list in-place (modifies the original list).
# By default, sorts alphabetically or numerically ascending.
my_list4 = ['t', 'y', 'p']
print(my_list4)
my_list4.sort()
print(my_list4)

# --- Reversing Lists (reverse) ---
# Reversing the order of elements in the list in-place.
my_list4.reverse()
print(my_list4)





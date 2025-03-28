#Set

my_set = set([1,2,3,4,5])
print(my_set)

other_set={1,2,3}
print(other_set)

other_set1={1,2,3,3}
print(other_set1)

my_set.add(6)
print(len(my_set))
print(2 in my_set)

s3 = other_set.union(my_set)
print(s3)

my_set.remove(2)
print(my_set)

my_set.discard(2)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)


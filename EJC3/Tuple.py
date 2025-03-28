#Tuples

my_tuple=1,2,3,4
print(my_tuple)

my_tuple2=1,"ddd",3.3,4
print(my_tuple2)

print(my_tuple2[0])
print(my_tuple2[-1])

my_tuple3=1,2,(3,3.5,3.9),4
print(my_tuple3[2][1])

my_list =list(my_tuple)
print(type(my_list))

x,y,z,s = my_tuple
print(x)
print(y)
print(z)
print(s)

my_tuple4=1,2,3,1
print(my_tuple4.count(1))
# --- Dictionaries ---
# Dictionaries store data in key-value pairs.

# Access and print the value associated with the key "C1"
dic={"C1":"Valor1" ,"C2":"Valor2"}
print(dic)
print(dic["C1"])

# Attempting to access a non-existent key ("C3") would raise a KeyError.
#print(dic["C3"])

# Create a dictionary representing a client's information
client={"nombre":"Paco" ,"apellido":"Robles","age":20}
print(client["apellido"])

# Access the list associated with "c1", then access the element at index 1 within that list
dic2={"c1":[1,2,3]}
print(dic2["c1"][1])

# Access the list for key "c2", get the element at index 1 ("E"), convert it to lowercase, and print
dic2={"c1":["A","B","C"],"c2":["D","E","F"]}
print(dic2["c2"][1].lower())

# Modify the value associated with the existing key 2
dic3={1:"A",2:"B"}
print(dic3)
dic3[2]="C"
print(dic3)

# Modify the value associated with the existing key 1
dic3[1]="b"
print(dic3)

# Print a view object containing all the keys of 'dic3'
print(dic3.keys())

# Print a view object containing all the key-value tuple pairs of 'dic3'
print(dic3.items())

# Print a view object containing all the values of 'dic3'
print(dic3.values())




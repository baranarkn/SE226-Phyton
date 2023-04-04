# part a
dictionary = {i: (i-1)*i for i in range(1,31)}
print(dictionary)
print("----------------------------------------------------")

# part b
dictionary = {i: (i-1)*i for i in range(1,31)}
for k, v in dictionary.items():
    print(f"{k}: {v}")
print("----------------------------------------------------")

# part c
dictionary = {i: (i-1)*i for i in range(1,31)}
total = 0
for value in dictionary.values():
    total += value
print("The sum of all the values in the dictionary:",total)
print("----------------------------------------------------")

# part d
for x in range(1, 31):
    if x == 1:
        dictionary[x] = 0
    else:
        dictionary[x] = (x - 1) * x

key_to_remove = input("Enter a key to remove from the dictionary: ")

if key_to_remove.isdigit() and int(key_to_remove) in dictionary:
    del dictionary[int(key_to_remove)]
    print("The item with key", key_to_remove, "has been removed from the dictionary.")
else:
    print("Invalid input or key not found in the dictionary.")

for k, v in dictionary.items():
    print(f"{k}: {v}")
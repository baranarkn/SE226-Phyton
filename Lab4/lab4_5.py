divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

# part a
united_we_stand = divided.copy()
united_we_stand.update(we_fall)

print("Name  Age")
for name, age in united_we_stand.items():
    print(f"{name}   {age}")
print("----------------------------------------------------")

# part b
del united_we_stand['Nat']
print(united_we_stand)
print("----------------------------------------------------")

# part c
print("Name  Age")
for name, age in sorted(united_we_stand.items()):
    print(f"{name}   {age}")
print("----------------------------------------------------")

# part d
values = united_we_stand.values()
print("Maximum value:",max(values))
print("Minimum value:",min(values))
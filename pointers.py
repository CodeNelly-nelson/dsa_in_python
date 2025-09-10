
# # Integer are immutable - can't be changed

# num1 = 11
# num2  = num1 # both num1 and num

# print("Before num2 is updated")
# print(f"num1 points to: {id(num1)} value: {num1}")
# print(f"num2 points to: {id(num2)} value: {num2}")

# # Updating num2
# num2 = 22

# print("\nAfter num2 is updated")
# print(f"num1 points to: {id(num1)} value: {num1}")
# print(f"num2 points to: {id(num2)} value: {num2}")


# Dictionaries - are mutable, can be changed
dict1  = {"value": 11}
dict2  = dict1

dict3 = {"value": 33}


print("\nBefore dict2-value is updated")
print(f"dict1 points to: {id(dict1)} value: {dict1}")
print(f"dict2 points to: {id(dict2)} value: {dict2}")
print(f"dict3 points to: {id(dict3)} value: {dict3}")

dict2["value"] = 22 # changing just the value not the reference

print("\nAfter dict2 -value is updated") 
print(f"dict1 points to: {id(dict1)} value: {dict1}")
print(f"dict2 points to: {id(dict2)} value: {dict2}")
dict2 = dict3 # changing the variable is pointing to, the reference
print("\nAfter dict2 is change to point to dict3 ") 
print(f"dict2 points to: {id(dict2)} value: {dict2}")
print(f"dict3 points to: {id(dict3)} value: {dict3}")





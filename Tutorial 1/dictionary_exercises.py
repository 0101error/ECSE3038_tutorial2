# tutorial/dictionary_exercises.py
person = {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}

print("a. Person's name:", person["name"])

person["occupation"] = "Engineer"
print("\nb. Dictionary after adding occupation:", person)

person["age"] = 29
print("\nc. Dictionary after updating age:", person)

del person["city"]
print("\nd. Dictionary after removing city:", person)

print("\ne. Keys of the modified dictionary:", person.keys())
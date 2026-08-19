a = {
    "name": "Manju",
    "age": 22,
    "city": "Bangalore",
    "marks": [90, 80, 70, 60]
}

print(a.items())
print(a.keys())
print(a.values())

print(a.get("name"))
print(a["name"])

a.update({"name": "Manoj"})
print(a)
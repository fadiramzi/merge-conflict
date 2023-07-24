people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
def mysort(p):
    return p['name']

people.sort(key=lambda p:p['name'])
print(people)
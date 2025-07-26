person = {
    "name": "John",
    "Hobby": "Reading",
    "hright": 180,
    "weight": 75,
}

person.clear()

person_copy = person.copy()

hobby = person.get("Hobby")

items = person.items()

keys = person.keys()

values = person.values()

popped_hobby = person.pop("Hobby")

person.popitem()

person.update({"name": "Alice", "Hobby": "Cycling", "height": 165, "weight": 60})

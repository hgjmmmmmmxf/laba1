data = {
    "countries": [],
    "capitals": [],
    "coordinates": []
}

countries = ["Россия", "Канада", "Япония", "Германия"]
capitals = ["Москва", "Оттава", "Токио", "Берлин"]
coordinates = [
    (55.7558, 37.6173),
    (45.4215, -75.6996),
    (35.6895, 139.6917),
    (52.52, 13.405)
]

for i in range(len(countries)):
    data["countries"].append(countries[i])
    data["capitals"].append(capitals[i])
    data["coordinates"].append(coordinates[i])

tests = [
    {"country": "Россия", "capital": "Москва", "coordinates": (55.7558, 37.6173)},
    {"country": "Канада", "capital": "Оттава", "coordinates": (45.4215, -75.6996)},
    {"country": "Япония", "capital": "Токио", "coordinates": (35.6895, 139.6917)},
    {"country": "Германия", "capital": "Берлин", "coordinates": (52.52, 13.405)}
]

print("Словарь:", data)
print("Тесты:", tests)
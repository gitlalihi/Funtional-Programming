#Python program that creates a list of tuples, each containing a city name and its population. Use the filter function to extract cities with a population greater than 2 million.

def filter_cities(city):
    return city[1] > 2000000


cities_population = [
    ("City1", 8398748),
    ("City2", 3990456),
    ("City3", 2705994),
    ("city4", 2320268),
    ("city5", 1680992),
   
]


filtered_cities = list(filter(filter_cities, cities_population))


print("Cities with population greater than 2 million:")
for c in filtered_cities:
    print(f"{c[0]}: {c[1]}")

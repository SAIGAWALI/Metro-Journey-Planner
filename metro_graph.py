def create_metro_graph(city):
    base_edges = get_city_edges(city)
    graph = {}

    for u, v, weight in base_edges:
        graph.setdefault(u, {})[v] = weight
        graph.setdefault(v, {})[u] = weight

    return graph


def get_cities():
    return ["Mumbai", "Delhi"]

import csv

def get_city_edges(city):
    if city == "Delhi":
        with open("delhi_metro.csv", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            return [(row[0], row[1], float(row[2])) for row in reader]
    elif city == "Mumbai":
        with open("mumbai_metro.csv", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            return [(row[0], row[1], float(row[2])) for row in reader]
    return []

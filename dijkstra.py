import heapq
import math

def dijkstra(graph, src, dst, optimize_for="distance"):
    queue = []
    heapq.heappush(queue, (0, src, [src]))
    visited = set()

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        if current == dst:
            time_minutes = math.ceil(cost / 60) if optimize_for == "time" else None
            return {
                "path": path,
                "cost": cost,
                "time_minutes": time_minutes
            }

        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                if optimize_for == "time":
                    new_cost = cost + 120 + 40 * weight
                else:
                    new_cost = cost + weight
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))

    return None

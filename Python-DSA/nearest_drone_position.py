class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target[0], target[1]
        min_distance = float('inf')
        best_index = -1
        for i in range(len(drones)):
            x, y, travel_range = drones[i]
            distance = abs(x - tx) + abs(y - ty)

            if distance <= travel_range:
                if distance < min_distance:
                    min_distance = distance
                    best_index = i
        return best_index




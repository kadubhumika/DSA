class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                found_value = self.cache[i][1]
                self.cache.pop(i)
                self.cache.append([key, found_value])
                return found_value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                break  # Stop searching once found
        self.cache.append([key, value])
        if len(self.cache) > self.capacity:
            self.cache.pop(0)

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = defaultdict(list)
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key][1] += 1
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            min_freq = min(self.cache.values(), key=lambda x: x[1])[1]
            for k, v in list(self.cache.items()):
                if v[1] == min_freq:
                    del self.cache[k]
                    break
        self.cache[key] = [value, 1]

lfu = LFUCache(2)
lfu.put(1, 10)
lfu.put(2, 20)
print(lfu.get(1))  # Output: 10
lfu.put(3, 30)  # Removes LFU key
print(lfu.get(2))  # Output: -1

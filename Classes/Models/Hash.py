class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.keys = [None] * self.size
        self.buckets = [None] * self.size

    def hashFunction(self, key):
        # Use a built-in hash function to handle non-integer keys
        hash_value = hash(key)
        return hash_value % self.size

    def rehashFunction(self, oldHash):
        return (oldHash + 1) % self.size

    def resize(self):
        self.size *= 2
        self.keys = self.keys + [None] * self.size
        self.buckets = self.buckets + [None] * self.size

    def __setitem__(self, key, value):
        if self.count / self.size > 0.6:  # resize if load factor > 0.6
            self.resize()

        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys[index] is None:
                self.buckets[index] = value
                self.keys[index] = key
                self.count += 1
                break
            else:
                if self.keys[index] == key:
                    self.buckets[index] = value
                    break
                else:
                    index = self.rehashFunction(index)
                    if index == startIndex:
                        break

    def __getitem__(self, key):
        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys[index] == key:
                return self.buckets[index]
            else:
                index = self.rehashFunction(index)
                if index == startIndex:
                    return None

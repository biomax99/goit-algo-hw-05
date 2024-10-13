class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        # Якщо ключ вже існує, оновлюємо значення
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Інакше додаємо новий ключ-значення
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    self.table[index].pop(i)
                    return True
        return False

# Використання
hash_table = HashTable(10)
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)

print(hash_table.get("apple"))
hash_table.delete("apple")
print(hash_table.get("apple"))

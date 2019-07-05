class CacheItem(object):

    def __init__(self, key, val, cache):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        cache[key] = self


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = None
        self.tail = None

    def print(self):
        item = self.head
        vals = []
        while item is not None:
            vals.append(item.key)
            item = item.next
        print(vals)

    def _set_head(self, item):
        if self.head is None:
            self.head = item
        else:
            self.head.pre = item
            item.next = self.head
            item.pre = None
            self.head = item

        if self.count == 1:
            self.tail = item

    def _pop_item(self, item):
        # pop item from linked list
        if item.pre is not None:
            item.pre.next = item.next
        if item.next is not None:
            item.next.pre = item.pre

        if item == self.head:
            self.head = item.next

        if item == self.tail:
            self.tail = item.pre

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            item = self.cache[key]

            self._pop_item(item)

            # put item to head of queue
            self._set_head(item)
            # self.print()
            return item.val



    def put(self, key: int, value: int) -> None:

        # update value and move item to head
        if key in self.cache:
            item = self.cache[key]
            item.val = value

            self._pop_item(item)

            # put item to head of queue
            self._set_head(item)
        else:
            if self.count >= self.capacity:
                # pop tail
                item = self.tail
                self._pop_item(item)
                del self.cache[item.key]
                self.count -= 1

            item = CacheItem(key, value, self.cache)

            self.count += 1
            self._set_head(item)

        # self.print()


if __name__ == "__main__":
    # cache = LRUCache(2)

    # print(cache.put(1, 1))
    # print(cache.put(2, 2))
    # print(cache.get(1))
    # print(cache.put(3, 3))
    # print(cache.get(2))
    # print(cache.put(4, 4))
    # print(cache.get(1))
    # print(cache.get(3))
    # print(cache.get(4))

    commands = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    items = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    cache = LRUCache(10)

    for i in range(1, len(commands)):
        if commands[i] == 'put':
            cache.put(items[i][0], items[i][1])
        elif commands[i] == 'get':
            cache.get(items[i][0])
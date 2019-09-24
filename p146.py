class CacheItem(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.count = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def move_node_to_head(self, node):
        if self.head is None:
            self.head = node
            return
        if node == self.head:
            return
        if node == self.tail:
            self.tail = self.tail.pre
            self.tail.next = None
        if node.pre is not None:
            node.pre.next = node.next
        if node.next is not None:
            node.next.pre = node.pre
        node.pre = None
        node.next = self.head
        self.head.pre = node
        self.head = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = CacheItem(key, value)
            self.cache[key] = node
            self.move_node_to_head(node)
            self.count += 1
        else:
            node = self.cache[key]
            node.val = value
            self.move_node_to_head(node)

        if self.tail is None:
            self.tail = node

        if self.count > self.capacity:
            del self.cache[self.tail.key]
            self.tail = self.tail.pre
            self.tail.next = None
            self.count -= 1


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

    # commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # items = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    commands = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    items = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

    # commands = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put",
    #             "put",
    #             "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put",
    #             "get",
    #             "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put",
    #             "put",
    #             "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get",
    #             "put",
    #             "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put",
    #             "put",
    #             "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put",
    #             "put",
    #             "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    # items = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
    #          [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3],
    #          [10, 11], [8],
    #          [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
    #          [2, 9],
    #          [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26],
    #          [8, 17],
    #          [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28],
    #          [1, 20],
    #          [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12],
    #          [9, 19],
    #          [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1],
    #          [2, 2],
    #          [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    cache = LRUCache(2)

    print(None)
    for i in range(1, len(commands)):
        if commands[i] == 'put':
            cache.put(items[i][0], items[i][1])
            print(None)
        elif commands[i] == 'get':
            print(cache.get(items[i][0]))

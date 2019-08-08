from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dict = {}
        self.vacant_ids = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            if len(self.vacant_ids) > 0:
                ind = self.vacant_ids.pop()
                self.arr[ind] = val
                self.dict[val] = ind
            else:
                self.arr.append(val)
                self.dict[val] = len(self.arr) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            ind = self.dict[val]
            del self.dict[val]
            self.vacant_ids.add(ind)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        while True:
            ind = randint(0, len(self.arr)-1)
            if ind not in self.vacant_ids:
                return self.arr[ind]

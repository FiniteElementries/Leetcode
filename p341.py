# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):

    def flatten_nest(self, nested_list):
        if nested_list.isInteger():
            self.arr.append(nested_list.getInteger())
        else:
            for item in nested_list.getList():
                self.flatten_nest(item)

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.arr = []
        for item in nestedList:
            self.flatten_nest(nested_list=item)
        self.ind = 0

    def next(self):
        """
        :rtype: int
        """
        ret_val = self.arr[self.ind]
        self.ind += 1
        return ret_val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ind < len(self.arr)

# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)

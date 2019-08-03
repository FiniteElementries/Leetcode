import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def balance(self):
        while len(self.max_heap) - len(self.min_heap) > 1:
            # move from max to min
            max_top = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -max_top)

        while len(self.min_heap) - len(self.max_heap) > 1:
            # move from min to max
            min_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_top)

    def peek_top(self, h):
        min_top = heapq.heappop(h)
        heapq.heappush(h, min_top)
        return min_top

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        else:
            min_top = self.peek_top(self.min_heap)

            if num < min_top:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            self.balance()

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.min_heap:
            return self.max_heap[0]
        if not self.max_heap:
            return self.min_heap[0]

        min_top = self.peek_top(self.min_heap)
        max_top = self.peek_top(self.max_heap)

        if len(self.min_heap) == len(self.max_heap):
            return (min_top - max_top) / 2
        elif len(self.min_heap) < len(self.max_heap):
            return -max_top
        else:
            return min_top


if __name__ == '__main__':

    s = MedianFinder()

    commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
                "findMedian",
                "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
                "addNum",
                "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    val = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]

    commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    val = [[], [1], [2], [], [3], []]

    # commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian"]
    # val = [[], [40], [], [12], [], [16], [], [14], [], [35], [], [19], [], [34], [], [35], [], [28], [], [35], [], [26], [],
    #  [6], [], [8], [], [2], [], [14], [], [25], [], [25], [], [4], [], [33], [], [18], [], [10], [], [14], [], [27], [],
    #  [3], [], [35], [], [13], [], [24], [], [27], [], [14], [], [5], [], [0], [], [38], [], [19], [], [25], [], [11],
    #  [], [14], [], [31], [], [30], [], [11], [], [31], [], [0], []]

    # commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    # val = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]
    #
    # commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian"]
    # val = [[], [78], [], [14], [], [50], [], [20], [], [13], [], [9], [], [25], [], [8], [], [13], [], [37], [], [29], [],
    #  [33], [], [55], [], [52], [], [6], [], [17], [], [65], [], [23], [], [74], [], [43], [], [5], [], [29], [], [29],
    #  [], [72], [], [7], [], [13], [], [56], [], [21], [], [31], [], [66], [], [69], [], [69], [], [74], [], [12], [],
    #  [77], [], [23], [], [10], [], [6], [], [27], [], [63], [], [77], [], [21], [], [40], [], [10], [], [19], [], [59],
    #  [], [35], [], [40], [], [44], [], [4], [], [15], [], [29], [], [63], [], [27], [], [46], [], [56], [], [0], [],
    #  [60], [], [72], [], [35], [], [54], [], [50], [], [14], [], [29], [], [62], [], [24], [], [18], [], [79], [], [16],
    #  [], [19], [], [8], [], [77], [], [10], [], [21], [], [66], [], [42], [], [76], [], [14], [], [58], [], [20], [],
    #  [0], []]
    #
    # commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
    #  "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
    #  "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    # val = [[], [155], [], [66], [], [114], [], [0], [], [60], [], [73], [], [109], [], [26], [], [154], [], [0], [], [107],
    #  [], [75], [], [9], [], [57], [], [53], [], [6], [], [85], [], [151], [], [12], [], [110], [], [64], [], [103], [],
    #  [42], [], [103], [], [126], [], [3], [], [88], [], [142], [], [79], [], [88], [], [147], [], [47], [], [134], [],
    #  [27], [], [82], [], [95], [], [26], [], [124], [], [71], [], [79], [], [130], [], [91], [], [131], [], [67], [],
    #  [64], [], [16], [], [60], [], [156], [], [9], [], [65], [], [21], [], [66], [], [49], [], [108], [], [80], [],
    #  [17], [], [159], [], [24], [], [90], [], [79], [], [31], [], [79], [], [113], [], [39], [], [54], [], [156], [],
    #  [139], [], [8], [], [90], [], [19], [], [10], [], [50], [], [89], [], [77], [], [83], [], [13], [], [3], [], [71],
    #  [], [52], [], [21], [], [50], [], [120], [], [159], [], [45], [], [22], [], [69], [], [144], [], [158], [], [19],
    #  [], [109], [], [52], [], [50], [], [51], [], [62], [], [20], [], [22], [], [71], [], [95], [], [47], [], [12], [],
    #  [21], [], [32], [], [17], [], [130], [], [109], [], [8], [], [61], [], [13], [], [48], [], [107], [], [14], [],
    #  [122], [], [62], [], [54], [], [70], [], [96], [], [11], [], [141], [], [129], [], [157], [], [136], [], [41], [],
    #  [40], [], [78], [], [141], [], [16], [], [137], [], [127], [], [19], [], [70], [], [15], [], [16], [], [65], [],
    #  [96], [], [157], [], [111], [], [87], [], [95], [], [52], [], [42], [], [12], [], [60], [], [17], [], [20], [],
    #  [63], [], [56], [], [37], [], [129], [], [67], [], [129], [], [106], [], [107], [], [133], [], [80], [], [8], [],
    #  [56], [], [72], [], [81], [], [143], [], [90], [], [0], []]

    for i in range(len(commands)):
        if commands[i] == 'addNum':
            s.addNum(val[i][0])
        elif commands[i] == 'findMedian':
            print(f"\n{s.findMedian()}\n")
            pass

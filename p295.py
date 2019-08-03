class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.order = 1

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = None
        self.count = 0
        self.left_count = 0
        self.right_count = 0

    def update_branch(self, node):

        if not node:
            return
        node.order += 1

        self.update_branch(node.left)
        self.update_branch(node.right)

    def add_val(self, val, node):
        if node is None:
            return TreeNode(val)
        else:
            if val <= node.val:
                node.left = self.add_val(val, node.left)
            else:
                node.right = self.add_val(val, node.right)
            return node

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.root = self.add_val(num, self.root)
        self.count += 1

        if self.root.left is not None or self.root.right is not None:
            if num <= self.root.val:
                self.left_count += 1
                # rotate right
                if self.left_count - self.right_count >= 1:
                    self.rotate_right()
                    self.left_count -= 1
                    self.right_count += 1

            else:
                self.right_count += 1
                # rotate left
                if self.right_count - self.left_count >= 1:
                    self.rotate_left()
                    self.left_count += 1
                    self.right_count -= 1
            if self.left_count == self.right_count:
                self.median = self.root.val
            elif self.left_count > self.right_count:
                self.median = (self.root.val + self.root.left.val) / 2
            else:
                self.median = (self.root.val + self.root.right.val) / 2
        else:
            self.median = self.root.val

    def rotate_left(self):
        node = self.root
        right = node.right
        node.right = None

        new_root_old_parent = None
        new_root = right
        while new_root.left:
            new_root_old_parent = new_root
            new_root = new_root.left
        if new_root_old_parent:
            new_root_old_parent.left = new_root.right

        new_root.left = node
        if new_root != right:
            new_root.right = right

        self.root = new_root

    def rotate_right(self):
        node = self.root
        left = node.left
        node.left = None

        new_root_old_parent = None
        new_root = left
        while new_root.right:
            new_root_old_parent = new_root
            new_root = new_root.right
        if new_root_old_parent:
            new_root_old_parent.right = new_root.left

        new_root.right = node
        if new_root != left:
            new_root.left = left

        self.root = new_root

    def findMedian(self):
        """
        :rtype: float
        """
        return self.median


if __name__ == '__main__':

    s = MedianFinder()

    commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
                "findMedian",
                "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
                "addNum",
                "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    val = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]

    # commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    # val = [[], [1], [2], [], [3], []]

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

    commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    val = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]

    commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian"]
    val = [[], [78], [], [14], [], [50], [], [20], [], [13], [], [9], [], [25], [], [8], [], [13], [], [37], [], [29], [],
     [33], [], [55], [], [52], [], [6], [], [17], [], [65], [], [23], [], [74], [], [43], [], [5], [], [29], [], [29],
     [], [72], [], [7], [], [13], [], [56], [], [21], [], [31], [], [66], [], [69], [], [69], [], [74], [], [12], [],
     [77], [], [23], [], [10], [], [6], [], [27], [], [63], [], [77], [], [21], [], [40], [], [10], [], [19], [], [59],
     [], [35], [], [40], [], [44], [], [4], [], [15], [], [29], [], [63], [], [27], [], [46], [], [56], [], [0], [],
     [60], [], [72], [], [35], [], [54], [], [50], [], [14], [], [29], [], [62], [], [24], [], [18], [], [79], [], [16],
     [], [19], [], [8], [], [77], [], [10], [], [21], [], [66], [], [42], [], [76], [], [14], [], [58], [], [20], [],
     [0], []]

    commands = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    val = [[], [155], [], [66], [], [114], [], [0], [], [60], [], [73], [], [109], [], [26], [], [154], [], [0], [], [107],
     [], [75], [], [9], [], [57], [], [53], [], [6], [], [85], [], [151], [], [12], [], [110], [], [64], [], [103], [],
     [42], [], [103], [], [126], [], [3], [], [88], [], [142], [], [79], [], [88], [], [147], [], [47], [], [134], [],
     [27], [], [82], [], [95], [], [26], [], [124], [], [71], [], [79], [], [130], [], [91], [], [131], [], [67], [],
     [64], [], [16], [], [60], [], [156], [], [9], [], [65], [], [21], [], [66], [], [49], [], [108], [], [80], [],
     [17], [], [159], [], [24], [], [90], [], [79], [], [31], [], [79], [], [113], [], [39], [], [54], [], [156], [],
     [139], [], [8], [], [90], [], [19], [], [10], [], [50], [], [89], [], [77], [], [83], [], [13], [], [3], [], [71],
     [], [52], [], [21], [], [50], [], [120], [], [159], [], [45], [], [22], [], [69], [], [144], [], [158], [], [19],
     [], [109], [], [52], [], [50], [], [51], [], [62], [], [20], [], [22], [], [71], [], [95], [], [47], [], [12], [],
     [21], [], [32], [], [17], [], [130], [], [109], [], [8], [], [61], [], [13], [], [48], [], [107], [], [14], [],
     [122], [], [62], [], [54], [], [70], [], [96], [], [11], [], [141], [], [129], [], [157], [], [136], [], [41], [],
     [40], [], [78], [], [141], [], [16], [], [137], [], [127], [], [19], [], [70], [], [15], [], [16], [], [65], [],
     [96], [], [157], [], [111], [], [87], [], [95], [], [52], [], [42], [], [12], [], [60], [], [17], [], [20], [],
     [63], [], [56], [], [37], [], [129], [], [67], [], [129], [], [106], [], [107], [], [133], [], [80], [], [8], [],
     [56], [], [72], [], [81], [], [143], [], [90], [], [0], []]

    for i in range(len(commands)):
        if commands[i] == 'addNum':
            s.addNum(val[i][0])
        elif commands[i] == 'findMedian':
            print(f"\n{s.findMedian()}\n")
            pass

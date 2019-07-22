from typing import List


class HeightEvent(object):

    def __init__(self, l, h):
        self.l = l
        self.h = h

    def __lt__(self, other):
        return self.h < other.h

    def __eq__(self, other):
        return self.h == other.h

    def __repr__(self):
        return str([self.l, self.h])


class Solution:

    def consolidate_stack(self, stack, item):
        if stack[-1][0] == item[0]:
            stack.pop()

        if stack[-1][1] != item[1]:
            stack.append(item)



    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = []

        for item in buildings:
            events.append([item[0], item[2]])
            events.append([item[1], item[2]])

        events = sorted(events, key=lambda x: x[0])

        height_stack = [HeightEvent(0, 0)]
        records = []

        for i in range(len(events)):
            item = events[i]
            new_event = HeightEvent(item[0], item[1])
            if new_event > height_stack[-1]:
                height_stack.append(HeightEvent(item[0], item[1]))
                records.append([item[0], item[1]])
            elif new_event < height_stack[-1]:
                for i in range(len(height_stack)):
                    if height_stack[i] == new_event:
                        height_stack.remove(height_stack[i])
                        break
                    if height_stack[i] > new_event:
                        height_stack = height_stack[:i] + [new_event] + height_stack[i:]
                        break
            elif new_event == height_stack[-1]:
                height_stack.pop()
                records.append([new_event.l, height_stack[-1].h])


        stack = []
        for item in records:
            if not stack:
                stack.append(item)
            else:
                self.consolidate_stack(stack, item)

        return stack




if __name__ == '__main__':
    s = Solution()

    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    # buildings = [[0, 2147483647, 2147483647]]

    # buildings = [[0, 1, 3]]
    #
    # buildings = [[0, 2, 3], [2, 5, 3]]

    buildings = [[2, 9, 10], [9, 12, 15]]

    print(s.getSkyline(buildings))

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        # find interval range
        lower = intervals[0][0]
        higher = intervals[0][1]
        for item in intervals:
            if item[0] < lower:
                lower = item[0]
            if item[1] > higher:
                higher = item[1]

        marker = [0] * (higher + 1)

        for item in intervals:
            # keep right open to enforce over lapping between intervals
            for j in range(item[0], item[1]):
                marker[j] = 1

        ret_val = []

        # handle single intervals with same open and close
        single_intervals = set([])
        for item in intervals:
            if item[0] == item[1]:
                if item[0] not in single_intervals and marker[item[0]] == 0:
                    if item[0] == 0:
                        single_intervals.add(item[0])
                        ret_val.append([item[0], item[1]])
                    elif marker[item[0] - 1] == 0:
                        single_intervals.add(item[0])
                        ret_val.append([item[0], item[1]])

        begin = False
        for i in range(lower, len(marker)):
            if not begin and marker[i] == 1:
                begin = True
                start = i
            if begin and marker[i] == 0:
                begin = False
                end = i
                ret_val.append([start, end])
        if begin:
            ret_val.append([start, higher])

        return ret_val


if __name__ == "__main__":
    s = Solution()

    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    #
    # intervals = [[1,4],[4,5]]

    # intervals = [[1,4],[5,6]]

    intervals = [[1, 4], [0, 0]]

    intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]

    print(s.merge(intervals))

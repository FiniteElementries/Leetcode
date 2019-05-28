from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        lower = intervals[0][0]
        higher = intervals[0][1]
        for item in intervals:
            if item[0] < lower:
                lower = item[0]
            if item[1] > higher:
                higher = item[1]

        offset = higher - lower + 1

        marker = [0] * offset

        for item in intervals:
            # keep right open to enforce over lapping between intervals
            for j in range(item[0], item[1]):
                marker[j - lower] = 1

        begin = False
        start = 0
        end = 0

        ret_val = []

        # handle single intervals with same open and close
        single_intervals = set([])
        for item in intervals:
            if item[0] == item[1]:
                if item[0] not in single_intervals and marker[item[0] - lower] == 0:
                    if item[0] - lower - 1 >= 0:
                        if marker[item[0] - lower - 1] == 0:
                            single_intervals.add(item[0])
                            ret_val.append([item[0], item[1]])
                    else:
                        single_intervals.add(item[0])
                        ret_val.append([item[0], item[1]])

        for i in range(0, len(marker)):
            if not begin and marker[i] == 1:
                begin = True
                start = i
            if begin and marker[i] == 0:
                begin = False
                end = i
                ret_val.append([start + lower, end + lower])
        if begin:
            ret_val.append([start + lower, len(marker) - 1 + lower])

        return ret_val


if __name__ == "__main__":
    s = Solution()

    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    #
    # intervals = [[1,4],[4,5]]

    # intervals = [[1,4],[5,6]]

    intervals = [[1, 4], [0, 0]]

    # intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]

    print(s.merge(intervals))

from collections import defaultdict
from typing import List


class Solution:

    def create_dict(self, equations, values):
        dic = defaultdict(lambda: defaultdict(lambda: None))
        for i, equ in enumerate(equations):
            dic[equ[0]][equ[1]] = values[i]
            dic[equ[1]][equ[0]] = 1 / values[i]
        return dic

    def find_answer(self, dic, nominator, demoninator, history_set):

        if dic[nominator][demoninator] is not None:
            return dic[nominator][demoninator]

        nominator_dic = dic[nominator]

        for k, v in nominator_dic.items():
            if k not in history_set and v is not None and v != -1:

                # dfs
                history_set.add(k)
                answer = self.find_answer(dic, k, demoninator, history_set)
                history_set.remove(k)

                if answer is not -1:
                    dic[nominator][demoninator] = answer * v
                    print(history_set)
                    break
        if dic[nominator][demoninator] is None:
            dic[nominator][demoninator] = -1
        return dic[nominator][demoninator]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = self.create_dict(equations, values)

        ret_val = []
        for q in queries:
            print(q[0], q[1])
            ret_val.append(self.find_answer(dic, q[0], q[1], set(q[0])))
        return ret_val


if __name__ == '__main__':
    s = Solution()

    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
    values = [3.0, 4.0, 5.0, 6.0]
    queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]

    equations = [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"]]
    values = [4.5, 2.3, 8.9, 0.44]
    queries = [["a", "c"], ["d", "f"], ["h", "e"], ["b", "e"], ["d", "h"], ["g", "f"], ["c", "g"]]

    print(s.calcEquation(equations, values, queries))

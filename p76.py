import heapq


class Solution:

    def create_index_map(self, t, s):
        index_map = {}
        for c in t:
            index_map[c] = []

        for i in range(0, len(s)):
            if s[i] in index_map:
                index_map[s[i]].append(i)

        return index_map

    def init_state(self, t, index_map):
        state = {}

        for c in t:
            if c not in state:
                if len(index_map[c]) == 0:
                    return None
                state[c] = [0, 0]
            else:
                if state[c][1] + 1 >= len(index_map[c]):
                    return None
                state[c] = [0, state[c][1] + 1]
        return state

    def add_new_item(self, heap, item, max_ind):
        if item > max_ind:
            max_ind = item
        heapq.heappush(heap, item)
        return max_ind

    def scan(self, t, s, index_map, state):

        heap = []

        # create initial max_ind and heap
        max_ind = -1
        for item in state:
            for i in range(state[item][0], state[item][1] + 1):
                actual_index = index_map[item][i]
                max_ind = self.add_new_item(heap, actual_index, max_ind)

        all_min_index = 0
        all_max_index = 0
        all_length = len(s)
        while True:
            min_ind = heapq.heappop(heap)

            if max_ind - min_ind + 1 <= all_length:
                all_min_index = min_ind
                all_max_index = max_ind
                all_length = max_ind - min_ind + 1

            c = s[min_ind]  # character from actual index

            # slide window at this ch forward
            i = state[c][0]
            j = state[c][1]
            state[c] = [i + 1, j + 1]

            # add new j+1 actual index to heap
            # j+1 is out of bound, stop
            if j + 1 >= len(index_map[c]):
                break
            actual_index = index_map[c][j + 1]
            max_ind = self.add_new_item(heap, actual_index, max_ind)

        return s[all_min_index:all_max_index + 1]

    def minWindow(self, s: str, t: str) -> str:
        index_map = self.create_index_map(t, s)
        state = self.init_state(t, index_map)

        if state is None:
            return ""

        return self.scan(t, s, index_map, state)


if __name__ == "__main__":
    s = Solution()

    S = "a"
    T = "aa"

    S = "ADOBECODEBANC"
    T = "AABC"

    S = "ADOBECODEBANC"
    T = "AABFC"

    S = 'aa'
    T = 'aa'

    print(s.minWindow(S, T))

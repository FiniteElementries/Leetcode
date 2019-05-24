class Solution:


    mapping = {}
    def find_potential_states(self, p, i):
        if i in self.mapping:
            return self.mapping[i]

        if i >= len(p):
            return {len(p)}

        states = set([i])
        if p[i] == '*':
            states.add(i-1)
            states = states.union(self.find_potential_states(p, i + 1))

        self.mapping[i] = states

        return states

    def isMatch(self, s: str, p: str) -> bool:
        self.mapping = {}
        if p == '':
            return s == p

        potential_states = self.find_potential_states(p, 0)

        for i in range(0, len(s)):
            current_states = set()

            for item in potential_states:
                if item < 0:
                    continue
                if item < len(p):
                    if s[i] == p[item]:
                        current_states.add(item)
                    if p[item] == '?':
                        current_states.add(item)
                    if p[item] == '*':
                        current_states.add(item)

            potential_states = set()

            for item in current_states:
                if p[item] == '*':
                    potential_states = potential_states.union(self.find_potential_states(p, item))
                else:
                    potential_states = potential_states.union(self.find_potential_states(p, item+1))

        for item in potential_states:
            if item >= len(p):
                return True
        return False


if __name__ == "__main__":
    so = Solution()

    # s = "aa"
    # p = "a"
    #
    # s = "aa"
    # p = "*"
    #
    # s = "cb"
    # p = "?a"

    # s = "adceb"
    # p = "*a*b"

    # s = "acdcb"
    # p = "a*c?b"

    # s = 'aa'
    # p = 'aa'
    #
    s = 'aa'
    p = '*'

    # s = 'a'
    # p = 'a*'
    print(so.isMatch(s, p))

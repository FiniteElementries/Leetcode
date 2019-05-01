class Solution:

    transition_state = []


    def dfs(self, pattern, position):
        if position >= len(pattern):
            return [-1]
        ret_state = [position]
        if pattern[position] == '*':
            ret_state.append(position - 1)
            ret_state.extend(self.dfs(pattern, position + 1))
        if position<len(pattern)-1:
            if pattern[position+1] == '*':
                ret_state.extend(self.dfs(pattern, position + 1))
        return ret_state

    def isMatch(self, s, p):

        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False

        # for i in range(len(p)):
        #     if p[i] != "*":
        #         self.transition_state[i] = [i+1]
        #     else:
        #         self.transition_state[i] = [i-1, i+1]


        # look through text to update state
        current_states = self.dfs(p, 0)
        for i in range(len(s)):
            next_states = []
            for state in current_states:
                if state == -1:
                    continue
                state_char = p[state]
                # if match populate next possible states
                if s[i] == state_char or state_char == ".":
                    next_states.extend(self.dfs(p, state + 1))

            current_states = next_states

            if len(current_states) == 0:
                return False

        return -1 in current_states


so = Solution()

s = "aa"
p = "a"

s = "aba"
p = "a*"
# #
s = "aaa"
p = ".*"

s = "aab"
p = "c*a*b"

s = "mississippi"
p = "mis*is*ip*."

# todo build transient state table before doing dfs
s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*a*a*b"

print(so.isMatch(s, p))

class Solution:

    def longestValidParentheses(self, s: str) -> int:

        max_l = 0

        start_index_stack = [-1]

        for i in range(0, len(s)):
            if s[i] == '(':
                start_index_stack.append(i)
            else:
                if (len(start_index_stack)) > 1 and s[start_index_stack[-1]] == '(':
                    start_index_stack.pop()
                    l = i - start_index_stack[-1]
                    max_l = max(max_l, l)

                else:
                    start_index_stack.append(i)

        return max_l


if __name__ == '__main__':
    s = Solution()

    st = "()()"

    # st = ')('

    st = "(()"

    # st = ")()())"
    st = "()(()"

    # st = "(()()"

    # st = "()(())"
    st = ")))"

    st = "(()"

    print(s.longestValidParentheses(st))



class Solution:

    mapping = { '(': ')',
                '{': '}',
                '[': ']'}

    def isValid(self, s: str) -> bool:

        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack)<=0:
                    return False
                if c == self.mapping[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True

if __name__=="__main__":
    s = Solution()

    ss = "()[]{}"
    ss = "([)]"
    print(s.isValid(ss))

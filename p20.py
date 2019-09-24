class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for item in s:
            if len(stack) == 0:
                stack.append(item)
            else:
                if item in {'{', '(', '['}:
                    stack.append(item)
                else:
                    if item == '}':
                        if stack[-1] != '{':
                            return False
                        else:
                            stack.pop()
                    elif item == ')':
                        if stack[-1] != '(':
                            return False
                        else:
                            stack.pop()
                    elif item == ']':
                        if stack[-1] != '[':
                            return False
                        else:
                            stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()

    ss = "()[]{}"
    ss = "([)]"
    print(s.isValid(ss))

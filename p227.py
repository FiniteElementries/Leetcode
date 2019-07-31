class Solution(object):

    def do_operation(self, num_stack, sign_stack):
        sign = sign_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        if sign == '+':
            res = num1 + num2
        elif sign == '-':
            res = num1 - num2
        elif sign == '/':
            res = num1 // num2
        else:
            res = num1 * num2
        num_stack.append(res)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", '')

        num_stack = []
        sign_stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                number = ''
                while s[i].isdigit():
                    number += s[i]
                    i += 1
                    if i >= len(s):
                        break
                num_stack.append(int(number))
            else:
                if not sign_stack:
                    sign_stack.append(s[i])
                else:
                    while sign_stack:
                        if (s[i] == '*' or s[i] == '/') and (sign_stack[-1] != '/' and sign_stack[-1] != '*'):
                            break
                        self.do_operation(num_stack, sign_stack)

                    sign_stack.append(s[i])
                i += 1

        while sign_stack:
            self.do_operation(num_stack, sign_stack)

        return num_stack[-1]


if __name__ == '__main__':
    s = Solution()

    st = "3+2*2"
    st = "1*2-3/4+5*6-7*8+9/10"
    st = "100000000/1/2/3/4/5/6/7/8/9/10"
    # st = "1+2*5/3+6/4*2"
    print(s.calculate(st))

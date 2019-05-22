'''

Google面试题目 leetcode 772 Basic Calculator III
输入数字，加减乘除，还有括号， 求解表达式
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
输入一定是合法表达式， 其中的数字是非负整数， 任何中间结果和最后都不会溢出整数
'''


class Solution(object):

    order = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '(': -1
    }

    def convert_to_prefix(self, s):

        stack = []
        prefixFormat = []

        num = ''
        for i in range(0, len(s)):

            if s[i].isdigit():
                num += s[i]
            else:
                if num != '':
                    prefixFormat.append(int(num))
                    num = ''
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    if s[i] == '(':
                        stack.append(s[i])
                    elif s[i] == ')':
                        while stack[-1] != '(':
                            prefixFormat.append(stack[-1])
                            del stack[-1]
                        del stack[-1]
                    else:
                        if self.order[stack[-1]]<self.order[s[i]]:
                            stack.append((s[i]))
                        else:
                            while len(stack)>0 and self.order[stack[-1]] > self.order[s[i]]:
                                prefixFormat.append(stack[-1])
                                del stack[-1]
                            stack.append(s[i])
        if num!='':
            prefixFormat.append(int(num))
        while len(stack)>0:
            prefixFormat.append(stack[-1])
            del stack[-1]
        return prefixFormat

    def calculate(self, s):
        s = s.replace(" ", '')
        prefix = self.convert_to_prefix(s)

        stack = []
        for item in prefix:
            if isinstance(item, int):
                stack.append(item)
            else:
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                if item == '+':
                    c = a+b
                elif item == '-':
                    c = b-a
                elif item == '/':
                    c = b/a
                else:
                    c = a*b
                stack.append(c)
        return stack[-1]




if __name__=="__main__":
    s = Solution()

    st = "1 + 1"
    st = " 6-4 / 2 "
    st = "2*(5+5*2)/3+(6/2+8)"
    st = "(2+6* 3+5- (3*14/7+2)*5)+3"
    print(s.calculate(st))

class Solution:
    def fizzBuzz(self, n: int):
        ret_val = []
        for i in range(1, n+1):
            s = ""
            three_div = (i % 3 == 0)
            five_div = (i % 5 == 0)
            if three_div:
                s += "Fizz"
            if five_div:
                s += "Buzz"
            if not three_div and not five_div:
                s += str(i)
            ret_val.append(s)
        return ret_val

if __name__ == "__main__":

    s = Solution()
    print(s.fizzBuzz(1))


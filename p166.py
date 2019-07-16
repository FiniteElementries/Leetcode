class Solution(object):

    def div(self, num, den):

        if num == 0:
            return 0, 0, 1

        scale = 1
        while num < den:
            num *= 10
            scale *= 10

        remain = num % den
        factor = num // den
        return factor, remain, scale

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator < 0:
            sign = "-"
        else:
            sign = ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        # f, r, s = self.div(numerator, denominator)
        r = 1
        digits = set([])
        less_than_zero = False
        total = ''
        while r != 0:
            f, r, s = self.div(numerator, denominator)
            if s == 1:
                total += str(f)
            else:

                if not less_than_zero:
                    less_than_zero = True
                    if len(total) == 0:
                        total += "0"
                    total += '.'

                # construct string after decimal point
                sf = str(f)
                s /= 10
                while s > 1:
                    sf = '0' + sf
                    s /= 10

                # check if f in digits already if yes, do replacedment and return
                if (f, r) in digits:
                    d = total.find(".")
                    ind = total.find(sf, d)
                    pat = total[ind:]
                    total = total.replace(pat, "(" + pat + ")")
                    break

                total += sf

                digits.add((f, r))

            numerator = r

        return sign + total


if __name__ == "__main__":
    s = Solution()

    numerator = 1
    denominator = 2

    # numerator = 2
    # denominator = 1

    # numerator = 2
    # denominator = 3

    numerator = 4
    denominator = 333

    numerator = 1
    denominator = 17

    # numerator = 1
    # denominator = 6

    numerator = 0
    denominator = 3

    numerator = -50
    denominator = 8

    numerator = 7
    denominator = -12

    numerator = 214748364737
    denominator = 37

    print(s.fractionToDecimal(numerator, denominator))

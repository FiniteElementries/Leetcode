class Solution:

    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while i<j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1
        return s


if __name__ == "__main__":

    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
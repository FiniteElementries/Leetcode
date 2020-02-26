class Solution:
    def reverseWords(self, s: str) -> str:

        arr = []
        item = ""
        for c in s:
            # if c is space, add item to list
            if c == " ":
                if len(item)>0:
                    arr.append(item)
                    item = ''
            else:
                item += c
            # else add c to item
        if len(item) > 0:
            arr.append(item)
        arr.reverse()
        return ' '.join(arr)





if __name__ == '__main__':
    s = Solution()
    st = "the sky is blue"
    st = "  hello world!  "
    print(s.reverseWords(st))

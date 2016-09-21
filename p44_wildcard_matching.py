class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        p= p + ' '
        s= s + ' '

        p = p[:-1]
        s = s[:-1]

        if(p[0]=='*'):
            s = 't' + s
            p = 't' + p

        if(p[-1]=='*'):
            p = p + 't'
            s = s + 't'

        phrase = p.split('*')

        for item in phrase:
            if(not '?' in item):
                f = s.find(item)
                if(f==-1):
                    return False
                else:
                    s = s[f+1:]
            else:
                sub_items = item.split('?')

                f = s.find(sub_items[0])
                if(f==-1):
                    return False
                else:
                    s = s[f+len(sub_items[0])+1:]

                for i in range(1, len(sub_items)):
                    if(not s.startswith(sub_items[i])):
                        return False
                    else:
                        s = s[len(sub_items[i])+1:]



        return  True







if __name__=="__main__":
    s = Solution()

    print(s.isMatch("abefcdgiescdfimde","ab*cd?i*de"))
    print(s.isMatch("aa", "*"))
    print(s.isMatch("hi", "*?"))
    print(s.isMatch("a", "aa"))
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "*"))
    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("ab", "?*"))

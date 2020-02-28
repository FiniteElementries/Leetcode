class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        i = 0
        last_insert_location = 0
        previous_copy_location = 0
        # search forward
        while i < len(S):
            if S[i].isdigit():
                previous_copy_location = last_insert_location
                last_insert_location = last_insert_location * (int(S[i]))
                # K is in repeated String between previous_current_ind and current_ind
                if last_insert_location >= K:
                    break
            else:
                last_insert_location += 1
                if last_insert_location == K:  # K is in new appended string
                    return S[i]
            i += 1

        # search backward recursively, new K should be K - last str length
        # consider last string has length 25 and K is 28, when last string is copied, we need to count 3 more
        # characters after end of last string, which is also beginning of last string
        # check between previous_current_id and current_id
        return self.decodeAtIndex(S, K-previous_copy_location)

if __name__ == '__main__':
    so = Solution()
    S = "leet2code3"
    K = 10

    S = "a2345678999999999999999"
    K = 1
    print(so.decodeAtIndex(S, K))

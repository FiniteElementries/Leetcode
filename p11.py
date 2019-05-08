class Solution:


    def find_volume(self, height, i, j):

        # move lower end of sides
        if height[i]<height[j]:
            min_height = height[i]
            move_i = True
        else:
            min_height = height[j]
            move_i = False

        return (j-i) * min_height, min_height, move_i

    def maxArea(self, height):

        i=0
        j=len(height)-1

        max_vol, vol_height, move_i = self.find_volume(height, i, j)

        while i<j:
            if move_i:
                i += 1
                if height[i]>vol_height:
                    # check volume
                    vol, new_height, move_i = self.find_volume(height, i, j)
                    if vol>max_vol:
                        max_vol = vol
                        vol_height = new_height
            else:
                j -= 1
                if height[j]>vol_height:
                    # check volume
                    vol, new_height, move_i = self.find_volume(height, i, j)
                    if vol>max_vol:
                        max_vol = vol
                        vol_height = new_height

        return max_vol


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(s.maxArea([2,3,10,5,7,8,9]))
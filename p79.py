from typing import List


class Solution:
    m = 0
    n = 0

    def find_word(self, board, marker, word, i, j, k):
        if i < 0 or i >= self.m:
            return False

        if j < 0 or j >= self.n:
            return False

        if marker[i][j] == 1:
            return False

        if board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        marker[i][j] = 1
        if self.find_word(board, marker, word, i + 1, j, k + 1):
            return True
        if self.find_word(board, marker, word, i - 1, j, k + 1):
            return True
        if self.find_word(board, marker, word, i, j + 1, k + 1):
            return True
        if self.find_word(board, marker, word, i, j - 1, k + 1):
            return True

        marker[i][j] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        marker = [[0] * self.n for _ in range(self.m)]
        for i in range(0, self.m):
            for j in range(0, self.n):
                if self.find_word(board, marker, word, i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCCED"
    # word = "SEE"
    # word = "ABCB"

    print(s.exist(board, word))

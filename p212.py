from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        node = self.head
        for c in list(word):
            if c in node:
                node = node[c]
            else:
                node[c] = dict()
                node = node[c]
        node['word_mark'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.head

        for c in list(word):
            if c in node:
                node = node[c]
            else:
                return False

        return 'word_mark' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.head

        for c in list(prefix):
            if c in node:
                node = node[c]
            else:
                return False
        return True


class Solution:
    solutions = set()

    def dfs(self, word, i, j, board):
        if i < 0 or i >= len(board):
            return
        if j < 0 or j >= len(board[0]):
            return

        if board[i][j] is None:
            return

        word = word + board[i][j]

        w = board[i][j]
        board[i][j] = None

        if self.trie.search(word):
            self.solutions.add(word)

        if self.trie.startsWith(word):
            self.dfs(word, i - 1, j, board)
            self.dfs(word, i + 1, j, board)
            self.dfs(word, i, j - 1, board)
            self.dfs(word, i, j + 1, board)

        board[i][j] = w

    def search_word(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                self.dfs('', i, j, board)
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        self.solutions = set()

        self.search_word(board)

        return list(self.solutions)


if __name__ == '__main__':
    s = Solution()

    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    print(s.findWords(board, words))

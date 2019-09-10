class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")

        path_stack = []

        for item in paths:
            if item == '..':
                if path_stack:
                    path_stack.pop()
            elif item == '.' or item == '':
                pass
            else:
                path_stack.append(item)

        return '/' + '/'.join(path_stack)


if __name__ == '__main__':

    s = Solution()
    path = "/../"
    print(s.simplifyPath(path))
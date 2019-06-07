from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        row = [1]

        for i in range(0, numRows):
            rows.append(row)

            new_row = [1]
            for j in range(0, len(row)-1):
                new_row.append(row[j] + row[j+1])
            new_row.append(1)

            row = new_row

        return rows

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visit = set()

        def bfs(coordinate):

            queue = deque()
            queue.append(coordinate)

            count = 0
            
            while queue:

                coordinate = queue.popleft()

                if coordinate in visit:
                    continue

                x, y = coordinate

                c1 = x >=0 and x < len(grid)
                c2 = y >=0 and y < len(grid[0])

                if c1 and c2:
                    value = grid[x][y]
                else:
                    value = 0
                

                if value == 1:
                    count += 1

                    queue.append((x + 1, y))
                    queue.append((x - 1, y))
                    queue.append((x, y + 1))
                    queue.append((x, y - 1))

                    visit.add(coordinate)

            return count

        rows, columns = len(grid), len(grid[0])
        max_area = 0

        for i in range(rows * columns):

            r = i // columns
            c = i % columns

            c1 = grid[r][c] == 1
            c2 = (r,c) not in visit

            if c1 and c2:
                max_area = max(bfs((r,c)) , max_area)

        return max_area

        
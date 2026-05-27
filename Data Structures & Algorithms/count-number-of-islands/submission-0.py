from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited_area = {}

        def bfs(queue):
            
            count = 0

            while queue:

                coordinate = queue.popleft()
                i,j = coordinate

                if coordinate in visited_area:
                    continue

                c1 = i >= 0 and i < len(grid)
                c2 = j >= 0 and j < len(grid[0])

                if c1 and c2:
                    value = grid[i][j]
                else:
                    value = "0"

                if value == "1":
                    count += 1
                    visited_area[coordinate] = True

                    queue.append((i + 1, j))
                    queue.append((i, j + 1))
                    queue.append((i - 1, j))
                    queue.append((i , j - 1))

            return count

        rows, columns = len(grid), len(grid[0])

        for i in range(rows * columns):
            r = i // columns
            c = i % columns

            coordinate = (r,c)
            value = grid[r][c]

            if coordinate in visited_area :
                continue

            queue = deque()
            queue.append(coordinate)
            
            if value == "1":
                print('Initiating', coordinate)
                count = bfs(queue)
                print('Number of lands', count)
                islands += 1

            else:
                visited_area[coordinate] = True
        
        return islands




            

        
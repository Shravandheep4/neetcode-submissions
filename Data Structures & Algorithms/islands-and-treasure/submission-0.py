class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    
        max_value = 2147483647


        def bfs(coordinate, grid):

            visit = set()

            queue = deque()
            queue.append(coordinate)

            while queue:
                
                coordinate, distance = queue.popleft()

                if coordinate in visit:
                    continue
                
                x, y = coordinate
                c1 = x >= 0 and x < len(grid)
                c2 = y >= 0 and y < len(grid[0])

                if c1 and c2:
                    value = grid[x][y]
                else:
                    value = -1

                # Case 1
                if value == -1:
                    continue
                
                # Case 2
                grid[x][y] = min(distance, value)
                distance += 1

                queue.append(((x + 1, y), distance))
                queue.append(((x - 1, y), distance))
                queue.append(((x, y + 1), distance))
                queue.append(((x, y - 1), distance))

                visit.add(coordinate)

            return grid

        rows, columns = len(grid), len(grid[0])

        for i in range(rows * columns):

            x = i // columns
            y = i % columns

            if grid[x][y] == 0:
                coordinate = (x, y)
                grid = bfs((coordinate, 0), grid)

        return grid
        
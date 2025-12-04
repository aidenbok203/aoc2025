with open("d04/data.txt", "r") as f:
    grid = f.read().splitlines()
    grid = [list(row) for row in grid]

valid = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        count = 0
        if grid[i][j] == "@":
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[i]):
                            if grid[i + dx][j + dy] == "@":
                                count += 1

            if count < 4:
                valid += 1


print(valid)
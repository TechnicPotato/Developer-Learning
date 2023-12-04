def symbol(char:chr):
    return (not char.isdigit() and char != '.')

def grabId(grid:list):
    totalScore = 0
    x = 0
    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[0]):
            if grid[y][x].isdigit():
                valid = False
                value = ""
                while x < len(grid[0]) and grid[y][x].isdigit():
                    value += grid[y][x]
                    # Logic to check around for validity
                    # Scan above
                    if y != 0:
                        valid = valid or symbol(grid[y-1][x])
                        if x != 0:
                            valid = valid or symbol(grid[y-1][x-1])
                        if x != len(grid[0]) - 1:
                            valid = valid or symbol(grid[y-1][x+1])
                    # Scan left
                    if x != 0:
                        valid = valid or symbol(grid[y][x-1])
                    # Scan right
                    if x != len(grid[0]) - 1:
                        valid = valid or symbol(grid[y][x+1])
                    # Scan below
                    if y != len(grid) - 1:
                        valid = valid or symbol(grid[y+1][x])
                        if x != 0:
                            valid = valid or symbol(grid[y+1][x-1])
                        if x != len(grid[0]) - 1:
                            valid = valid or symbol(grid[y+1][x+1])
                    x += 1

                if valid:
                    print(totalScore)
                    totalScore += int(value)
            x += 1
        y += 1
    return totalScore
if __name__ == "__main__":
    totalSum = 0
    
    with open("input.txt", "r") as inputFile:
        grid = []
        for line in inputFile:
            grid.append([char for char in line.rstrip('\n')])
    print(grabId(grid))
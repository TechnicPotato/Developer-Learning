# Scan the grid, looking for numbers and gears
def gearScanner(grid:list):
    gears = []
    numbers = {}
    y = 0
    for line in grid:
        line += '|'
        print(line)
        x = 0
        value = ""
        # Stores the coords of the current number.
        cache = []
        for char in line:
            if char in "0123456789":
                value += char
                cache.append(x)
            elif char == '*':
                gears.append((y,x))
                if cache:
                    for i in cache:
                        numbers[(y,i)]=int(value)
                value = ""
                cache = []
            else:
                if cache:
                    for i in cache:
                        numbers[(y,i)]=int(value)
                value = ""
                cache = []
            x += 1
        y += 1
    return numbers, gears

# Find the geared values based on coords
def scoring(num:dict, gears:list):
    totalScore = 0
    for y,x in gears:
        values = set()
        for i in [(y-1,x-1), (y-1,x), (y-1, x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x), (y+1,x+1)]:
            if i in num.keys():
                values.add(num[i])
        if len(values) >=2:
            # print(sorted(values))
            score = 1
            for i in values:
                score *= i
            totalScore += score
    return totalScore


if __name__ == "__main__":
    totalSum = 0
    
    with open("input.txt", "r") as inputFile:
        grid = []
        for line in inputFile:
            grid.append([char for char in line.rstrip('\n')])
    num, gears = gearScanner(grid)
    # print([i for i in num if num[i] == 154])
    print(scoring(num, gears))
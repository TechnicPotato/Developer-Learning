cubes = {
    "red" : 0,
    "green" : 0,
    "blue" : 0
}

def count(line:str, cubes:dict):
    for game in line.split(';'):
        for item in game.split(','):
            number, value = item.lstrip(' ').split(' ')
            if cubes[value] < int(number):
                cubes[value] = int(number)
    return cubes['red'] * cubes['green'] * cubes['blue']

if __name__ == "__main__":
    totalSum = 0
    
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            id, data = line.lstrip("Game ").rstrip('\n').split(':')
            totalSum += count(data, cubes.copy())
    print(totalSum)
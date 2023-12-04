cubes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def count(line:str, cubes:dict):
    """Counts the cubes in a line and returns if the game is
    possible based on the cube count.

    Args:
        line (str): Line for cubes to count
        cubes (dict): Dictionary to validate against

    Returns:
        bool: if the game is possible.
    """
    for game in line.split(';'):
        for item in game.split(','):
            number, value = item.lstrip(' ').split(' ')
            if cubes[value] < int(number):
                return False
    return True

if __name__ == "__main__":
    totalSum = 0
    
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            id, data = line.lstrip("Game ").rstrip('\n').split(':')
            if count(data, cubes):
                totalSum += int(id)
    print(totalSum)
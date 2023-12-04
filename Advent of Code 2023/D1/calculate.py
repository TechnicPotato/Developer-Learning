def findFirstNumber(line:str):
    """Grabs the first number found reading left to right
    in a string.

    Args:
        line (str): line to obtain the first number from.

    Raises:
        TypeError: Raised if there is no number found within the string

    Returns:
        int: The first number found within the string.
    """
    #  First Part
    # for char in line:
    #     if char.isdigit():
    #         return int(char) \
    numbers = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    ptr = 0
    while ptr < len(line):
        if line[ptr].isdigit():
            return int(line[ptr])
        else:
            for key in numbers.keys():
                if line[ptr:].startswith(key):
                    return numbers[key]
        ptr += 1
        
def findLastNumber(line:str):
    """Grabs the first number found reading left to right
    in a string.

    Args:
        line (str): line to obtain the first number from.

    Raises:
        TypeError: Raised if there is no number found within the string

    Returns:
        int: The first number found within the string.
    """
    #  First Part
    # for char in line:
    #     if char.isdigit():
    #         return int(char) \
    numbers = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    ptr = len(line) - 1
    while ptr >= 0:
        if line[ptr].isdigit():
            return int(line[ptr])
        else:
            for key in numbers.keys():
                if line[ptr:].startswith(key):
                    return numbers[key]
        ptr -= 1

if __name__ == "__main__":
    totalSum = 0
    
    with open('input.txt', 'r') as inputFile:
        for line in inputFile:
            line = line.rstrip('\n')
            # score = findFirstNumber(line) * 10 + findFirstNumber(line[::-1])
            score = findFirstNumber(line) * 10 + findLastNumber(line)
            totalSum += score
            print("{line}, {score}".format(line=line, score=score))
    print("----------------")
    print(totalSum)
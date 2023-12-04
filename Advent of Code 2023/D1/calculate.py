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
    for char in line:
        if char.isdigit():
            return int(char) 
    raise TypeError("No Number in String")

if __name__ == "__main__":
    totalSum = 0
    
    with open('input.txt', 'r') as inputFile:
        for line in inputFile:
            score = findFirstNumber(line) * 10 + findFirstNumber(line[::-1])
            totalSum += score
            print("{line}, {score}".format(line=line.rstrip('\n'), score=score))
    print("----------------")
    print(totalSum)
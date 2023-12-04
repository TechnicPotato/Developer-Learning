if __name__ == "__main__":
    totalCount = {
    }
    for i in range(1,198):
        totalCount[i] = 1
    
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            point = 0
            card, data = line.lstrip("Card ").split(":")
            winning, numbers = data.split(" | ")
            for i in numbers.rstrip().split():
                if i in winning.lstrip().rstrip().split():
                    point += 1
                    
            for i in range(1, point+1):
                # Iterations
                for j in range(0, totalCount[int(card)]):
                    totalCount[i+int(card)] += 1
            # print(totalCount)
    print(sum(totalCount.values()))
                        
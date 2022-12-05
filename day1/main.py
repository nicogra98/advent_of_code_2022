from doctest import ELLIPSIS_MARKER


def part_1(calories):
    currentSum = 0
    maxSum = float("-inf")
    for calorie in calories:
        if calorie != "":
            currentSum += int(calorie)
            maxSum = max(maxSum, currentSum)
        else:
            currentSum = 0
    return maxSum

def part_2(calories):
    elves = []
    currentSum = 0
    for calorie in calories:
        if calorie != "":
            currentSum += int(calorie)
        else:
            elves.append(currentSum)
            currentSum = 0
    elves.append(currentSum)
    return sum(sorted(elves,reverse=True)[:3])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        calories = f.read().split("\n")
        
        print(part_1(calories))
        print(part_2(calories))
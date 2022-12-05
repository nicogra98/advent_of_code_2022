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

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        calories = f.read().split("\n")
        
        print(part_1(calories))
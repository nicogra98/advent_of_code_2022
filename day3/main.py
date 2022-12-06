def part_1 (rucksacks):
    priority = 0
    for rucksack in rucksacks:
        half = int(len(rucksack) / 2)
        top, bottom = rucksack[:half], rucksack[half:]

        for letter in top:
            if letter in bottom:
                print(letter)
                if ord(letter) >= 97:
                    priority += (ord(letter) - ord("a") + 1)
                    break
                else:
                    priority += (ord(letter) - ord("A") + 27)
                    break
    return priority


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        rucksacks = f.read().split("\n")

        print(ord("b") - ord("a") + 1)
        print(part_1(rucksacks))
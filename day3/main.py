def part_1 (rucksacks):
    priority = 0
    for rucksack in rucksacks:
        half = int(len(rucksack) / 2)
        top, bottom = rucksack[:half], rucksack[half:]

        for letter in top:
            if letter in bottom:
                if ord(letter) >= 97:
                    priority += (ord(letter) - ord("a") + 1)
                    break
                else:
                    priority += (ord(letter) - ord("A") + 27)
                    break
    return priority
    
def part_2(rucksacks):
    priority = 0

    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        letter = next(iter(common))

        if ord(letter) >= 97:
            priority += (ord(letter) - ord("a") + 1)
        else:
            priority += (ord(letter) - ord("A") + 27)

    return priority



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        rucksacks = f.read().split("\n")

        print(part_1(rucksacks))
        print(part_2(rucksacks))
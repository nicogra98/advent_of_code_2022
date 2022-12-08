def part_1 (pairs):
    count = 0

    for section1, section2 in pairs:
        section1 = [int(section) for section in section1.split("-")]
        section2 = [int(section) for section in section2.split("-")]

        if section1[0] <= section2[0] and section1[1] >= section2[1]:
            count += 1
        elif section2[0] <= section1[0] and section2[1] >= section1[1]:
            count += 1

    return count
    
def part_2(pairs):
    count = 0

    for section1, section2 in pairs:    
        section1 = [int(section) for section in section1.split("-")]
        section2 = [int(section) for section in section2.split("-")]
        
        a, b = sorted([section1, section2])

        if a[1] >= b[0]:
            count += 1

    return count



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        pairs = [pair.split(",") for pair in f.read().split("\n")]
        print(part_1(pairs))
        print(part_2(pairs))
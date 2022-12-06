SCORES = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

WINNER = {
    "Rock": "Paper", # A -> Rock loses against paper Y
    "Paper": "Scissors", # B -> Paper loses against scissors Z
    "Scissors": "Rock" # C -> Scissors loses against rock X
}

LOSER = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

EQUIVALENT = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

def part_1(games):
    score = 0
    for play in games:
        player1, player2 = play.split(" ")
        player1, player2 = EQUIVALENT[player1], EQUIVALENT[player2]
        score += SCORES[player2]

        if WINNER[player1] == player2:
            score += 6
        elif player1 == player2:
            score += 3
    
    return score

def part_2(games):
    score = 0
    for play in games:
        player1, player2 = play.split(" ")
        player1 = EQUIVALENT[player1]

        if player2 == "X":
            score += 0
            score += SCORES[LOSER[player1]]
        elif player2 == "Y":
            score += 3
            score += SCORES[player1]
        else:
            score += 6
            score += SCORES[WINNER[player1]]
    
    return score

    
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        games = f.read().split("\n")

    print(part_1(games))
    print(part_2(games))

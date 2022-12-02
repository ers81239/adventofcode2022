"""
A/X-Rock Points 1
B/Y-Paper Points 2
C/Z-Scissors Points 3

0 Points loss
3 Points draw
6 Points win

Round score = What you played score + win/loss score

"""

play_points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

losses = ["ZA", "XB", "YC"]
ties = ["XA", "YB", "ZC"]
wins = ["YA", "ZB", "XC"]

labels = {
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors",
    "X":"Rock",
    "Y":"Paper",
    "Z":"Scissors"
}


def score_round(my_play, their_play):
    # Score for play
    play_score = play_points[my_play]

    # Score for win
    play = f"{my_play}{their_play}"
    if play in wins:
        win_score = 6
        win_text = "beats"
    elif play in ties:
        win_score = 3
        win_text = "ties"
    elif play in losses:
        win_score = 0
        win_text = "loses to"
    else:
        raise ValueError("play {play} not scored")

    print(f"{labels[my_play]} {win_text} {labels[their_play]}.  Play score: {play_score} Win score: {win_score}")

    return play_score + win_score


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total_score = 0
for line in lines:
    their_play, my_play = line.split()
    total_score += score_round(my_play, their_play)
    print(f"Total score: {total_score}")








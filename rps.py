"""
May the best player win
"""
msg = input("How was your day? Reply in 5 words or more : ")
player = input("rock, paper, or scizzors : ")
message_number= len(msg)
random_number = float(message_number)* float(9)
if random_number <= 200:
    computer = ("scizzors")
elif random_number >200 and random_number<400:
    computer = ("rock")
elif random_number>400:
    computer = ("paper")
if computer == "scizzors" and player == "rock":
    print("You played rock, computer played scizzors")
    print("You win!!")
if computer == "scizzors" and player == "paper":
    print("You played paper, computer played scizzors")
    print("You lose!!")
if computer == "scizzors" and player == "scizzors":
    print("You played scizzors, computer played scizzors")
    print("You tie!!")
if computer == "rock" and player == "rock":
    print("You played rock, computer played rock")
    print("You Tie!!")
if computer == "rock" and player == "paper":
    print("You played paper, computer played rock")
    print("You Win!!")
if computer == "rock" and player == "scizzors":
    print("You played scizzors, computer played Rock")
    print("You Lose!!")
if computer == "paper" and player == "rock":
    print("You played rock, computer played paper")
    print("You lose!!")
if computer == "paper" and player == "paper":
    print("You played paper, computer played paper")
    print("You tie!!")
if computer == "paper" and player == "scizzors":
    print("You played scizzors, computer played paper")
    print("You win!!")
go_again = input("Great Game! Care to play again? (Say yes or no) :")
if go_again == "no":
    print("Have a great day!")
elif go_again =="yes":
    msg = input("What was the funniest thing that happened to you today? (answer in 5 or more words): ")
    player = input("rock, paper, or scizzors : ")
    message_number= len(msg)
    random_number = float(message_number)* float(9)
    if random_number <= 200:
     computer = ("scizzors")
    elif random_number >200 and random_number<400:
        computer = ("rock")
    elif random_number>400:
        computer = ("paper")
    if computer == "scizzors" and player == "rock":
        print("You played rock, computer played scizzors")
        print("You win!!")
    if computer == "scizzors" and player == "paper":
        print("You played paper, computer played scizzors")
        print("You lose!!")
    if computer == "scizzors" and player == "scizzors":
        print("You played scizzors, computer played scizzors")
        print("You tie!!")
    if computer == "rock" and player == "rock":
        print("You played rock, computer played rock")
        print("You Tie!!")
    if computer == "rock" and player == "paper":
        print("You played paper, computer played rock")
        print("You Win!!")
    if computer == "rock" and player == "scizzors":
        print("You played scizzors, computer played Rock")
        print("You Lose!!")
    if computer == "paper" and player == "rock":
        print("You played rock, computer played paper")
        print("You lose!!")
    if computer == "paper" and player == "paper":
        print("You played paper, computer played paper")
        print("You tie!!")
    if computer == "paper" and player == "scizzors":
        print("You played scizzors, computer played paper")
        print("You win!!")

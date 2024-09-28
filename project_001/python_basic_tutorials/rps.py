import random


def play():
    print("Rock Paper scissors ! lets go")
    player =  input("whats ur choice ? r for rock , p for paper , s for scissors ")
    print(player)
    if player not in ["r", "p","s"]:
        print("wrong option ")
        quit()
    
    comp = random.choice(["r", "p", "s"])
    print("comp "+ comp)

    is_user_win(player, comp)


def is_user_win(player, opponent):
    if (player == opponent):
        print("its a tie!")

    if (player == 'r' and opponent == "s") or (player == "p" and opponent=="r") or (player =="s" and opponent=="p"):
        print("You win")

    else:
        print("you lost")

play()
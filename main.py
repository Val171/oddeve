import time
from random import randint, choice
import random


#toss


def enter_number():
    global a, b
    a = int(input("Enter Number 1-6: "))
    b = randint(1, 6)
    time.sleep(1)

def play():
    global a, b, play_choice, player_score, bot_score, bot_choice

    if not checkifout():
        if play_choice == "bat":
            if a > 6:
                print("NOT VALID")
            else:
                player_score += a
            print(f"Your Score: {player_score}\n")
        elif play_choice == "ball":
            if a > 6:
                print("NOT VALID")
            else:
                bot_score += b
            print(f"Bot Score: {bot_score}\n")
    else:
        pass

def checkifout():
    global a, b, play_choice, player_score, bot_score, bot_choice, first_round, second_round

    if a == b and first_round:
        print("OUT!\nRoles switch\n")
        if play_choice == "bat":
            play_choice = "ball"
            bot_choice = "bat"
            print(f"bot_score: {bot_score}, To_Win: {player_score + 1}\n")
        else:
            play_choice = "bat"
            bot_choice = "ball"
            print(f"To_Win: {bot_score + 1}, your_score: {player_score}\n")
        time.sleep(1)
        first_round = False
        return True

    if a == b and second_round:
        print("OUT!")
        time.sleep(1)
        if bot_score >= player_score:
            print(f"\nYOU LOSE\nYour score: {player_score}\n\nBot Score: {bot_score}\n\nGIT GUD SON")
        else:
            print(f"YOU WIN\nYour score: {player_score}\n\nBot Score: {bot_score}")
        second_round = False
        return True

    if second_round and player_score >= bot_score:
        time.sleep(1)
        print(f"\nGGS YOU WIN\nYour score: {player_score}\nBot Score: {bot_score}")

        second_round = False
        return True

    elif second_round and bot_score >= player_score:
        print(f"YOU LOSE\n\nYour score: {player_score}\nBot Score: {bot_score}\n\nGIT GUD SON")
        second_round = False
        return True

play_again = True

while play_again:

    player_score = 0
    bot_score = 0
    bat_ball = ["ball", "bat"]
    second_round = False
    first_round = True

    while True:
        choice = input("Choose: Odd or Even: ").lower()
        if choice.isalpha() == False:
            print("ENTER A STRING")
        else:
            break

    b = randint(1, 6)
    # time.sleep(2)

    a = int(input("Enter Number between 1-6: "))
    sum = a + b

    time.sleep(1)
    print(f"Total: {sum}")

    if choice == "even" and sum % 2 == 0 or choice == "odd" and sum % 2 != 0:
        play_choice = input("Wanna bat or ball? ")
        print(f"You choose to {play_choice}\n")

        if play_choice.lower() == "bat":
            bot_choice = "ball"
        else:
            bot_choice = "bat"

    else:
        bot_choice = random.choice(bat_ball)
        print(f"bot chooses to {bot_choice}\n")

        if bot_choice.lower() == "bat":
            play_choice = "ball"
        else:
            play_choice = "bat"

    while first_round:
        # print("first_round_on")
        enter_number()
        play()



    second_round = True

    while second_round:
        # print("second_round")
        enter_number()
        play()

    yn = input("\nDo you wanna play again? (y/n)\n ").lower()
    if yn == "n":
        break
    else:
        pass

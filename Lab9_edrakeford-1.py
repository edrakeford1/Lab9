"""
Program: Match Coins Game
Name: Elijah Drakeford
Purpose: This program runs the Match Coins game using the Player
and Coin classes. Two players toss coins and gain or lose coins
based on the game rules.
Starter Code: None
Date: March 15, 2026
"""

from player import Player


def main():

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    play = input("Do you want to toss the coins? (y/n): ")

    while play.lower() == 'y':

        # Toss coins
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)

        # Determine winner
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("It's a match!" ,player1.get_name(), "wins a coin")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("No match!" ,player2.get_name(), "wins a coin!")

        # Wallet totals
        print(player1.get_name(), "has", player1.get_wallet(), "coins")
        print(player2.get_name(), "has", player2.get_wallet(), "coins")

        # Optional Game Over
        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("Game Over!")
            break

        play = input("Do you want to toss the coins? (y/n): ")

    # Final results
    print("\n---Final Score---")
    print(player1.get_name(), ":", player1.get_wallet(), "coins")
    print(player2.get_name(), ":", player2.get_wallet(), "coins")

    if player1.get_wallet() > player2.get_wallet():
        print(player1.get_name(), "wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(player2.get_name(), "wins the game!")
    else:
        print("It's a draw!")


main()
#!/usr/bin/env python3

from collections import namedtuple
from random import sample, randint
from itertools import product
from validator import enter_integer_in_range, enter_valid_character
import time
from RankTheHand import *

'''
*** This lab emulates a hand of 5 card draw 'em poker ***
Below are the instructions for the assignment.
- There can be 2-9 players
- Player 1 is you. If you fold, the game terminates and no one wins.
- There are three rounds and each player starts with $1000.
- Number of players are automatically generated.
- The first round is a betting round. If player 1 bets, all remaining players
  must bet that amount.
- There is a random number generator that decides if a players bets or folds.
- Round two is a card exchange round.
- There is a rand num generator that decides if a player will exchange cards
  and how many.
- The new hand will be displayed.
- Round three is the last betting round. Player 1 is prompted to b/f again.
- If Player 1 folds, the game is over and there is no winner.
- After all bets are in, the game will evaluate all active hands and display
  the winner, name of winning hand, and the actual hand.
'''


# Generate a players hand from the deck
def gen_cards(the_deck, number_of_cards):
    # Pick out 'number_of_cards' cards at random AND REMOVE THEM
    a_hand = sample(the_deck, number_of_cards)

    for a_card in list(the_deck):
        if a_card in a_hand:
            the_deck.remove(a_card)
    return a_hand


# Generate a playing deck
def generate_deck():
    # creates a 52 card deck with four suits with 13 cards each
    card_num_ids = range(52)
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["Ace", "King", "Queen", "Jack"]
    #  extend will add the remaining numbered cards to each suit.
    rank.extend([str(rank_num) for rank_num in range(2, 11)])
    display_cards = product(rank, suits)
    return list(display_cards)


# Create num_players
def create_players(the_deck, num_players):
    # utilizing namedtuples to assign/edit player attributes
    Player = namedtuple(
        "Player", "name, amount_left, player_hand, \
still_playing, hand_rank, final_hand"
    )

    all_players = [
        Player(
            name=f"Player_{int(player_num)}",
            amount_left=1_000,
            player_hand=gen_cards(the_deck, 5),
            still_playing=True,
            hand_rank=8,
            final_hand=None
        )
        for player_num in range(1, num_players + 1)
    ]

    return all_players


# Cycle through remaining players and complete their betting
def handle_the_bet(a_player, amount_you_bet, the_pot):
    the_pot += amount_you_bet
    # Remember that players HAVE TO bet what you bet above
    # Add amount to pot...deduct from a_player
    a_player = \
        a_player._replace(amount_left=(a_player.amount_left - amount_you_bet))
    # Print the player name and their hand
    print(f"\n{a_player.name} cards: {a_player.player_hand}")
    # Change amount player has left - subtract bet amount from existing amount
    print(
        f"{a_player.name} bets {amount_you_bet}.\tThe pot is at {the_pot}.\t\
{a_player.name} has ${a_player.amount_left} left."
    )
    print()

    return the_pot, a_player


# Completes player 1 action for first and third round
def handle_special_player_1_actions(you, low_bet_amt, the_pot):
    # Player_1 opts to bet....
    if you.amount_left == 0:
        no_bet = 0
        print(f'{you.name}, you are already all in!')
        return the_pot, you, no_bet

    else:
        amount_you_bet = enter_integer_in_range(
            f"What's your bet {you.name}? "
            f"(between {low_bet_amt} and {you.amount_left})", low_bet_amt,
            you.amount_left,)
    # update the pot amount
    the_pot += amount_you_bet
    # display updated player information
    you = you._replace(amount_left=(you.amount_left - amount_you_bet))
    print(f"\n{you.name} cards: {you.player_hand}")
    print(
        f"{you.name} bets {amount_you_bet}.   {the_pot = }.   \
{you.name} has ${you.amount_left} left."
    )

    return the_pot, you, amount_you_bet


#  Randomly decides # of cards players will exchange (0-3)
def discard_and_replace_cards_one_player(a_player, the_deck):
    print()
    # random number generator to automate amount of cards to exchange
    num_cards_replace = randint(0, 3)
    a_player_hand = a_player.player_hand

    if num_cards_replace > 0:
        card_word_for_print = "card" if num_cards_replace == 1 else "cards"
        print(
            f"{a_player.name} will exchange {num_cards_replace} \
{card_word_for_print}...."
        )

        for card in range(0, num_cards_replace):
            a_player_hand.pop(card)

        new_cards = sample(the_deck, num_cards_replace)

        for card in new_cards:
            a_player_hand.append(card)

        a_player = a_player._replace(player_hand=a_player_hand)
        # Change player hand to include new cards

    else:
        # Player has not opted to take any cards
        print(f"{a_player.name} has opted not to exchange any \
cards (standing pat)")

    # Print the altered hand
    print(f"{a_player.name}'s hand is now {a_player_hand}")


# Evaluate active hands and assign the hand name and number to each player
def rank_the_hand(player_list):

    for player in range(0, len(player_list)):
        # numerical value associates with hand strength(0 - 8)
        if is_straight_flush(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=0)
            player_list[player] = \
                player_list[player]._replace(final_hand='straight flush!')

        elif is_four_kind(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=1)
            player_list[player] = \
                player_list[player]._replace(final_hand='four of a kind!')

        elif is_flush(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=2)
            player_list[player] = \
                player_list[player]._replace(final_hand='a flush!')

        elif is_full_house(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=3)
            player_list[player] = \
                player_list[player]._replace(final_hand='a full house!')

        elif is_straight(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=4)
            player_list[player] = \
                player_list[player]._replace(final_hand='a straight!')

        elif is_three_kind(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=5)
            player_list[player] = \
                player_list[player]._replace(final_hand='three of a kind!')

        elif is_two_pairs(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=6)
            player_list[player] = \
                player_list[player]._replace(final_hand='two pair!')

        elif is_pair(player_list[player].player_hand):
            player_list[player] = player_list[player]._replace(hand_rank=7)
            player_list[player] = \
                player_list[player]._replace(final_hand='a pair!')

        else:
            player_list[player] = player_list[player]._replace(hand_rank=8)
            player_list[player] = \
                player_list[player]._replace(final_hand='high card!')


# Evaluates all remaining player hand strengths. Returns the winner
def pick_a_winner(player_list):
    winner_idx = None
    for player_idx in range(0, len(player_list)):

        # if a_player.still_playing:
        if player_list[player_idx].still_playing is True:
            # print(f"{player_list[player_idx]}")
            if(winner_idx is None):
                winner_idx = player_idx
            else:
                if(player_list[player_idx].hand_rank <
                        player_list[winner_idx].hand_rank):
                    winner_idx = player_idx
    return winner_idx


# Where the main program is running from. Time constraints played a factor
# in my structuring and logic.
def main():
    print()
    print("-" * 15, "Welcome to Five Card Draw!", "-" * 15)
    print()
    # utilizing functions from validator.py to validate input
    num_players = enter_integer_in_range(
        "Enter a number between 2 and 5, inclusive, for # players ", 2, 5
    )
    print()
    the_deck = generate_deck()
    player_list = create_players(the_deck, num_players)

    # Displays all players, amount_left, and active status prior to game
    for a_player in player_list:
        print(
            f"{a_player.name}\tamount_left = {a_player.amount_left}\
\tstill_playing = {a_player.still_playing}"
        )
        # used the sleep function for visual effect
        time.sleep(0.2)
    print()
    ###########################################################################
    # Round 1: Betting Round
    ###########################################################################
    # region    print()
    print("-" * 15, "Round 1", "-" * 15)
    print()
    # if more time was available, I would create more functions to complete
    # the rounds and clean up my main function.
    the_pot = 0
    number_of_players = len(player_list)
    everyone_folded = False
    msg = "Do you bet or fold (B or F)?"
    # used this to break the loop at the proper time
    kill_loop = False
    # loops through round one, completing the required actions
    while not kill_loop and not everyone_folded:
        if (player_1_action := enter_valid_character(msg, ("b", "f"))) != "f":
            everyone_folded = True
            # Player_1 bets. Let's get the amount of the bet...
            the_pot, player_list[0], amount_you_bet = \
                handle_special_player_1_actions(
                player_list[0], 1, the_pot
            )
            # Blank line to make outputs a bit easier to view
            print()
            the_pot = the_pot
            # Remaining players betting and cards.
            loop_count = 0
            for player_idx in range(1, number_of_players):
                # if a_player.still_playing:
                if player_list[player_idx].still_playing:
                    player_wanna_bet = randint(1, 100) > 25
                    if player_wanna_bet:
                        # for player_1 since other players must match it
                        the_pot, player_list[player_idx] = handle_the_bet(
                            player_list[player_idx], amount_you_bet, the_pot
                        )
                        everyone_folded = False
                    else:
                        print(f"{player_list[player_idx].name} folds")
                        # Take player out of the game....
                        player_list[player_idx] = \
                            player_list[player_idx]._replace(
                            still_playing=False
                        )
                loop_count += 1
                if loop_count == len(player_list) - 1:
                    kill_loop = True
                    break
        else:
            print(
                f"Player 1 folds. \tPlayer 1 amount left = \
{player_list[0].amount_left} \tGame over!"
            )
            exit()

    if everyone_folded is True:
        print(
            f"You win! The pot is {the_pot} and you have \
{player_list[0].amount_left + the_pot}"
        )
        exit()
    # endregion
    ###########################################################################
    # Round 2: Card Exchange
    ###########################################################################
    # region
    print()
    time.sleep(0.2)
    print("-" * 15, "Round 2", "-" * 15)
    print("You may exchange up to three cards")
    # loop to automate exchanging of cards for active players
    for player_idx in range(0, len(player_list)):
        if player_list[player_idx].still_playing is True:
            discard_and_replace_cards_one_player(player_list[player_idx],
                                                 the_deck)
    # endregion
    ###########################################################################
    # Round 3: Betting Round
    ###########################################################################
    # region
    print()
    time.sleep(0.2)
    print("-" * 15, "Round 3", "-" * 15)
    print("Players will bet and a winner will be selected!")
    # determines if player 1 wants to bet/fold at start of third round
    if (player_1_action := enter_valid_character(msg, ("b", "f"))) != "f":
        the_pot, player_list[0], amount_you_bet = \
            handle_special_player_1_actions(player_list[0], 1, the_pot)
        # determines remaining players bet/fold
        for player_idx in range(1, number_of_players):
            # if a_player.still_playing:
            if player_list[player_idx].still_playing is True:
                player_wanna_bet = randint(1, 100) > 10
                if player_wanna_bet:
                    # for player_1 since other players must match it
                    the_pot, player_list[player_idx] = handle_the_bet(
                        player_list[player_idx], amount_you_bet, the_pot
                    )
                else:
                    print(f"\n{player_list[player_idx].name} folds")
                    # Take player out of the game....
                    player_list[player_idx] = player_list[player_idx]._replace(
                        still_playing=False
                    )
    else:
        print("Player 1 folds. There is no winner. Game Over!\n")
        print(f"Player 1 remaining balance = {player_list[0].amount_left}\n")
        print("Thanks for playing!\n")
        exit()
    # endregion
    ###########################################################################
    # Determine winning hand
    ###########################################################################
    # sends remaining active hands to func and assigns name hand and value to
    # player attribute
    rank_the_hand(player_list)

    print(f'Active Players Hand and Rank:')
    for a_player in player_list:
        print(f'{a_player.name} is holding {a_player.final_hand}\n\
cards = {a_player.player_hand}\n')

    # returns the winner according to hand strength
    winner_idx = pick_a_winner(player_list)

    # final displayed output
    print(f"The winner is {player_list[winner_idx].name} who drew \
{player_list[winner_idx].final_hand} with the following hand:\n\
{player_list[winner_idx].player_hand}")


if __name__ == "__main__":
    main()

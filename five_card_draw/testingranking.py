#!/usr/bin/env python3
from RankTheHand import *
from collections import namedtuple
from Play5CardDraw import *
# test_hand = [('2', 'Hearts'), ('A', 'Spades'), ('8', 'Clubs'), ('4', 'Clubs'), ('7', 'Diamonds')]

def create_players(the_deck, num_players):
    Player = namedtuple(
        "Player", "name, amount_left, player_hand, still_playing, hand_rank"
    )

    all_players = [
        Player(
            name=f"Player_{int(player_num)}",
            amount_left=1_000,
            player_hand=gen_cards(the_deck, 5),
            still_playing=True,
            hand_rank=8,
        )
        for player_num in range(1, num_players + 1)
    ]

    return all_players

def gen_cards(the_deck, number_of_cards):
    # Pick out 'number_of_cards' cards at random AND REMOVE THEM
    a_hand = sample(the_deck, number_of_cards)

    for a_card in list(the_deck):
        if a_card in a_hand:
            the_deck.remove(a_card)
    return a_hand

def generate_deck():
    card_num_ids = range(52)
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["A", "King", "Queen", "Jack"]
    #  extend will add the remaining numbered cards to each suit.
    rank.extend([str(rank_num) for rank_num in range(2, 11)])
    display_cards = product(rank, suits)
    return list(display_cards)


def rank_the_hand(a_hand):
    
    if is_straight_flush(a_hand):
        print('You have a straight flush!')
        
    elif is_four_kind(a_hand):
        print('You have a four of a kind!')
        
    elif is_flush(a_hand):
        print('You have a flush!')
    
    elif is_full_house(a_hand):
        print('You have a full house!')
    
    elif is_straight(a_hand):
        print('You have a straight!')

    elif is_three_kind(a_hand):
        print('You have a three of a kind!')
        
    elif is_two_pairs(a_hand):
        print('You have a pair!')
    
    elif is_pair(a_hand):
        print('You have a pair')
    
    else:
        print("You didn't have any substantial hand.")


def main():
     
    #a_hand = [('3', 'Hearts'), ('3', 'Spades'), ('3', 'Clubs'), ('5', 'Clubs'), ('5', 'Diamonds')]

    #rank_the_hand(a_hand)
    the_deck = generate_deck()
    player_list = create_players(the_deck, num_players= 5)
    print(player_list[0][4])
    player_list[0] = player_list[0]._replace(hand_rank = 1)
    player_list[1] = player_list[1]._replace(hand_rank = 8)
    player_list[2] = player_list[2]._replace(hand_rank = 3)
    for player_index in range(0, len(player_list)):
        
        sorted_player_list = sorted(player_list, key = player_list[player_index].hand_rank)
        print(sorted_player_list)

    

if __name__ == '__main__':
    main()
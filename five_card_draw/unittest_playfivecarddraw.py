#!/usr/bin/env python3

from collections import namedtuple
import unittest
import Play5CardDraw as pcd
import RankTheHand as rth

'''
This Unit Test Module tests function in the
Play5CardDraw.py and RankTheHand.py modules.
'''


class TestCase(unittest.TestCase):

    def setUp(self):
        print('Creating Test Environment.')
        self.test_deck = pcd.generate_deck()
        self.test_hand = pcd.gen_cards(self.test_deck, 5)
        self.test_player = pcd.create_players(self.test_deck, 1)
        self.player_list = [self.test_player]

    def tearDown(self):
        print('Done Test')

    def test_generate_player_hand(self):
        # test the length of hand is 5 cards
        self.assertEquals(len(self.test_hand), 5)

    def test_generate_52_card_deck(self):
        func_deck = pcd.generate_deck()
        # compares test deck and func deck to ensure function creates the same
        # deck each time it is called
        try:
            func_deck == self.test_deck
        except Exception as e:
            set.fail(f'Generate deck funciton failed {e}')

    def test_create_player_object(self):
        # test checks the object type returned from the function
        # should be a list of tuples.
        self.assertEquals(type(self.test_player), list)

    def test_handle_the_bet(self):
        print(f'\n***Testing player bet updated and return the pot***')
        the_pot = 0
        amount_bet = 100
        the_pot, self.test_player = \
            pcd.handle_the_bet(self.test_player[0], amount_bet, the_pot)
        self.assertEquals(amount_bet, the_pot)

    def test_hand_is_straight_flush(self):
        straight_flush = [('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'),
                          ('5', 'Spades'), ('6', 'Spades')]
        self.assertEquals(rth.is_straight_flush(straight_flush), True)

    def test_hand_is_not_straight_flush(self):
        not_straight_flush = [('King', 'Spades'), ('3', 'Spades'),
                              ('4', 'Spades'), ('5', 'Spades'),
                              ('6', 'Spades')]
        self.assertEquals(rth.is_straight_flush(not_straight_flush), False)

    def test_hand_is_flush(self):
        flush = [('2', 'Spades'), ('6', 'Spades'), ('King', 'Spades'),
                 ('5', 'Spades'), ('6', 'Spades')]
        self.assertEquals(rth.is_flush(flush), True)

    def test_hand_is_not_flush(self):
        not_flush = [('2', 'Hearts'), ('6', 'Spades'), ('King', 'Spades'),
                     ('5', 'Spades'), ('6', 'Spades')]
        self.assertEquals(rth.is_flush(not_flush), False)

    def test_rank_the_hand_valid_straight_flush(self):
        straight_flush = [('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'),
                          ('5', 'Spades'), ('6', 'Spades')]
        self.player_list[0][0] = \
            self.player_list[0][0]._replace(player_hand=straight_flush)
        pcd.rank_the_hand(self.player_list[0])
        self.assertEquals(self.player_list[0][0].hand_rank, 0)

    def test_rank_the_hand_invalid_straight_flush(self):
        not_straight_flush = [('King', 'Spades'), ('3', 'Spades'),
                              ('4', 'Spades'), ('5', 'Spades'),
                              ('6', 'Spades')]
        self.player_list[0][0] = \
            self.player_list[0][0]._replace(player_hand=not_straight_flush)
        pcd.rank_the_hand(self.player_list[0])
        self.assertNotEqual(self.player_list[0][0].hand_rank, 0)

    def test_rank_the_hand_valid_four_kind(self):
        four_kind = [('2', 'Spades'), ('2', 'Hearts'), ('2', 'Clubs'),
                     ('2', 'Diamonds'), ('6', 'Spades')]
        self.player_list[0][0] = \
            self.player_list[0][0]._replace(player_hand=four_kind)
        pcd.rank_the_hand(self.player_list[0])
        self.assertEquals(self.player_list[0][0].hand_rank, 1)

    def test_rank_the_hand_invalid_four_kind(self):
        not_four_kind = [('2', 'Spades'), ('4', 'Hearts'),
                         ('2', 'Clubs'), ('2', 'Diamonds'), ('6', 'Spades')]
        self.player_list[0][0] = \
            self.player_list[0][0]._replace(player_hand=not_four_kind)
        pcd.rank_the_hand(self.player_list[0])
        self.assertNotEqual(self.player_list[0][0].hand_rank, 1)


if __name__ == '__main__':
    unittest.main()

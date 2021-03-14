#########################################
##### Name: Zhaorui Yang            #####
##### Uniqname: zryang              #####
#########################################

import unittest
import hw5_cards_ec2


class TestCard(unittest.TestCase):
        
    def test_1_remove_card(self):
        '''basic test on remove only one pair
        '''
        c1 = hw5_cards_ec2.Card(0, 1)
        c2 = hw5_cards_ec2.Card(0, 2)
        c3 = hw5_cards_ec2.Card(1, 2)
        hand1 = [c1, c2, c3]
        h1 = hw5_cards_ec2.Hand(hand1)
        h1.remove_pairs()
        self.assertEqual(h1.init_cards[0], c1)

    def test_2_remove_card(self):
        '''test on remove a pair from 4
        '''
        c1 = hw5_cards_ec2.Card(0, 1)
        c2 = hw5_cards_ec2.Card(0, 2)
        c3 = hw5_cards_ec2.Card(1, 2)
        c4 = hw5_cards_ec2.Card(2, 2)
        c5 = hw5_cards_ec2.Card(3, 2)
        hand1 = [c1, c2, c3, c4, c5]
        hand2 = [c1, c2, c3]
        h1 = hw5_cards_ec2.Hand(hand1)
        h1.remove_pairs()
        self.assertEqual(h1.init_cards[0], c1)
        self.assertEqual(h1.init_cards[1], c2)
        self.assertEqual(h1.init_cards[2], c3)

    def test_3_remove_card(self):
        '''test on remove two pairs
        '''
        c1 = hw5_cards_ec2.Card(0, 1)
        c2 = hw5_cards_ec2.Card(0, 2)
        c3 = hw5_cards_ec2.Card(1, 2)
        c4 = hw5_cards_ec2.Card(2, 3)
        c5 = hw5_cards_ec2.Card(3, 3)
        hand1 = [c1, c2, c3, c4, c5]
        hand2 = [c1]
        h1 = hw5_cards_ec2.Hand(hand1)
        h1.remove_pairs()
        self.assertEqual(h1.init_cards[0], c1)

    def test_4_deal_deck(self):
        '''test on deal all to 4 hands(exact division)
        '''
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(4, -1)
        self.assertEqual(len(hand_list), 4)
        self.assertEqual(len(hand_list[0]), 13)
        self.assertEqual(len(d1.cards), 0)

    def test_5_deal_deck(self):
        '''test on deal all to 5 hands(has remainder)
        '''
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(5, -1)
        self.assertEqual(len(hand_list), 5)
        self.assertEqual(len(hand_list[0]), 11)
        self.assertEqual(len(hand_list[1]), 11)
        self.assertEqual(len(hand_list[2]), 10)
        self.assertEqual(len(hand_list[3]), 10)
        self.assertEqual(len(hand_list[4]), 10)
        self.assertEqual(len(d1.cards), 0)

    def test_6_deal_deck(self):
        '''test on deal parts of the cards
        '''
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(6, 5)
        self.assertEqual(len(hand_list), 6)
        self.assertEqual(len(hand_list[0]), 5)
        self.assertEqual(len(d1.cards), 22)


if __name__ == "__main__":
    unittest.main()
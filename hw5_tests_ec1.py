#########################################
##### Name: Zhaorui Yang            #####
##### Uniqname: zryang              #####
#########################################

import unittest
import hw5_cards_ec1


class TestHand(unittest.TestCase):

    def test_construct_Card(self):
        hand = []
        for i in range(1, 4):
            hand.append(hw5_cards_ec1.Card(0, i))
        h1 = hw5_cards_ec1.Hand(hand)
        self.assertEqual(h1.init_cards[0].suit, 0)
        self.assertEqual(h1.init_cards[0].suit_name, "Diamonds")
        self.assertEqual(h1.init_cards[0].rank, 1)
        self.assertEqual(h1.init_cards[0].rank_name, "Ace")
        self.assertEqual(h1.init_cards[1].suit, 0)
        self.assertEqual(h1.init_cards[1].suit_name, "Diamonds")
        self.assertEqual(h1.init_cards[1].rank, 2)
        self.assertEqual(h1.init_cards[1].rank_name, "2")
        self.assertEqual(h1.init_cards[2].suit, 0)
        self.assertEqual(h1.init_cards[2].suit_name, "Diamonds")
        self.assertEqual(h1.init_cards[2].rank, 3)
        self.assertEqual(h1.init_cards[2].rank_name, "3")

    def testAddAndRemove(self):
        #test add
        c1 = hw5_cards_ec1.Card(0, 1)
        c2 = hw5_cards_ec1.Card(0, 2)
        c3 = hw5_cards_ec1.Card(2, 13)
        hand1 = [c1, c2]
        hand2 = [c1, c2, c3]
        h1 = hw5_cards_ec1.Hand(hand1)
        #add existing card
        h1.add_card(c1)
        self.assertEqual(h1.init_cards, hw5_cards_ec1.Hand(hand1).init_cards)
        #add other card
        h1.add_card(c3)
        self.assertEqual(h1.init_cards, hw5_cards_ec1.Hand(hand2).init_cards)
        #test remove
        #remove card in hand
        h1.remove_card(c3)
        self.assertEqual(len(h1.init_cards), 2)
        self.assertEqual(h1.init_cards, hw5_cards_ec1.Hand(hand1).init_cards)
        #remove card not in hand
        h1.remove_card(c3)
        self.assertEqual(len(h1.init_cards), 2)
        self.assertEqual(h1.init_cards, hw5_cards_ec1.Hand(hand1).init_cards)

    def test_draw(self):
        c1 = hw5_cards_ec1.Card(0, 1)
        c2 = hw5_cards_ec1.Card(0, 2)
        d1 = hw5_cards_ec1.Deck()
        d1.shuffle()
        h1 = hw5_cards_ec1.Hand(d1.deal_hand(5))
        self.assertEqual(len(h1.init_cards), 5)
        self.assertEqual(len(d1.cards), 47)
        h1.draw(d1)
        self.assertEqual(len(h1.init_cards), 6)
        self.assertEqual(len(d1.cards), 46)
        h1.draw(d1)
        self.assertEqual(len(h1.init_cards), 7)
        self.assertEqual(len(d1.cards), 45)


if __name__ == "__main__":
    unittest.main()

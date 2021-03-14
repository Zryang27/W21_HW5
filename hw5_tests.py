#########################################
##### Name: Zhaorui Yang            #####
##### Uniqname: zryang              #####
#########################################

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q1_0 = hw5_cards.Card(0,12)
        self.assertEqual(c_test_q1_0.rank_name, "Queen")
        c_test_q1_1 = hw5_cards.Card(1,12)
        self.assertEqual(c_test_q1_1.rank_name, "Queen")
        c_test_q1_2 = hw5_cards.Card(2,12)
        self.assertEqual(c_test_q1_2.rank_name, "Queen")
        c_test_q1_3 = hw5_cards.Card(3,12)
        self.assertEqual(c_test_q1_3.rank_name, "Queen")
        X = c_test_q1_3.rank_name
        Y = "Queen"
        return X, Y
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q2_1 = hw5_cards.Card(1,2)
        self.assertEqual(c_test_q2_1.suit_name, "Clubs")
        X = c_test_q2_1.suit_name
        Y = "Clubs"
        return X, Y    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q3_1 = hw5_cards.Card(3,13)
        self.assertEqual(c_test_q3_1.__str__(), "King of Spades")
        X = c_test_q3_1.__str__()
        Y = "King of Spades"
        return X, Y
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q4_1 = hw5_cards.Deck()
        self.assertEqual(len(c_test_q4_1.cards), 52)
        X = len(c_test_q4_1.cards)
        Y = 52
        return X, Y  

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q5_1 = hw5_cards.Deck()
        self.assertIsInstance(c_test_q5_1.deal_card(), hw5_cards.Card)
        X = c_test_q5_1.deal_card()
        Y = hw5_cards.Card
        return X, Y
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q6_1 = hw5_cards.Deck()
        self.assertEqual(len(c_test_q6_1.cards), 52)
        c_test_q6_1.deal_card()
        self.assertEqual(len(c_test_q6_1.cards), 51)
        c_test_q6_1.deal_card()
        self.assertEqual(len(c_test_q6_1.cards), 50)
        X = len(c_test_q6_1.cards)
        Y = 50
        return X, Y    
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q7_1 = hw5_cards.Deck()
        self.assertEqual(len(c_test_q7_1.cards), 52)
        card0 = c_test_q7_1.deal_card()
        self.assertEqual(len(c_test_q7_1.cards), 51)
        c_test_q7_1.replace_card(card0)
        self.assertEqual(len(c_test_q7_1.cards), 52)
        card1 = c_test_q7_1.deal_card()
        card2 = c_test_q7_1.deal_card()
        self.assertEqual(len(c_test_q7_1.cards), 50)
        c_test_q7_1.replace_card(card1)
        c_test_q7_1.replace_card(card2)
        self.assertEqual(len(c_test_q7_1.cards), 52)
        X = len(c_test_q7_1.cards)
        Y = 52
        return X, Y
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_test_q8_1 = hw5_cards.Deck()
        self.assertEqual(len(c_test_q8_1.cards), 52)
        c_test_q8_1.deal_card()
        self.assertEqual(len(c_test_q8_1.cards), 51)
        card1 = hw5_cards.Card(0,1)
        c_test_q8_1.replace_card(card1)
        self.assertEqual(len(c_test_q8_1.cards), 51)
        X = len(c_test_q8_1.cards)
        Y = 51
        return X, Y  



if __name__ == "__main__":
    unittest.main()
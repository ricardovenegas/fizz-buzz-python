# -*- coding: utf-8 -*-
import unittest
import math
from fizzbuzz.fizzbuzz import FizzBuzz
from fizzbuzz.exception import ArgsException

class TestBuzz(unittest.TestCase) :
    def setUp(self):
        self.game = FizzBuzz()
        
    def testPlayTenFirstNumbers(self):
        self.assertEqual(self.game.play(1), "1", 'incorrect reponse for 1')
        self.assertEqual(self.game.play(2), "2", 'incorrect reponse for 2')
        self.assertEqual(self.game.play(3), "3", 'incorrect reponse for 3')
        self.assertEqual(self.game.play(4), "4", 'incorrect reponse for 4')
        self.assertEqual(self.game.play(5), "Fizz", 'incorrect reponse for 5')
        self.assertEqual(self.game.play(6), "6", 'incorrect reponse for 6')
        self.assertEqual(self.game.play(7), "Buzz", 'incorrect reponse for 7')
        self.assertEqual(self.game.play(8), "8", 'incorrect reponse for 8')
        self.assertEqual(self.game.play(9), "9", 'incorrect reponse for 9')
        self.assertEqual(self.game.play(10), "Fizz", 'incorrect reponse for 10')
    
    def testPlayTenFirstNumbersInString(self):
        self.assertEqual(self.game.play("1"), "1", 'incorrect reponse for 1')
        self.assertEqual(self.game.play("2"), "2", 'incorrect reponse for 2')
        self.assertEqual(self.game.play("3"), "3", 'incorrect reponse for 3')
        self.assertEqual(self.game.play("4"), "4", 'incorrect reponse for 4')
        self.assertEqual(self.game.play("5"), "Fizz", 'incorrect reponse for 5')
        self.assertEqual(self.game.play("6"), "6", 'incorrect reponse for 6')
        self.assertEqual(self.game.play("7"), "Buzz", 'incorrect reponse for 7')
        self.assertEqual(self.game.play("8"), "8", 'incorrect reponse for 8')
        self.assertEqual(self.game.play("9"), "9", 'incorrect reponse for 9')
        self.assertEqual(self.game.play("10"), "Fizz", 'incorrect reponse for 10')
    
    def testPlayMultiplicationsNumber(self):
        self.assertEqual(self.game.play(15), "Fizz", 'incorrect reponse for 15')
        self.assertEqual(self.game.play(22), "Buzz", 'incorrect reponse for 22')
        self.assertEqual(self.game.play(35), "Fizz", 'incorrect reponse for 35')
        self.assertEqual(self.game.play(42), "Buzz", 'incorrect reponse for 42')
        self.assertEqual(self.game.play(56), "Buzz", 'incorrect reponse for 56')
        self.assertEqual(self.game.play(70), self.game.name, 'incorrect reponse for 70')
    
    def testPlayNan(self):
        with self.assertRaises(ArgsException):
            self.game.play(math.nan)

    def testPlayLargeNumber(self):
        self.assertEqual(self.game.play("133463891334689133463891334689133463891334689133463891334689133463891334689133463891334689133463891"), "133463891334689133463891334689133463891334689133463891334689133463891334689133463891334689133463891", 'incorrect reponse for 133463891334689133463891334689133463891334689133463891334689133463891334689133463891334689133463891')
        self.assertEqual(self.game.play("123467891234689123467891234689123467891234689123467891234689123467891234689123467891234689123467895"), "Fizz", 'incorrect reponse for 123467891234689123467891234689123467891234689123467891234689123467891234689123467891234689123467895')
        self.assertEqual(self.game.play("2000300624103679337202883934330700182830667"), "Buzz", 'incorrect reponse for 2000300624103679337202883934330700182830667')
        self.assertEqual(self.game.play("10002303120328396686014429771633300914233330"), self.game.name, 'incorrect reponse for 10002303120328396686014429771633300914233330')

if __name__ == '__main__':
    unittest.main()   
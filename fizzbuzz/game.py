# -*- coding: utf-8 -*-
from fizzbuzz.exception import ArgsException

class Game :
    def __init__(self, name):
        self.name = name
    
    def accept(self, game):
        if game is None:
            return False
        return game==self.name
        
    def play(self, number):
        self.is_nan(number)
        if self.is_multiple(number) or self.contains_value(number):
            return self.name
        return str(number)
    
    def is_nan(self, number):
        # This condition raise an exception if "number" is not a number
        if (number != number):
            raise ArgsException
        
    def is_multiple(self, number):
        # This condition test if the number is a multiple of the value associated with the game
        return (int(number) % self.game_value == 0)
        
    def contains_value(self, number):
        # This condition test if the number contains the value associated with the game
        return str(self.game_value) in str(number)
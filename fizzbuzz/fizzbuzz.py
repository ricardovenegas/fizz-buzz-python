# -*- coding: utf-8 -*-
from fizzbuzz.game import Game
from fizzbuzz.buzz import Buzz
from fizzbuzz.fizz import Fizz

class FizzBuzz(Game) :
    def __init__(self) :
        Game.__init__(self, "FizzBuzz")

    def play(self, number):
        availableGames = [Fizz(), Buzz()]
        count_multiple = 0
        count_contains = 0
        answer = ""
        self.is_nan(number)
        # This loop allow the number to be tested with each game value
        for currentGame in availableGames :
            if currentGame.is_multiple(number):
                # We increment count_multiple every time the number test true for a game rule
                count_multiple += 1
                # This condition allow for the answer to be the name of the last game tested successful if it's not FizzBuzz
                answer = currentGame.name
            if currentGame.contains_value(number):
                # We increment count_contains every time the number test true for a game rule
                count_contains += 1
                answer = currentGame.name
        # If the number tested true for at least one of the same criteria for every game, it's FizzBuzz
        if count_multiple == len(availableGames) or count_contains == len(availableGames):
            return self.name
        # Else, it's the name of the first game tested successful
        elif answer != "":
            return answer
        # If neither, return the number as per the rule
        return str(number)
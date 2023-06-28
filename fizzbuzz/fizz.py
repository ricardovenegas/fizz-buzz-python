# -*- coding: utf-8 -*-
from fizzbuzz.game import Game

class Fizz(Game) :
    game_value = 5

    def __init__(self) :
        Game.__init__(self, "Fizz")
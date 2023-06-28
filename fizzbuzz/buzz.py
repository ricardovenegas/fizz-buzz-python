# -*- coding: utf-8 -*-
from fizzbuzz.game import Game

class Buzz(Game) :
    game_value = 2
    
    def __init__(self) :
        Game.__init__(self, "Buzz")
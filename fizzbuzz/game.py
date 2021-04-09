# -*- coding: utf-8 -*-
class Game :
    def __init__(self, name):
        self.name = name
    
    def accept(self, game):
        if game is None:
            return False
        return game==self.name
        
    def play(self, number):
        pass
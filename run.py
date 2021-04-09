# -*- coding: utf-8 -*-
import argparse
from fizzbuzz.buzz import Buzz
from fizzbuzz.fizz import Fizz
from fizzbuzz.fizzbuzz import FizzBuzz

parser = argparse.ArgumentParser()
parser.add_argument("number", help="donnez votre nombre")
parser.add_argument("game", help="donnez votre jeu")
args = parser.parse_args()

availableGames = [Buzz(), Fizz(), FizzBuzz()]
for currentGame in availableGames :
    if currentGame.accept(args.game) :
        print(currentGame.play(args.number))
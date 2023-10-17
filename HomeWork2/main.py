import random

from HomeWork2.GemGenerator import GemGenerator
from HomeWork2.GoldGenerator import GoldGenerator
from HomeWork2.SilverGenerator import SilverGenerator
from HomeWork2.CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()
from HomeWork2.ItemFabric import ItemFabric
from HomeWork2.CupperReward import CupperReward


class CupperGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (медь)")
        return CupperReward()

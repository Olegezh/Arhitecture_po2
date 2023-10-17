from HomeWork2.ItemFabric import ItemFabric
from HomeWork2.GoldReward import GoldReward


class GoldGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (золото)")
        return GoldReward()

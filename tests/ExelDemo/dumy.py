import unittest
from unittest.dataModel.item_id import ItemId
from unittest import ItemId


class TestItemId(unittest.TestCase):
    itemIds = lambda: (
        ( 'q42' ),
        ( 'Q42' ),
        ( 'Q1' ),
        ( 'Q1000' ),
        ( 'Q31337' ),
    )

    @ItemId(itemIds)
    def test_constructor(self, itemString):
        itemId = ItemId(itemString)
        self.assertEqual(itemId.getSerialization(), itemString)
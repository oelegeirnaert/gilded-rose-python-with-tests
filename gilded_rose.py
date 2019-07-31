class GildedRose:
    @staticmethod
    def update_quality(items):
        #if "CONJURED" in item.name.upper():
        for item in items:
            # At the end of each day our system lowers both values for every item.
            # So decrease the sell_in...
            GildedRose.decrease_sell_in(item)

            # "Backstage passes", like "Aged Brie", increases by one in Quality as its SellIn date approaches
            #if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
            current_item_name = item.name.upper()
            if "AGED BRIE" in current_item_name or "BACKSTAGE PASSES" in current_item_name:
                # Increase the quality by 1 by default
                GildedRose.increase_quality(item)
                # Quality increases by 2 when there are 10 days or less
                if item.sell_in <= 10:
                    GildedRose.increase_quality(item)
                # Quality increases by 3 when there are 5 days or less
                if item.sell_in <= 5:
                    GildedRose.increase_quality(item)

                if item.sell_in <= 0:
                    item.quality = 0

            else:
                GildedRose.decrease_quality(item)

                # "Conjured" items degrade in Quality twice as fast as normal items
                if "CONJURED" in current_item_name and item.sell_in > 0:
                    GildedRose.decrease_quality(item, by = 3) # Not that sure, ask for more tests or check if the tests are correct!

                # Once the sell by date has passed, Quality degrades twice as fast.
                if item.sell_in <= 0:
                    GildedRose.decrease_quality(item)

        return items


    @staticmethod
    def decrease_sell_in(item):
        if item.name.upper() != "SULFURAS, HAND OF RAGNAROS":
            item.sell_in -= 1
        return item


    @staticmethod
    def increase_quality(item, by = 1):
        """
        Increase the quality of an item.
        The Quality of an item is never more than 50, but "Sulfuras" is a legendary item and as such its Quality is always 80 and it never alters.
        """

        if GildedRose.has_quality_problem(item) and item.quality < 50:
            item.quality += by
        return item


    @staticmethod
    def decrease_quality(item, by = 1):
        """
        Decrease the quality of an item.
        The Quality of an item is never negative, but "Sulfuras" is a legendary item and as such its Quality is always 80 and it never alters
        """

        if GildedRose.has_quality_problem(item) and item.quality > 0:
            item.quality -= by
        return item


    @staticmethod
    def has_quality_problem(item):
        """
        "Sulfuras" is a legendary item and as such its Quality is always 80 and it never alters
        """
        if "SULFURAS" in item.name.upper():
            item.quality=80
            return False
        return True

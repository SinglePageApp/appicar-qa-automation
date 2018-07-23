from automation.data import Model, Field


class Store(Model):
    """
    Represents a store which offers food and drinks (restaurant / bar).
    """
    def __init__(self):
        """
        Constructor: model's schema is defined here.
        """
        super(Store, self).__init__(
            'stores',
            Field('name'),
            Field('date', type='datetime'),
            Field('description', type='json'),
            Field('address'),
            Field('featured', type='boolean'),
            Field('lat', type='double'),
            Field('lng', type='double'),
            Field('image'),
            Field('city'),
            Field('menu', type='json'),
            Field('country'),
            Field('category'),
            Field('URI'),
            Field('reviews', type='list:string')
        )

    def find_all(self):
        """
        Finds all the stores.

        :returns: A set of stores.
        :rtype: pydal.objects.Set
        """
        return self.query(self.model).select()

    def find_by_food(self, category):
        """
        Finds all the stores which have the given food category in their menus.

        :param category: The food category to search.
        :type category: str
        :returns: An iterator for a set of stores.
        :rtype: pymongo.cursor.Cursor
        """
        return self.native.find(
            {'menu.items.food.category': {'$regex': '.*' + category + '.*'}}
        )

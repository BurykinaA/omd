from keyword import iskeyword
from numbers import Number
import json


class AdvertNestedKey():
    def __init__(self, mapping: dict):
        for key in mapping:
            if isinstance(mapping[key], dict):
                self.__dict__[key] = AdvertNestedKey(mapping[key])
            else:
                self.__dict__[key] = mapping[key]

    def __getattr__(self, key: str):
        if key[-1] == '_' and iskeyword(key[:-1]):
            key = key[:-1]
        return self.__dict__[key]

    def __str__(self, lvl=0) -> str:
        strt = '_' * lvl * 5
        res = []
        nesteds = []
        for key in self.__dict__:
            if not isinstance(self.__dict__[key], AdvertNestedKey):
                res.append(strt + str(self.__dict__[key]))
            else:
                nesteds.append(key)
        for key in nesteds:
            res.append(strt + '| ' + key + ':')
            res.append(
                self.__dict__[key].__str__(lvl+1)
                )
        return '\n'.join(res)


class ColorMixin:
    color_code = 32

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__str__ = ColorMixin.__str__

    def __str__(self, color=None) -> str:
        if color is None:
            color = self.color_code
        res = f'\033[1;{color};40m' + super().__str__()
        res += '\033[0;37;40m'
        return res


class Advert(ColorMixin, AdvertNestedKey):
    def __init__(self, mapping: dict) -> None:
        self.check_title(mapping)
        self._price: Number = 0
        if 'price' in mapping:
            self.price = mapping['price']
            mapping.pop('price')
        
        super().__init__(mapping)

    @staticmethod
    def check_title(mapping) -> None:
        if 'title' not in mapping:
            raise ValueError('title must be in mapping.')
        if not isinstance(mapping['title'], str):
            raise ValueError('title must be a string.')

    @property
    def price(self) -> Number:
        return self._price

    @price.setter
    def price(self, value: Number) -> None:
        if not isinstance(value, Number):
            raise ValueError("Price must be a number")
        if value < 0:
            raise ValueError("Price must be not negative number.")
        self._price = value


if __name__ == "__main__":
    json_str = """
     {
        "title": "Kupi slona",
        "class": "slon",
        "price": 222,
        "location": {
            "address": "gorod grechov 343",
            "metro_stations": ["Domodedovo", "Novikovo"],
            "nested": {
                "four": "vse govorat kuply, a ti vosmi i kupi"
                }
            }
    }
    """
    json_obj = json.loads(json_str)
    adv = Advert(json_obj)
    print(adv)
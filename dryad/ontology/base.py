import re

class BaseField(str):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        try:
            return (self.name == other.name) and isinstance(other, type(self))
        except AttributeError:
            return self.name == other

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return "{}[{}]".format(self.__class__.__name__, self.name)

    def __str__(self):
        return self.name


class StringField(BaseField):
    pass

class DigitField(StringField):
    def item_clean(self, val):
        return re.sub(r"[^\d]*", "", val)

class DateField(BaseField):
    pass

from dryad import *
from dryad.ontology import *

class TestBaseField:
    field = BaseField("A")

    def test_str(self):
        assert self.field.__str__() == "A"

    def test_repr(self):
        assert self.field.__repr__() == "BaseField[A]"

    def test_equality(self):
        assert self.field == BaseField("A")

    def test_equality_to_str(self):
        assert self.field == "A"

    def test_equality_wrong_type(self):
        assert self.field != 1

    def test_hash(self):
        assert hash(self.field) == hash("A")


class TestDigitField:
    field = DigitField("digit")
    ds = DryadSeries(["123a", "456b", "789c"], name=field)

    def test_value_clean(self):
        assert self.field.value_clean("123-456-7890") == "1234567890"

    def test_clean_series(self):
        assert list(self.ds.clean()) == ["123", "456", "789"]

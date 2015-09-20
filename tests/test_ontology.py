from dryad.ontology import *

class TestBaseField():
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

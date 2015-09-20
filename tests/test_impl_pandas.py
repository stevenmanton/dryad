import pytest

import pandas as pd

from dryad.ontology import *
from dryad.impl_pandas import *


class TestDataFrameConstructors:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
    names = map(BaseField, df.columns)

    def test_from_pandas(self):
        ddf = DryadDataFrame.from_pandas(self.df, self.names)
        assert all([isinstance(x, BaseField) for x in ddf.columns])


class TestDataFrameOperations:
    ddf = DryadDataFrame.from_pandas(
        pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']}),
        map(BaseField, 'AB'))

    def test_str_indexing(self):
        assert list(self.ddf['A']) == [1, 2, 3]

    def test_field_indexing(self):
        assert list(self.ddf[BaseField('A')]) == [1, 2, 3]


class PlusOneField(BaseField):
    def value_plus_one(self, val):
        return val+1

class UpperField(BaseField):
    def value_upper(self, val):
        return str.upper(val)


class TestSeriesFunctionDispatch:
    ds = DryadSeries([1, 2, 3], name=PlusOneField("A"))

    def test_value_plus_one(self):
        assert list(self.ds.plus_one()) == [2, 3, 4]

    def test_attribute_error(self):
        with pytest.raises(AttributeError):
            self.ds.plus_one_non_existent()


class TestDataFrameFunctionDispatch:
    ddf = DryadDataFrame({PlusOneField("A"): [1, 2, 3],
                          UpperField("B"): ['x', 'y', 'z']})

    def test_value_plus_one(self):
        assert list(self.ddf.plus_one()['A']) == [2, 3, 4]

    # def test_attribute_error(self):
    #     with pytest.raises(AttributeError):
    #         self.ds.plus_one_non_existent()

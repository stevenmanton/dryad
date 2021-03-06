import pytest
import pandas as pd

import dryad
from dryad.ontology.base import *
from dryad.impl.pandas_ import *

# ----- Series -----

class TestSeriesReturnTypes:
    ds = dryad.Series([1, 2, 3])

    def test_return_types(self):
        assert isinstance(self.ds.apply(lambda x: x), dryad.Series)

    def test_slice_return_types(self):
        assert isinstance(self.ds[:], dryad.Series)


# ----- DataFrame -----

class TestDataFrameConstructors:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
    names = map(BaseField, df.columns)

    def test_from_pandas(self):
        ddf = DataFrame.from_pandas(self.df, self.names)
        assert isinstance(ddf, dryad.DataFrame)
        assert all([isinstance(x, BaseField) for x in ddf.columns])


class TestDataFrameOperations:
    ddf = DataFrame.from_pandas(
        pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']}),
        map(BaseField, 'AB'))

    def test_str_indexing(self):
        assert list(self.ddf['A']) == [1, 2, 3]

    def test_field_indexing(self):
        assert list(self.ddf[BaseField('A')]) == [1, 2, 3]


class TestDataFrameReturnTypes:
    ddf = DataFrame({BaseField('A'): [1, 2, 3],
                     BaseField('B'): ['x', 'y', 'z']})

    def test_col_slice_to_series(self):
        assert isinstance(self.ddf['A'], dryad.Series)
        assert isinstance(self.ddf.loc[:, 'A'], dryad.Series)
        assert isinstance(self.ddf.ix[:, 'A'], dryad.Series)
        assert isinstance(self.ddf.icol(0), dryad.Series)

    def test_slice_to_dataframe(self):
        assert isinstance(self.ddf[['A', 'B']], dryad.DataFrame)


# ----- Test DataFrame function dispatching -----

class PlusOneField(BaseField):
    attr = 'attr'  # test attribute

    def item_plus_one(self, val):
        return val + 1

    @staticmethod
    def item_plus_n(val, n):
        return val + n


class UpperField(BaseField):
    def item_upper(self, val):
        return str.upper(val)


class TestSeriesFunctionDispatch:
    ds = dryad.Series([1, 2, 3], name=PlusOneField("A"))

    def test_attr(self):
        assert self.ds.attr == 'attr'

    def test_item_plus_one(self):
        assert list(self.ds.plus_one()) == [2, 3, 4]

    def test_item_plus_n(self):
        assert list(self.ds.plus_n(4)) == [5, 6, 7]

    def test_attribute_error(self):
        with pytest.raises(AttributeError):
            self.ds.plus_one_non_existent()

    def test_returns_dryad(self):
        """Returns another dryad instance for chaining commands"""
        assert isinstance(self.ds.plus_one(), Series)


class TestDataFrameFunctionDispatch:
    ddf = DataFrame({PlusOneField("A"): [1, 2, 3],
                     UpperField("B"): ['x', 'y', 'z']})

    def test_item_plus_one(self):
        assert list(self.ddf.plus_one()['A']) == [2, 3, 4]

    def test_attribute_error(self):
        with pytest.raises(AttributeError):
            self.ddf.function_that_does_not_exist()

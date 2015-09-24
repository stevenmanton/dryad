import pandas as pd

__all__ = ["Series", "DataFrame"]

class Series(pd.Series):
    def __getattr__(self, attr):
        try:
            return super(Series, self).__getattr__(attr)
        except AttributeError as e:
            pass

        try:
            fun = getattr(self.name, "item_" + attr)
            return lambda: Series(self.apply(fun))
        except AttributeError:
            raise e


class DataFrame(pd.DataFrame):
    # todo: Return dryad Series and DF's from indexing
    # todo: Support inplace keyword

    @property
    def _constructor(self):
        return DataFrame

    # Hack pandas DataFrame to return dryad Series type:
    _constructor_sliced = Series

    @classmethod
    def from_pandas(cls, df, names):
        ddf = cls.from_records(df, columns=names)
        return ddf

    def __getattr__(self, attr):
        try:
            return super(DataFrame, self).__getattr__(attr)
        except AttributeError as e:
            pass

        df_new = self.copy()
        encountered_method = False
        for idx, col in self.iteritems():
            try:
                fun = getattr(idx, "item_" + attr)
                df_new[idx] = col.apply(fun)
                encountered_method = True
            except AttributeError:
                pass
        # return lambda: df_new

        if encountered_method:
            return lambda: df_new
        else:
            raise e

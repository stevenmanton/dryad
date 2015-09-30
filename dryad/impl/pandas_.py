import pandas as pd

__all__ = ["Series", "DataFrame"]

class Series(pd.Series):

    @property
    def _constructor(self):
        return Series

    @property
    def _constructor_expanddim(self):
        return DataFrame

    def __getattr__(self, attr):
        try:
            return super(Series, self).__getattr__(attr)
        except AttributeError as e:
            # Test to see if the function exists:
            try:
                fun = getattr(self.name, "item_" + attr)

                def apply_fun(*args, **kwargs):
                    return Series(self.apply(fun, args=args, **kwargs))
                return apply_fun
            except AttributeError:
                # Test to see if the attribute exists:
                try:
                    attr = getattr(self.name, attr)
                    return attr
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
            df_new = self.copy()
            encountered_method = False
            for idx, col in self.iteritems():
                try:
                    fun = getattr(idx, "item_" + attr)
                    df_new[idx] = col.apply(fun)
                    encountered_method = True
                except AttributeError:
                    pass

            if encountered_method:
                return lambda: df_new
            else:
                raise e

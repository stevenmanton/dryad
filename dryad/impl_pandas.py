import pandas as pd

__all__ = ["DryadSeries", "DryadDataFrame"]

class DryadSeries(pd.Series):
    def __getattr__(self, attr):
        try:
            return super(DryadSeries, self).__getattr__(attr)
        except AttributeError as e:
            pass

        try:
            fun = getattr(self.name, "value_" + attr)
            return lambda: self.apply(fun)
        except AttributeError:
            raise e


class DryadDataFrame(pd.DataFrame):
    @staticmethod
    def from_pandas(df, names):
        df.columns = names
        return df

    def __getattr__(self, attr):
        try:
            return super(DryadDataFrame, self).__getattr__(attr)
        except AttributeError as e:
            pass

        df_new = self.copy()
        for idx, col in self.iteritems():
            try:
                fun = getattr(idx, "value_" + attr)
                df_new[idx] = col.apply(fun)
                print col.attr()
            except AttributeError:
                pass

        return lambda: df_new

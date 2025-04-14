
class Transformer:
    def transform(self, df):
        # eksempel på transformation
        df["name"] = df["name"].str.upper()
        return df
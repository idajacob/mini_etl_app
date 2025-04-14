
class TransformExtra:
    def transform(self, df):
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.strip().str.capitalize()
        return df

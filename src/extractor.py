import pandas as pd

class Extractor:
    def extract_csv(self, filepath):
        print(f"Indlæser: {filepath}")
        try:
            df = pd.read_csv(filepath)
            return df
        except Exception as e:
            print(f"Fejl ved indlæsning af CSV: {e}")
            return None

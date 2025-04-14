class Loader:
    def load(self, df, output_path):
        try:
            df.to_csv(output_path, index=False)
            print(f"Data gemt her: {output_path}")
            return True
        except Exception as e:
            print(f"FEJL ved load af: {e}")
            return False

      
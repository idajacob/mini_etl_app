from extractor import Extractor
from transform_extra import TransformExtra # man kan skifte mellem transformer.py og transform_extra.py for forskellige transformationer
from loader import Loader

def main():
    print("Starter indlæsning af CSV")
    
    # extractor
    extractor = Extractor()
    df = extractor.extract_csv("data/products.csv")

    print("CSV indlæst")
    
    if df is not None:
        # transformer
        transformer = TransformExtra()
        df = transformer.transform(df)
        
        print("Data indlæst:")
        print(df.head())
    
        # loader
        loader = Loader()
        success = loader.load(df, "data/output.csv")
        if success:
            print("Load færdig")
        else:
            print("Load mislykkedes")
        
    
    else:
        print("Kunne ikke indlæse data.")

if __name__ == "__main__":
    main()

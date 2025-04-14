import streamlit as st
import pandas as pd
import io
import sys
import os

# Gør det muligt at importere fra src-mappen
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.extractor import Extractor
from src.transformer import Transformer
from src.transform_extra import TransformExtra
from src.loader import Loader

st.set_page_config(page_title="Mini ETL App", layout="wide")
st.title("Mini ETL App")

uploaded_file = st.file_uploader("Vælg en fil", type="csv")

if uploaded_file:
    extractor = Extractor()
    df = pd.read_csv(io.StringIO(uploaded_file.getvalue().decode("utf-8")))

    st.success("Fil uploadet og læst.")
    st.subheader("Original data")
    st.dataframe(df)

    transformer_valg = st.radio("Vælg en tranformation", ["standard", "extra"])

    if transformer_valg == "standard":
        transformer = Transformer()
    else:
        transformer = TransformExtra()

    df_transformed = transformer.transform(df)

    st.subheader("Transformeret data")
    st.dataframe(df_transformed)

    if st.button("Gem som output.csv"):
        loader = Loader()
        loader.load(df_transformed, "data/output.csv")
        st.success("Data gemt som data/output.csv")
        
        csv = df_transformed.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download som CSV",
            data=csv,
            file_name="output.csv",
            mime="text/csv"
        )

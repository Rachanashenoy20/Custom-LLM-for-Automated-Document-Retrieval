from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib



load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)

st.title("Prompt driven analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    if os.path.isfile("temp_chart.png"):
        os.remove("temp_chart.png")
    prompt = st.text_area("Enter your prompt:")
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                response = pandas_ai.run(df, prompt=prompt)
                st.write(pandas_ai.run(df, prompt=prompt))
                matplotlib.use('svg')
                if os.path.isfile("temp_chart.png"):
                    st.image("temp_chart.png")
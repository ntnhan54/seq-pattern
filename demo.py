import pandas as pd
import streamlit as st
from time import time
from itertools import cycle

st.title("Welcome to Galaxy Play 🍔📸")
st.header("Sequential Pattern Demo")


values = st.slider(
    'Select a range of pattern index',
    0, 1000, (0, 50))
st.write('Values:', values)

bt = st.button('Generate')
if bt:
    idx = list(range(values[0], values[1]))
    seq_df = pd.read_pickle('sequential_pattern.pkl')

    res = seq_df.iloc[idx]

    pattern_list = res.pattern.tolist()
    movies_df = pd.read_pickle('movies.pkl')

    for pattern in pattern_list:
        cols = cycle(st.columns(len(pattern))) # st.columns here since it is out of beta at the time I'm writing this
        result = movies_df.loc[pattern]

        images = result.urls.tolist()
        caption = result.movie_name.tolist()
        # st.dataframe(images)
        for idx, image in enumerate(images):
            next(cols).image(image, width=200, caption=caption[idx])
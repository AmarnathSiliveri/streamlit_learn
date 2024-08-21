import streamlit as st
st.write("RajiniFIED")

st.title("We will be working with dataframes and its periphery")

import pandas as pd


st.json(
    {
        "hero": "Prabhas",
        "Director": "NAGI MOWA",
        "Other Actors": [
            "Amithabhbachaan",
            "Kamal Hasan",
            "Deepika Padukone",
            "Kyra and roxie papa",
        ],
    }
)
data={
    'heroes':['Prabhas','Rajini','Vijay sethupathi','Ajith','Surya'],
    'heroins':['Anushka','Aishwarya','Trisha','Nayanthara','Jyothika'],
    'directors':['SS Rajamouli','Shankar','Maniratnam','GVM','Bala'],
    'movies':['Baahubali','Endhiran','Super Deluxe','Veeram','Ayan']
}

df=pd.DataFrame(data)

df #it will display the dataframe in the table format and its a magic command


#filtering the data

#st.write(df['heroes']) #it will display the heroes column

import pandas as pd
import streamlit as st

# Sample DataFrame
movie_data = {
    'heroes': ['Prabhas', 'Rajini', 'Vijay sethupathi', 'Ajith', 'Surya'],
    'flops': [0, 1, 2, 3, 4],
    'hits': [5, 6, 7, 8, 9],
    'movies': [23, 45, 67, 89, 90]
}

movie_dataframe = pd.DataFrame(movie_data)

# Streamlit sliders for user input
flops_f = st.slider("Select the number of flops", 0, 4, step=1, value=(2, 3))
hits_f = st.slider("Select the number of hits", 5, 9, step=1, value=(6, 7))
movies_f = st.slider("Select the number of movies", 23, 90, step=1, value=(67, 89))

# Filter DataFrame based on user input
filtered_data = movie_dataframe[
    (movie_dataframe['flops'] >= flops_f[0]) & (movie_dataframe['flops'] <= flops_f[1]) &
    (movie_dataframe['hits'] >= hits_f[0]) & (movie_dataframe['hits'] <= hits_f[1]) &
    (movie_dataframe['movies'] >= movies_f[0]) & (movie_dataframe['movies'] <= movies_f[1])
]

# Display filtered data
st.write(filtered_data)


filtered_data
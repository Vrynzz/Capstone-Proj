import streamlit as st
import pandas as pd
import json

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="Explore Singapore Films"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🎬 Explore Singapore Films 🎬")

st.markdown(
    """
    Please use this page to explore Singapore Films, specially curated to be suitable for different types of events. 

    The films are organised into the themes of: 
    - 👪 Family Friendly 
    - 🌍 World Cinema
    - 🌏 Southeast Asian Cinema
    
    The table below is interactive and can be sorted/searched. Give it a try! 🤗

    
    """
    )

# Load the JSON file
filepath = './data/film_programming.json'
with open(filepath, 'r', errors='ignore') as file:
    json_string = file.read()
    dict_of_films = json.loads(json_string)
    print(dict_of_films)

list_of_dict = []
for film_name, details_dict in dict_of_films.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)

st.data_editor(
    df,
    column_config={
        "Trailer_Link": st.column_config.LinkColumn(
            "Trailer Link",
             display_text="Link"
        ),
    },
    hide_index=True,
    use_container_width=True
)

st.markdown(
    """
    For a more comprehensive list of Singapore Films, please explore the [Film Directory](https://www.imda.gov.sg/about-imda/research-and-statistics/support-for-industry-sectors/media/film/directory)

    For information on film ratings, please refer to [Film Classification](https://www.imda.gov.sg/regulations-and-licensing-listing/content-standards-and-classification/standards-and-classification/films).

    """
)
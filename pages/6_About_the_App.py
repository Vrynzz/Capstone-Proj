import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About SFC's Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.divider()

st.subheader("Project Scope")

st.markdown(
    """
    The Singapore Film Commission (SFC) receives many queries on a daily basis. The top two queries are relating to filming in Singapore and for recommendation of films to programme for various events. 

    """
    )

st.subheader("Objectives")

st.markdown(
    """
    1. Build a user friendly interface for users to explore Singapore films and understand location filming in Singapore.
    
    2. Build a chatbot for users to query on exploring Singapore films and understanding location filming in Singapore.

    """
    )

st.subheader("Data Sources")

st.markdown(
    """
    1. 🎬 Explore SG Films 
        Curated list of Singapore Films, with some data replaced by dummy data. Other data are available publicly from various sources, including:
        -  [Film Directory](https://www.imda.gov.sg/about-imda/research-and-statistics/support-for-industry-sectors/media/film/directory)
        -  [Film Classificstion Database](https://imdaonline.imda.gov.sg/classification/search/film/default.aspx)  
    """
    )
 
st.markdown(
    """   
    2. 🎥 Location facilitation
        - [Filming in Singapore Guidelines](https://www.imda.gov.sg/about-imda/research-and-statistics/support-for-industry-sectors/media/film-sector/filming-in-singapore)

    """
    )

st.subheader("Features")

st.markdown(
    """
    1. Chatbot for Exploring SG Films: 
        - Read information from json to answer user's queries; and return a list of suitable film titles if applicable. 
    
    2. Chatbot for Understanding Location Filming in SG:
        - Read information from PDF to answer user's queries.
    """
    )

st.subheader("Repository")

st.markdown(
    """
    You can find the source code for this project on GitHub: https://github.com/Vrynzz/Capstone-Proj
    """
    )

st.subheader("Created by")

st.markdown(
    """
    Ang Yi Eng / IMDA
    """
    )


st.divider()


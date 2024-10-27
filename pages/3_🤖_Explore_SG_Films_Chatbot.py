# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password 

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Explore SG Films - Chatbot"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🤖 Explore SG Films - Chatbot 🤖")

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.markdown(
    """
    Please use this 🤖 Chatbot only for queries relating to exploring Singapore films, such as types of films (e.g. Family Friendly, World Cinema, Southeast Asian Cinema), specific film titles.

    """
    )

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, film_details = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)

    st.divider()

    print(film_details)
    df = pd.DataFrame(film_details)


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


with st.expander("Disclaimer"):
    st.write('''
    IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalised advice.

    ''')

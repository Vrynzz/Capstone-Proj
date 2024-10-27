# Set up and run this Streamlit App
import streamlit as st


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="SFC's Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🍿 Singapore Film Commission 🍿")

st.markdown(
    
    """
    This is a Streamlit App for Singapore Film Commission (SFC). 

    Please use this app to:  
    
    - 🎬 Explore Singapore Films 
    - 🎥 Understand Location Filming in SG

    Use the respective 🤖 Chatbot function to query on the two above topics!

    """
    )

st.image('data/SFC.png')

with st.expander("Disclaimer"):
    st.write('''
    
             IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
             
             Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
             
             Always consult with qualified professionals for accurate and personalized advice.
    ''')

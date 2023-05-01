import streamlit as st
from modules.get_data import get_first_page


# app intro
st.title("hh.ru salary graph by regions")

st.subheader("Welcome to the job market analysis tool.")

st.write(
    """ This Python Streamlit app allows you to see graphics for salary data from hh.ru, a popular job portal in Russia, 
    and analyze the current job market for any given job. After entering the job name, 
    the app will retrieve and present graphical representations of the minimum, maximum, or average 
    salary for that job. The data will be grouped and sorted by regions across Russia. This app provides 
    real-time and up-to-date information about the job market, which can be beneficial for job seekers and 
    employers alike. The data presented through the app can help job seekers to better understand salary 
    trends and make decisions about their careers. """
)


# get user input
vacancy_name = st.text_input(
    "Enter name of vacancy you want to get info about. For example: Middle React",
    placeholder="Enter name here...",
)

# check if user entered something
if vacancy_name:
    st.subheader(f"Results for '{vacancy_name}'")
    data = get_first_page(vacancy_name)
    st.write(data)

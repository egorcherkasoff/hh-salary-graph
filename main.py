import streamlit as st
import plotly.express as pl
from modules.get_data import get_first_page


# app intro
st.title("hh.ru salary graph by regions")

st.subheader("Welcome to the job market analysis tool.")

st.write(
    """ This Python Streamlit app allows you to see graphics for salary data from hh.ru, a popular job portal in Russia, 
    and analyze the current job market for any given job. After entering the job name, 
    the app will retrieve and present graphical representations of the max, min, and average 
    salary for that job. The data will be grouped by regions across Russia. This app provides 
    real-time and up-to-date information about the job market, which can be beneficial for job seekers and 
    employers alike. The data presented through the app can help job seekers to better understand salary 
    trends and make decisions about their careers. """
)


# get user input
vacancy_name = st.text_input(
    "Enter name of vacancy you want to get info about. For example: Middle React",
    placeholder="Enter name here...",
)

# this will be inserted to histfunc to calc salary
calc_funcs = {"Avg": "avg", "Max": "max", "Min": "min"}

# user's selected function
func_key = st.selectbox("Which salaries you want to see?", options=calc_funcs)

# check if user entered something
if vacancy_name:
    st.subheader(f"Results for '{vacancy_name}'")
    cities, salaries = get_first_page(vacancy_name.replace(" ", "+"))

    # if there are no data, user will get warning
    try:
        # make plotly figure
        figure = pl.histogram(
            x=cities,
            y=salaries,
            histfunc=calc_funcs[func_key],  # user selected function
            labels={"x": "Cities", "y": "Salaries"},
        )
        st.plotly_chart(figure_or_data=figure, theme="streamlit")
    except ValueError:  # no data exception
        st.warning(
            "Looks like your query is invalid or theres no data on it! Try another one!"
        )

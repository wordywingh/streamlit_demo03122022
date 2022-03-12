import streamlit as st
import pandas as pd
import numpy as np

# this will tell you if number is even or odd
def my_func(user_input):
    if (user_input % 2) == 0:
        return "even"
    else:
        return "odd"
    return

st.title("Even Odd Wizard")

form = st.form(key = "my_form")

with form:
    user_input = st.text_area("What number are you wondering about")
    submitted = st.form_submit_button(label="Submit")

if submitted:
    st.success(my_func(int(user_input)))
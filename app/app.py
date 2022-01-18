import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from about_page import show_about_page


# sidebar
page = st.sidebar.selectbox('Explore or Predict', ('Explore', 'Predict', 'About'))
if page == 'Predict':
    show_predict_page()
elif page == 'Explore':
    show_explore_page()
else:
    show_about_page()
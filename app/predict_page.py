import streamlit as st
import pickle
import numpy as np


def load_model():
    """
    Load the cached regression model
    :return: <file> regression model
    """
    with open('assets/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def show_predict_page():
    """
    Display prediction page on Streamlit app
    :return: None
    """
    st.title('Predict Software Developer Salaries')
    st.write('### By Location and Qualifications')
    countries = (
        'United States of America',
        'India',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden',
        'Turkey',
        'Switzerland',
        'Israel',
        'Norway',
    )
    education = (
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Master’s degree',
        'Post grad',
    )
    country = st.selectbox('Country', countries)
    education = st.selectbox('Education Level', education)
    experience = st.slider('Years of Experience', 0, 50, 3)
    submit = st.button('Calculate Salary')
    # calculate button clicked
    if submit:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f'Estimated yearly salary: ${salary[0]:,.2f} USD')


# load in data
data = load_model()
regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

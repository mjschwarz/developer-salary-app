import streamlit as st
import pandas as pd
import plotly.express as px


def shorten_categories(categories, cutoff):
    """
    Remove data points which are outside cutoff range
    :param categories: <pandas.Series> category, value (eg. 17, 8276)
    :param cutoff: <int> cutoff value
    :return: <dict> category: value with outlier values removed
    """
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    """
    Clean the experience data - convert to float
    :param x: <int/str> experience data
    :return: <float> cleaned experience data
    """
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    """
    Clean the education data - shorten/combine titles
    :param x: <str> education data
    :return: <str> cleaned education data
    """
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

@st.cache
def load_data():
    """
    Load in and cache the survey data
    :return: <pandas.DataFrame> survey data
    """
    df = pd.read_csv('assets/survey_results_public_2021.csv')
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    return df

def show_explore_page():
    """
    Display explore page on Streamlit app
    :return: None
    """
    # header
    st.title('Explore Software Developer Salaries')
    st.write('### Stack Overflow Developer Survey 2021')
    # responses - pie chart
    st.write('#### Number of responses per country')
    country = df['Country']
    data = country.value_counts()
    fig = px.pie(country, values=data, names=data.index)
    st.plotly_chart(fig)
    # country - bar chart
    st.write('#### Mean Salary by Country')
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    # experience - line chart
    st.write('#### Mean Salary by Experience')
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)


# load in data
df = load_data()
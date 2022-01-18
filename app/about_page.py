import streamlit as st


def show_about_page():
    """
    Display about page on Streamlit app
    :return: None
    """
    # header
    st.title('About the App')
    st.write("""
        ### Using Machine Learning to Predict Developer Salaries
        - All data comes from the [Stack Overflow 2021 Developer Survey](https://insights.stackoverflow.com/survey).
        - On the explore page, this data is filtered for outliers, minimum sample size, and displayed graphically.
        - The prediction page utilizes a machine learning model to apply a decision tree regression to the survey data.
        - The model considers important factors such as Country of Employment, Education Level, and Years of Professional Experience.
        - The machine learning model is then used to predict the expected salary based upon the supplied parameters.
        - To see the source code for this project, visit this [GitHub Repository](https://github.com/mjschwarz/developer-salary-app.git).
        """)

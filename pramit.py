 import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Marketing Data Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.write("First 5 rows of the dataset:")
    st.write(df.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Select columns for visualization
    st.subheader("Visualizations")
    st.write("Select columns for visualization")

    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    if numerical_columns:
        st.write("Numerical Columns")
        num_column = st.selectbox("Select Numerical Column", numerical_columns)

        # Histogram
        st.write(f"Histogram of {num_column}")
        plt.figure(figsize=(10, 6))
        sns.histplot(df[num_column], kde=True)
        st.pyplot(plt)

        # Boxplot
        st.write(f"Boxplot of {num_column}")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[num_column])
        st.pyplot(plt)

    if categorical_columns:
        st.write("Categorical Columns")
        cat_column = st.selectbox("Select Categorical Column", categorical_columns)

        # Bar chart
        st.write(f"Bar Chart of {cat_column}")
        plt.figure(figsize=(10, 6))
        sns.countplot(x=cat_column, data=df)
        st.pyplot(plt)

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    if len(numerical_columns) > 1:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df[numerical_columns].corr(), annot=True, cmap='coolwarm')
        st.pyplot(plt)
    else:
        st.write("Not enough numerical columns for correlation heatmap")

    # Pairplot
    st.subheader("Pairplot")
    if len(numerical_columns) > 1:
        st.write("Pairplot of numerical columns")
        sns.pairplot(df[numerical_columns])
        st.pyplot(plt)
    else:
        st.write("Not enough numerical columns for pairplot")

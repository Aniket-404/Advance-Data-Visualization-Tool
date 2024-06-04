# Copyright (c) 2024 Aniket Kamble
# SPDX-License-Identifier: MIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def main():
    st.set_page_config(page_title="Psychometric Template Generator", layout="wide")
    st.title("📊 Psychometric Template Generator")

    # Sidebar for file upload and chart selection
    with st.sidebar:
        st.header("Upload Data")
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        display_data_preview(df)
        selected_features = select_features(df)

        if selected_features:
            if validate_features(df, selected_features):
                chart_type = select_chart_type()
                display_chart(df, selected_features, chart_type)

def display_data_preview(df):
    # Displays a preview of the uploaded data
    with st.expander("Preview of the uploaded data", expanded=False):
        st.write(df.head())

def select_features(df):
    # Allows the user to select features for comparison
    selected_features = st.multiselect("Select features for comparison", df.columns)
    if not selected_features:
        st.warning("Please select at least one feature for comparison.")
    return selected_features

def validate_features(df, selected_features):
    # Validates that selected features are numeric
    if not all(df[feature].dtype in (int, float) for feature in selected_features):
        st.error("Selected features must be numeric for visualization.")
        return False
    return True

def select_chart_type():
    # Allows the user to select the type of chart
    with st.sidebar:
        st.header("Chart Selection")
        return st.selectbox(
            "Select the type of chart",
            ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Histogram", "Heatmap"],
        )

def display_chart(df, selected_features, chart_type):
    # Displays the selected chart
    st.subheader(f"{chart_type}")
    if chart_type == "Line Chart":
        generate_line_chart(df, selected_features)
    elif chart_type == "Bar Chart":
        generate_bar_chart(df, selected_features)
    elif chart_type == "Scatter Plot":
        generate_scatter_plot(df, selected_features)
    elif chart_type == "Pie Chart":
        generate_pie_chart(df, selected_features)
    elif chart_type == "Histogram":
        generate_histogram(df, selected_features[0])
    elif chart_type == "Heatmap":
        generate_heatmap(df, selected_features)

def generate_line_chart(df, selected_features):
    fig, ax = plt.subplots(figsize=(15, 8))
    for feature in selected_features:
        ax.plot(df.index, df[feature], label=feature)

    ax.set_xlabel("Index")
    ax.set_ylabel("Values")
    ax.set_title("Line Chart")
    ax.legend()
    st.pyplot(fig)

def generate_bar_chart(df, selected_features):
    fig = px.bar(df, x=df.index, y=selected_features, barmode="group")
    fig.update_layout(title="Bar Chart", xaxis_title="Index", yaxis_title="Values", height=600, width=1000)
    st.plotly_chart(fig)

def generate_scatter_plot(df, selected_features):
    fig = px.scatter(
        df,
        x=selected_features[0],
        y=selected_features[1],
        title="Scatter Plot",
        labels={
            selected_features[0]: selected_features[0],
            selected_features[1]: selected_features[1],
        },
        height=600,
        width=1000
    )
    st.plotly_chart(fig)

def generate_pie_chart(df, selected_features):
    fig = px.pie(df, names=selected_features, title="Pie Chart", hole=0.3, height=600, width=1000)
    st.plotly_chart(fig)

def generate_histogram(df, selected_feature):
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.hist(df[selected_feature], bins=20, edgecolor="black")
    ax.set_xlabel(selected_feature)
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram")
    st.pyplot(fig)

def generate_heatmap(df, selected_features):
    fig = px.imshow(df[selected_features].corr(), title="Heatmap", height=600, width=1000)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

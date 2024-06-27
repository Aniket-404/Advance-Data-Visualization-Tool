# 📊 Advance Data Visualization Tool

Psychometric Template Generator is a data visualization tool built using Python, Streamlit, Pandas, Matplotlib, and Plotly. It allows users to upload a CSV file and create intutive data visualizations just by selecting the features from the data.

## ✨ Features

- Upload CSV data: Allows users to upload CSV files containing the data for psychometric testing.
- Data preview: Displays a glimpse of the uploaded data using a Streamlit expander.
- Feature selection: Enables users to choose specific features (columns) for comparison in the charts.
- Feature validation: Ensures the selected features are numerical for visualization.
- Chart selection: Provides a dropdown menu for users to select the desired chart type (Line, Bar, Scatter, Pie, Histogram, Heatmap).
- Chart generation: Creates charts based on the chosen chart type and displays them on the Streamlit app.
- Line chart: Plots lines for each selected feature over the data index.
- Bar chart: Creates a bar chart to compare the values of selected features across the data index.
- Scatter plot: Generates a scatter plot to visualize the relationship between two selected features.
- Pie chart: Creates a pie chart to represent the distribution of data across the selected features.
- Histogram: Generates a histogram to show the frequency distribution of a single selected feature.
- Heatmap: Creates a heatmap to visualize the correlation between all selected features.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pands
- Matplotlib
- Plotly

## 🚀 Installation

1. Clone this repository to your local machine using:
   - `git clone https://github.com/Aniket-404/Psychometric-Template-Generator.git`
2. Install the required Python packages using pip:
   - `pip install -r requirements.txt`

## 💡 Usage

1. Run the app using:
   - `streamlit run app.py`
2. Upload the dataset.
3. Select features from the data.
4. Select the Visualization from the given visualization charts and plots.
5. You're Done, You'll get the visualization from selected features.

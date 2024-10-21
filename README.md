# Project-Soft-Development
Overview:

This project is designed for vehicle data analysis and management using Python and Jupyter Notebooks. It focuses on analyzing vehicle data such as make, model, year, price, and fuel efficiency using various data science tools. The project reads vehicle data from a CSV file and processes it for different tasks like exploratory data analysis (EDA), visualization, and reporting.

Features:

Data Analysis: Load and analyze a dataset of vehicles from vehicles_us.csv.
Interactive Visualizations: Create plots and charts to explore vehicle price trends, fuel efficiency, and more.
Streamlit Integration: Provides a web-based interface using Streamlit to interact with the data.
Jupyter Notebooks: Contains multiple notebooks for step-by-step analysis and exploration.
Technologies Used
Python: Core programming language.
Pandas: For data manipulation and analysis.
Streamlit: For building an interactive dashboard.
Plotly: For data visualizations.
Jupyter Notebook: To explore data and build models.
CSV: Dataset stored in vehicles_us.csv.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/stefanodasilva/Project-Soft-Development.git
cd Project-Soft-Development
Create a Virtual Environment (Optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application: To start the Streamlit app:

bash
Copy code
streamlit run app.py
Open your browser and go to http://localhost:8501/ to interact with the application.

Usage
Jupyter Notebooks: Access the notebooks under the Notebooks folder to explore the vehicle dataset and conduct various analyses.
Streamlit App: Use the web interface to filter and visualize vehicle data interactively.
Dataset
The vehicles_us.csv file contains various details about vehicles in the U.S. market, including:

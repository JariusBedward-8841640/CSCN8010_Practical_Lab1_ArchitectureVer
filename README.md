# Workshop: Linear Regression Architecture Workshop

##  Project Members:
    1. Jarius Bedward #8841640

## Project Summary:

This project was built off of the Data Streaming Workshop
in which we analyze time-series sensor data from a manufacturing system to detect abnormal 
behaviour using regression and residual analysis. This Workshop now has us model our project off of ML ops in 
transforming our notebook into a project using python scripts and a modular design. 

c5c544d

## **Key Features:**
- **Data Preprocessing:**
  - Filter out rows where all sensor readings are zero
  - Fill missing values
  - Normalize and standardize data fro consistent modeling
- **Regression Modelling:**
  - Linear regression on each sensor axis
  - Identification of slope and intercept for analysis
- **Synthetic Data Generation**
  - Generate synthetic test data based on regression predictions
  - Adding realistic deviations using residuals from the traning data
- **Residual Analysis:**
  - Analyze residuals to determine threshold limits for alerts and errors
  - Visualization of residual distributions
-  **Alert and Error Detection:**
  - Detect continuous periods exceeding thresholds
  - Log alerts and errors with start/end timestamps
- **Visualization:**
  - Scatter plots with regression lines
  - Overlay of alerts as (yellow) and errors as (orange) with duration annotations
- **Results Saving:**
  - Export thresholds and detected events to CSV reporting

## Modular Design Decisions
    - Many folders were created to split up different parts of the workflow
    - Each module handles a certain responsibility. For example synthetic data preperation and Data preperation from the db is handled in the DataPreperation folder while the  RegressionModel is handled in ModelTraning.
      This reduces the complexity of a single file
    - By modularizing the project and clearly seperating everything it makes it much easier to read and for collaborators to understand the workflow
    -

## Requirements:
    - pip install -r requirements.txt

##  🎯  How to Run:

1. Clone this repo (git clone <repo-url> cd <repo-folder)
2. Install Required Dependencies: "pip install -r requirements.txt"
4. Create a new .env file containing your Neon database URL
5. In the env file add the connection string from Neon ( DATABASE_URL=<your_database_url> )
6. Run all the Orchestrator.py file within the project


🤝 Contributing
This is a Practical Lab developed for CSNC8010. If any questions arise do not hesitate to contact the project member.
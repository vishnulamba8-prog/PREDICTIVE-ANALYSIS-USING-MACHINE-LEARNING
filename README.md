# PREDICTIVE-ANALYSIS-USING-MACHINE-LEARNING

COMPANY - CODTECH IT SOLUTIONS PRIVATE LIMITED

NAME - VISHNU LAMBA

INTERN ID - CTIS2986

DOMAIN - DATA ANALYTICS

DURATION - 8 WEEKS

MENTOR - NEELA SANTOSH

DESCRIPTION OF THE TASK 1

# Task 2 – Predictive Analysis Using Machine Learning  
# Project Overview

This project was completed as part of the CODTECH Data Analytics Internship (Task 2 – Predictive Analysis Using Machine Learning). 
The objective of this task was to build a machine learning model capable of predicting Apple's Earnings Per Share (EPS) based on its historical financial performance.

The dataset used in this project contains Apple’s financial data from 2009 to 2024, including key performance indicators such as revenue, net income, gross profit, operating income, total assets, cash on hand, long-term debt and number of employees. 
Using these financial features, a regression-based machine learning model was developed to estimate EPS and evaluate the predictive power of financial metrics.

# Objective of the Project
The primary objective of this project is to:
- Analyze Apple’s historical financial performance.
- Identify relationships between financial indicators and EPS.
- Build a regression model to predict Earnings Per Share.
- Evaluate model performance using appropriate evaluation metrics.
- Interpret results and determine the model’s predictive strength.
This task demonstrates the practical application of supervised machine learning techniques in financial data analysis.

# Dataset Description
The dataset includes annual financial records of Apple from 2009 to 2024. The key features used for prediction include:
- Revenue (millions)
- Net Income (millions)
- Gross Profit (millions)
- Operating Income (millions)
- Total Assets (millions)
- Cash on Hand (millions)
- Long Term Debt (millions)
- Number of Employees
And, the target variable for prediction is:
- Earnings Per Share (EPS)

Before model training, missing values were removed to ensure clean and consistent data for analysis.

# Methodology

The project follows a structured machine learning workflow:
## 1. Data Loading and Exploration
The dataset was loaded using Pandas and initial exploration was performed to check:
- Dataset shape
- Data types
- Column names
- Missing values
This step ensures a clear understanding of the dataset structure.

## 2. Data Preprocessing
Rows containing missing values were removed to maintain data quality. The independent variables (features) and dependent variable (target) were separated.

## 3. Train-Test Split
The dataset was divided into training and testing sets using an 80-20 split:
- 80% data for training
- 20% data for testing
This ensures that model performance is evaluated on unseen data.

## 4. Model Building
A Linear Regression model from Scikit-learn was used for prediction. Linear Regression was chosen because:
- EPS is a continuous variable.
- The relationship between financial indicators and EPS can be modeled linearly.
- It provides interpretable coefficients.
The model was trained using the training dataset.

## 5. Model Evaluation
After training, predictions were made on the test dataset. The model was evaluated using:
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

The R² score helps determine how well the financial features explain the variation in EPS.
Additionally, an Actual vs Predicted scatter plot was created to visually compare model performance.

## 6. Results & Interpretation
The model successfully predicted EPS using Apple’s financial indicators. The R² score indicates the strength of the model’s predictive capability:
- R² ≥ 0.90 → Excellent model performance
- R² ≥ 0.75 → Strong predictive power
- R² ≥ 0.50 → Moderate prediction accuracy
The evaluation results demonstrate how financial performance directly influences EPS and highlight the importance of revenue, profit and operational metrics in predicting shareholder value.

### Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Linear Regression Algorithm

### Key Learnings

Through this project, I gained practical experience in:
- Data preprocessing and cleaning
- Feature selection for regression problems
- Model training using supervised learning
- Performance evaluation using statistical metrics
- Visualizing prediction accuracy

This task strengthened my understanding of predictive modeling and its real-world application in financial analytics.

### Conclusion
This project successfully demonstrates the application of Machine Learning in financial forecasting. 
By leveraging historical financial data, the model predicts Apple’s Earnings Per Share (EPS) with measurable accuracy.
The project highlights how financial indicators can be transformed into actionable insights using data science techniques. 
This predictive analysis provides a foundation for more advanced financial forecasting and investment analytics in the future.

## OUTPUT
<img width="780" height="287" alt="Image" src="https://github.com/user-attachments/assets/880755bf-d461-44d5-b16f-d751f0f0cc68" /> 

<img width="792" height="642" alt="Image" src="https://github.com/user-attachments/assets/46f87222-3545-4900-a23f-8787e59be06e" /> 

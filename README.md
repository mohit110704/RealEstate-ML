# Real Estate Price Predictor & Analytics (Gurugram)

## Project Overview
This project is about predicting the prices of properties in Gurugram using machine learning. I collected property data from the 99acres website and built a system that can predict property prices and show useful analytics. The project also includes visualizations and analysis to help understand property trends.

## Dataset

- **Data Size:** ~3000 property listings from Gurugram.
- **Columns:**
  - `property_name` – Type of the property Flat or House 
  - `link` – URL of the listing
  - `society` – Society/Project name
  - `price` – Property price (target variable for prediction)
  - `area` – Area in numeric value
  - `areaWithType` – Area with unit (like sqft, sqm)
  - `bedRoom`, `bathroom`, `balcony`, `additionalRoom` – Number of rooms
  - `address` – Property address
  - `floorNum` – Floor number
  - `facing` – Direction property is facing
  - `agePossession` – Age or possession of the property
  - `nearbyLocations` – Nearby places (school, metro, market, etc.)
  - `description` – Text description of property
  - `furnishDetails` – Furnishing details (furnished, semi-furnished, unfurnished)
  - `features` – Additional features
  - `rating` – User ratings (if available)
  - `property_id` – Unique property identifier


## Why I Chose This Project
- Real estate is a growing field and property prices are very important for buyers and sellers.
- I wanted to practice data collection, cleaning, analysis, and machine learning in a real-world scenario.
- It helped me learn how to handle messy data and make meaningful predictions.

## What I Did in This Project

### 1. Data Collection
- Collected property listings from 99acres.com for Gurugram.
- Dataset included features like location, size, property type, and price.

### 2. Data Cleaning & Preprocessing
- Handled missing values using **median imputation**.
- Detected and removed outliers using **box plots and scatter plots**.
- Fixed errors and inconsistencies in the data.

### 3. Feature Engineering & Selection
- Created new features where needed to improve model predictions.
- Selected the most important features using different techniques for better accuracy.

### 4. Model Training & Evaluation
- Trained multiple machine learning models:
  - **XGBoost** (Best model, R² = 0.90, MAE = 0.44)
  - Extra Trees
  - Random Forest
  - Gradient Boosting
  - Decision Tree
  - MLP
  - AdaBoost
  - Linear Regression, Ridge, Lasso, SVR
- Evaluated models using **R² score** and **Mean Absolute Error (MAE)**.
- XGBoost gave the best results.

### 5. Exploratory Data Analysis (EDA) & Visualization
- Visualized property price distribution, trends, and correlations using scatter plots, box plots, and other charts.
- Helped understand which factors affect property prices the most.

### 6. Deployment
- Built a **Streamlit web app** for users to input property features and get predicted prices.
- The app also shows analytics and visualizations of the data.

## What I Learned
- How to collect and clean real-world data from websites.
- How to handle missing values and outliers effectively.
- How to select important features to improve model performance.
- How to train, evaluate, and compare different machine learning models.
- How to deploy a machine learning project using Streamlit.
- How to communicate technical results in a simple way through visuals.

## Challenges Faced
- Data had missing and inconsistent values, which needed careful cleaning.
- Some features had outliers, which affected the models.
- Choosing the best model required testing many algorithms and tuning parameters.
- Deployment required learning Streamlit integration with the trained model.

## Why This Project is Useful
- Helps buyers and sellers make informed decisions based on predicted prices.
- Provides a visual understanding of property trends in Gurugram.
- Shows a complete workflow of a real-world data science project from data collection to deployment.



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

## 7. Analytics Module & Prediction

After deployment, the Streamlit app includes a comprehensive **Analytics Module** with the following features:

### Analytics Visualizations:
- **Sector-wise Price per Sqft GeoMap** – Shows how price per sqft varies across different sectors in Gurugram.  
- **Features WordCloud** – Highlights the most common property features.  
- **Area vs Price Scatterplot** – Visualizes the relationship between property area and price.  
- **BHK Pie Chart** – Shows the percentage of properties with different number of bedrooms in each sector.  
- **Side-by-Side BHK Price Comparison (Box Plot)** – Compares prices for different BHK properties across sectors.  
- **Price Distribution: Flat vs House** – Shows how prices differ between flats and houses.

### Prediction Module:
- Users can enter property details such as:  
  - Property Type  
  - Sector  
  - Number of Bedrooms  
  - Number of Bathrooms  
  - Balconies  
  - Age of Property  
  - Built-Up Area (in sqft)  
  - Servant Room  
  - Store Room  
  - Furnishing Type  
  - Luxury Type  
  - Floor Type  

- The module predicts the **expected price range** using the trained model (XGBoost).  
- The predicted price is shown as a **range**, e.g., 22 Lacs ± a certain value, along with the **Mean Squared Error (MSE)** to indicate accuracy.  

This module allows users to **quickly estimate property prices** and analyze trends across Gurugram sectors in an interactive way.

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

## Conclusion
This project successfully demonstrates an **end-to-end workflow** of a real-world data analysis project with ML for predicting property prices in Gurugram.  

Key outcomes:  
- Built a **robust ML model** (XGBoost) achieving **high accuracy** (R² = 0.90, MAE = 0.44).  
- Gained insights into **property trends**, such as how area, location, and amenities affect prices.  
- Developed a **user-friendly Streamlit app** for price prediction and analytics.  

Future improvements could include:  
- Collecting **more data** from additional sources to improve model accuracy.  
- Incorporating **temporal trends** (price changes over time) for better predictions.  
- Adding **more interactive visualizations** in the app for enhanced user experience.  

Overall, this project provides **practical insights** for buyers, sellers, and real estate analysts while showcasing skills in **data collection, cleaning, feature engineering, machine learning, and deployment**.


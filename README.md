# Calorie Burn Prediction 🏋️‍♂️

This project is an end-to-end machine learning regression model to predict the number of calories burned based on user input features like age, gender, height, weight, heart rate, body temperature, and duration of exercise. The model is deployed as a web app using **Streamlit**.

---

## **Table of Contents**
1. [Problem Statement](#problem-statement)
2. [Dataset](#dataset)
3. [Steps](#steps)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Deployment](#deployment)
8. [Future Work](#future-work)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Problem Statement**
The goal of this project is to predict the number of calories burned during exercise based on features such as:
- Age
- Gender
- Height
- Weight
- Heart Rate
- Body Temperature
- Duration of Exercise

This is a **regression problem**, and the model is trained to predict continuous values (calories burned).

---

## **Dataset**
The dataset used for this project contains the following features:
- **Age**: Age of the individual (in years).
- **Gender**: Gender of the individual (0 = Female, 1 = Male).
- **Height**: Height of the individual(in cm)
- **Weight**: Weight of the individual(in kg)
- **Heart Rate**: Heart rate during exercise (in bpm).
- **Body Temperature**: Body temperature during exercise (in °C).
- **Duration**: Duration of exercise (in minutes).
- **Calories**: Calories burned (target variable).

The dataset is available in the `data/` directory.

---

## **Steps**
1. **Data Collection**: Loaded the dataset from a CSV file.
2. **Data Preprocessing**:
   - Handled missing values (if any).
   - Encoded categorical variables (e.g., gender).
   - Scaled numerical features using `StandardScaler`.
3. **Exploratory Data Analysis (EDA)**:
   - Visualized distributions and correlations.
   - Identified outliers and trends.
4. **Model Selection**:
   - Tested multiple regression algorithms (e.g., Linear Regression, Random Forest, XGBoost).
   - Selected the best-performing model (e.g., Random Forest).
5. **Model Training**:
   - Split the data into training and testing sets (80:20).
   - Trained the model on the training set.
6. **Model Evaluation**:
   - Evaluated the model using metrics like **RMSE** and **R² Score**.
7. **Model Deployment**:
   - Saved the trained model using `joblib`.
   - Created a web app using **Streamlit** for user interaction.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/calorie-prediction.git

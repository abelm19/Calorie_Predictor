#main
import streamlit as st
import pickle
import numpy as np
import base64

# Load your trained model (make sure the 'calorie_pred.pickle' file is in the same directory as the app or provide the path)
with open('calorie_pred.pickle', 'rb') as model_file:
    model = pickle.load(model_file)


# Function to estimate calories using the saved model
def estimate_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    # Gender encoding (assuming model expects numeric encoding)
    gender_value = 1 if gender == 'male' else 0

    # Prepare input features for the model in the correct order
    input_features = np.array([[gender_value, age, height, weight, duration, heart_rate, body_temp]])

    # Make the prediction using the loaded model
    predicted_calories = model.predict(input_features)

    return round(predicted_calories[0], 2)


# Load and encode the background image to base64
# Replace 'your_image.jpg' with the path to your image file
image_path = 'background.jpg'  # Specify your image file path
with open(image_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()

# Inject custom CSS for background and text
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{img_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .custom-text-box {{
        background-color: rgba(0, 0, 0, 0.7);  /* Dark background */
        color: white;  /* White text */
        padding: 20px;
        border-radius: 10px;
        font-size: 18px;
    }}

    body {{
        color: black !important;
    }}
    .streamlit-expanderHeader {{
        color: black !important;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: black !important;
    }}
    .css-1d391kg {{
        color: black !important;
    }}
    .css-1emrehy {{
        color: black !important;
    }}
    /* Change form labels to black */
    label {{
        color: black !important;
    }}
     /* Target radio button labels specifically */
    .stRadio label {{
        color: black !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Calories Burnt Prediction")

# Create the form with custom text box style
with st.form(key='calories_form'):
    # Inputs
    gender = st.radio("Gender", options=["male", "female"], index=1)
    age = st.number_input("Age", value=30, min_value=1)
    height = st.number_input("Height (cm)", value=170, min_value=1)
    weight = st.number_input("Weight (kg)", value=70, min_value=1)
    duration = st.number_input("Duration (minutes)", value=30, min_value=1)
    heart_rate = st.number_input("Heart Rate (beats/min)", value=120, min_value=1)
    body_temp = st.number_input("Body Temperature (°C)", value=37.0)

    # Submit button
    submit_button = st.form_submit_button(label="Estimate Calories")

# Display the result when the form is submitted
if submit_button:
    calories = estimate_calories(gender, age, height, weight, duration, heart_rate, body_temp)
    st.write(f"Estimated Calories Burnt: {calories} kcal")


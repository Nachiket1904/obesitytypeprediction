import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit App
st.title("Obesity Disease Prediction")

# Sidebar form to collect user input
with st.form("obesity_form"):
    st.subheader("Enter Your Details")
    
    Gender = st.selectbox("Gender", options=["Female", "Male"], index=0)
    Age = st.number_input("Age", min_value=0, step=1)
    Height = st.number_input("Height (in cm)", min_value=0.0, step=0.1)
    Weight = st.number_input("Weight (in kg)", min_value=0.0, step=0.1)
    family_history_with_overweight = st.selectbox("Family History with Overweight", options=["yes", "no"])
    FAVC = st.selectbox("Frequent Consumption of High Caloric Food (FAVC)", options=["yes", "no"])
    FCVC = st.number_input("Frequency of Consumption of Vegetables (FCVC)", min_value=0.0, step=0.1)
    NCP = st.number_input("Number of Main Meals (NCP)", min_value=0, step=1)
    CAEC = st.selectbox("Consumption of Food Between Meals (CAEC)", options=["Sometimes", "Frequently", "no", "Always"])
    SMOKE = st.selectbox("Do you smoke?", options=["no", "yes"])
    CH2O = st.number_input("Consumption of Water Daily (in liters)", min_value=0.0, step=0.1)
    SCC = st.selectbox("Calories Consumption Monitoring (SCC)", options=["no", "yes"])
    FAF = st.number_input("Physical Activity Frequency (FAF)", min_value=0.0, step=0.1)
    TUE = st.number_input("Time Using Technology Devices (TUE)", min_value=0.0, step=0.1)
    CALC = st.selectbox("Calories Consumption Monitoring (CALC)", options=["Sometimes", "no", "Frequently"])
    MTRANS = st.selectbox("Mode of Transport (MTRANS)", 
                           options=["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"])
    
    submit = st.form_submit_button("Predict Obesity Level")

# Process input data and predict
if submit:
    # Create input data instance
    input_data = CustomData(
        Gender=Gender,
        Age=Age,
        Height=Height,
        Weight=Weight,
        family_history_with_overweight=family_history_with_overweight,
        FAVC=FAVC,
        FCVC=FCVC,
        NCP=NCP,
        CAEC=CAEC,
        SMOKE=SMOKE,
        CH2O=CH2O,
        SCC=SCC,
        FAF=FAF,
        TUE=TUE,
        CALC=CALC,
        MTRANS=MTRANS
    )

    # Convert to dataframe
    pred_df = input_data.get_data_as_data_frame()
    
    st.write("Input Data:")
    st.dataframe(pred_df)

    # Make prediction
    try:
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(pred_df)
        
        # Obesity Level Mapping
        obesity_dict = {
            0: "Insufficient Weight",
            1: "Normal Weight",
            2: "Obesity Type I",
            3: "Obesity Type II",
            4: "Obesity Type III",
            5: "Overweight Level I",
            6: "Overweight Level II"
        }

        result = obesity_dict.get(prediction[0], "Unknown")
        st.success(f"Predicted Obesity Level: {result}")

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

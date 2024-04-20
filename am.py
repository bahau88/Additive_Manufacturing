import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# Load the trained models
rf_roughness = RandomForestRegressor(n_estimators=100, random_state=42)
rf_tension_strength = RandomForestRegressor(n_estimators=100, random_state=42)
rf_elongation = RandomForestRegressor(n_estimators=100, random_state=42)

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/bahau88/Additive_Manufacturing/main/data.csv')
df['infill_pattern'] = df['infill_pattern'].replace({'grid': 1, 'honeycomb': 2})
df['material'] = df['material'].replace({'abs': 1, 'pla': 2})
df.rename(columns={'tension_strenght': 'tension_strength'}, inplace=True)

# Define features and targets
features = ['layer_height', 'wall_thickness', 'infill_density', 'infill_pattern', 'nozzle_temperature', 'bed_temperature', 'print_speed', 'material', 'fan_speed']
targets = ['roughness', 'tension_strength', 'elongation']

# Train the models
rf_roughness.fit(df[features], df['roughness'])
rf_tension_strength.fit(df[features], df['tension_strength'])
rf_elongation.fit(df[features], df['elongation'])

# Streamlit UI
st.title("Quality Prediction App")
st.write("Enter the parameters below to predict quality metrics.")


 styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        #"icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#9478ff"},
    }

# User input for parameters
layer_height = st.slider("Layer Height", min_value=0.01, max_value=0.1, step=0.01, value=0.02)
wall_thickness = st.slider("Wall Thickness", min_value=5, max_value=10, step=1, value=7)
infill_density = st.slider("Infill Density", min_value=50, max_value=100, step=10, value=90)
infill_pattern = st.selectbox("Infill Pattern", options=['1', '2'])
infill_pattern = 1 if infill_pattern == 'Grid' else 2
nozzle_temperature = st.slider("Nozzle Temperature", min_value=200, max_value=250, step=5, value=225)
bed_temperature = st.slider("Bed Temperature", min_value=50, max_value=100, step=5, value=65)
print_speed = st.slider("Print Speed", min_value=20, max_value=60, step=5, value=40)
material = st.selectbox("Material", options=['1', '2'])
material = 1 if material == '1' else 2
fan_speed = st.slider("Fan Speed", min_value=0, max_value=100, step=5, value=25)

# Predict function
def predict_quality(layer_height, wall_thickness, infill_density, infill_pattern, nozzle_temperature, bed_temperature, print_speed, material, fan_speed):
    parameters = [[layer_height, wall_thickness, infill_density, infill_pattern, nozzle_temperature, bed_temperature, print_speed, material, fan_speed]]
    predicted_roughness = rf_roughness.predict(parameters)[0]
    predicted_tension_strength = rf_tension_strength.predict(parameters)[0]
    predicted_elongation = rf_elongation.predict(parameters)[0]
    return predicted_roughness, predicted_tension_strength, predicted_elongation

# Predict button
if st.button("Predict"):
    roughness, tension_strength, elongation = predict_quality(layer_height, wall_thickness, infill_density, infill_pattern, nozzle_temperature, bed_temperature, print_speed, material, fan_speed)
    st.write(f"Predicted Roughness: {roughness}")
    st.write(f"Predicted Tension Strength: {tension_strength}")
    st.write(f"Predicted Elongation: {elongation}")


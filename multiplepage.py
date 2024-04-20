import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Add image file path
logo_path = "https://www.irt-saintexupery.com/wp-content/uploads/2021/02/logo_IRT-Saint-Exupery.png"

# Display the logo or picture in the sidebar
st.sidebar.image(logo_path, use_column_width=True)

with st.sidebar:
    selected = option_menu(
    menu_title = None,
    options = ["Material","3D Printing","Manufacturing Process","Quick Quotation","Feedback"],
    icons = ["bricks","gear","activity","coin","envelope"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
    styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        #"icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#9478ff"},
    }
)


if selected == "Home":
    st.header('Snowflake Healthcare App')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)

    with st.container():
        c1.write("c1")
        c2.write("c2")

    with st.container():
        c3.write("c3")
        c4.write("c4")

    with c1:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.area_chart(chart_data)
           
    with c2:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
        st.bar_chart(chart_data)

    with c3:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)

    with c4:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
        
    
if selected == "Material":
    st.subheader(f"**You Have selected {selected}**")
    import pandas as pd
    import plotly.graph_objects as go
    import streamlit as st
    import random
    
    # Load the dataset from the provided link
    @st.cache(allow_output_mutation=True)
    def load_data():
        df = pd.read_csv('https://raw.githubusercontent.com/bahau88/Additive_Manufacturing/main/materialpropertiescsv.csv')
        return df
    
    df = load_data()
    
    # Remove commas and convert values to numeric
    numeric_cols = ['Elastic Modulus', 'Shear Modulus', 'Mass Density', 'Tensile Strength', 
                    'Compressive Strength', 'Yield Strength', 'Thermal Expansion Coefficient', 
                    'Thermal Conductivity', 'Specific Heat', 'Material Damping Ratio', 
                    'Minimum Temperature', 'Maximum Temperature', 'Electricity Conductivity', 'Price']
    
    for col in numeric_cols:
        df[col] = df[col].replace(',', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Material selection
    selected_materials = st.multiselect("Select Material(s)", df['Material'].unique())
    
    # Filter the dataset based on selected materials
    filtered_data = df[df['Material'].isin(selected_materials)]
    
    # Axis selection
    x_axis = st.selectbox("Select X Axis", numeric_cols)
    y_axis = st.selectbox("Select Y Axis", numeric_cols)
    
    # Create Plotly graph
    fig = go.Figure()
    
    # Add traces for each selected material
    for material in selected_materials:
        material_data = filtered_data[filtered_data['Material'] == material]
        # Generate a random color for each material
        
        #color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        color = "#9478ff"
        fig.add_trace(go.Scatter(
            x=material_data[x_axis],
            y=material_data[y_axis],
            mode='markers',
            marker=dict(
                size=50,  # Adjust the size of the markers
                symbol='circle',
                color=color,  # Use random color
                line=dict(width=3, color='#f0f0f0')
            ),
            name=material,
            hovertemplate=f'{y_axis}: %{{y}}<br>{x_axis}: %{{x}}'
        ))
        # Add text annotations for material names inside the circles
        fig.add_annotation(
            x=material_data[x_axis].iloc[0],
            y=material_data[y_axis].iloc[0],
            text=material,
            showarrow=False,
            font=dict(color='white', size=12)
        )
    
    # Update layout
    fig.update_layout(
        title=f'{y_axis} vs {x_axis}',
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    # Show the plot
    st.plotly_chart(fig)
    

    
if selected == "3D Printing":
    st.subheader(f"**You Have selected {selected}**")
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
    
    # User input for parameters
    layer_height = st.slider("Layer Height", min_value=0.01, max_value=0.1, step=0.01, value=0.02, key="layer_height")
    wall_thickness = st.slider("Wall Thickness", min_value=5, max_value=10, step=1, value=7, key="wall_thickness")
    infill_density = st.slider("Infill Density", min_value=50, max_value=100, step=10, value=90, key="infill_density")
    infill_pattern = st.selectbox("Infill Pattern", options=['Grid', 'Honeycomb'], key="infill_pattern")
    infill_pattern = 1 if infill_pattern == 'Grid' else 2
    nozzle_temperature = st.slider("Nozzle Temperature", min_value=200, max_value=250, step=5, value=225, key="nozzle_temperature")
    bed_temperature = st.slider("Bed Temperature", min_value=50, max_value=100, step=5, value=65, key="bed_temperature")
    print_speed = st.slider("Print Speed", min_value=20, max_value=60, step=5, value=40, key="print_speed")
    material = st.selectbox("Material", options=['ABS', 'PLA'], key="material")
    material = 1 if material == 'ABS' else 2
    fan_speed = st.slider("Fan Speed", min_value=0, max_value=100, step=5, value=25, key="fan_speed")
    
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

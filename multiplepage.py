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

# Set Streamlit page configuration
st.set_page_config(page_title="Snowflake Healthcare App", page_icon=":hospital:", layout="wide", initial_sidebar_state="expanded")

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
                line=dict(width=3, color='#dad0c0')
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
    

    
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")

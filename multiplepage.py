import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Add your image file path
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
)

# Custom CSS to change the color of the selected menu item
custom_css = f"""
<style>
.sidebar .sidebar-content .{selected.lower()} {{
    background-color: #9478ff; /* Change the color as needed */
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


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
        
    
if selected == "Warehouse":
    st.subheader(f"**You Have selected {selected}**")
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    # run a snowflake query and put it all in a var called my_catalog
    my_cur.execute("select * from SWEATSUITS")
    my_catalog = my_cur.fetchall()
    st.dataframe(my_catalog)
    q1 = st.text_input('Write your query','')
    st.button('Run Query')
    if not q1:
      st.error('Please write a query')
    else:
      my_cur.execute(q1)
      my_catalog = my_cur.fetchall()
      st.dataframe(my_catalog)

    
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")

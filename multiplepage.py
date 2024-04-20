import streamlit as st

def home():
    st.write("Welcome to the Home page!")
    # Add your home page content here

def about():
    st.write("This is the About page.")
    # Add your about page content here

def contact():
    st.write("You're on the Contact page.")
    # Add your contact page content here

# Sidebar navigation
nav_selection = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

# Main content based on sidebar selection
if nav_selection == "Home":
    home()
elif nav_selection == "About":
    about()
elif nav_selection == "Contact":
    contact()

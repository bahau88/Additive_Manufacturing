import streamlit as st
VERSION = "1.27"

def home():
    st.write("Welcome to the Home page!")
    # Add your home page content here

def about():
    st.write("This is the About page.")
    # Add your about page content here

def contact():
    st.write("You're on the Contact page.")
    # Add your contact page content here

# Sidebar navigation with icons and links
nav_selection = st.sidebar.radio("Menu", ["Home 🏠", "About ℹ️", "Contact 📞"])

# Main content based on sidebar selection
if "Home" in nav_selection:
    home()
elif "About" in nav_selection:
    about()
elif "Contact" in nav_selection:
    contact()

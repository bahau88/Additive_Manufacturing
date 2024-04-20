import streamlit as st

VERSION = "1.28"

st.set_page_config(
    page_title=f"New features in Streamlit {VERSION}",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

def draw_sidebar():
    st.sidebar.title("Menu")

    st.sidebar.markdown("""
    - [AppTest](https://release128.streamlit.app/AppTest)
    - [Cache Spinner Improvements](https://release128.streamlit.app/Cache_spinner)
    - [Dataframe Toolbar](https://release128.streamlit.app/Dataframe_toolbar)
    - [st.connection](https://release128.streamlit.app/st.connection)
    """)

def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    intro = """
    This release launches [AppTest](https://release128.streamlit.app/AppTest), improvements to the [cache spinner](https://release128.streamlit.app/Cache_spinner), a handy [dataframe toolbar](https://release128.streamlit.app/Dataframe_toolbar), and [st.connection](https://release128.streamlit.app/st.connection) is no longer experimental – it's fully supported! The release also includes bug fixes.
    """

    release_notes = """
    ---
    **Highlights**
    * 🧪 Introducing a new testing framework for Streamlit apps! Check out our [documentation](https://docs.streamlit.io/library/api-reference/app-testing) to learn how to build automated tests for your apps.
    * 💻 Announcing the general availability of `st.connection`, a command to conveniently manage connections in Streamlit apps. Check out the [docs](https://docs.streamlit.io/library/api-reference/connections/st.connection) to learn more.
    * ❄️ `SnowparkConnection` has been upgraded to the new and improved `SnowflakeConnection` — the same, great functionality *plus more*! Check out our [built-in connections](https://docs.streamlit.io/library/api-reference/connections#built-in-connections).
    * 🛠️ `st.dataframe` and `st.data_editor` have a new toolbar! Users can search and download data in addition to enjoying improved UI for row additions and deletions. See our updated guide on [Dataframes](https://docs.streamlit.io/library/advanced-features/dataframes).

    ... (the rest of your release notes)
    """

    st.markdown(intro, unsafe_allow_html=True)
    st.write(release_notes)

draw_sidebar()
draw_main_page()

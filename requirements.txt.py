try:
    import streamlit as st
    from PIL import Image
    from streamlit_option_menu import option_menu
    st.write("All required packages are installed and working!")
except ImportError as e:
    print(f"Missing package: {e}")
    print("Please run: pip install -r requirements.txt")

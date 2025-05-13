import streamlit as st
import base64
st.set_page_config(page_title="Face recognition attendance system", page_icon="🔒")

# Render the image and heading using flexbox (aligned to the left, moved up)
st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-left: -120px; margin-top: -60px;"> <!-- Move content up -->
        <h1 style="margin: 0; padding-left: 10px; white-space: nowrap;">FACE RECOGNITION BASED ATTENDANCE SYSTEM</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
## 📌 Features

""")

st.markdown(
    f"""
    <div style="display: flex; align-items: center;font-size:20px; margin-left: 110px; margin-top: 20px;">

- 📸 Real-time webcam-based **face recognition**  
- 🧍 New user **face registration**  
- 🧠 128D **facial feature extraction** stored in CSV  
- ✅ Automated **attendance marking**  
- 📊 Attendance logs stored in **SQLite database**  
- 🌐 Web interface built using **Streamlit**  
- ⚙️ Uses **dlib wheel** prebuilt for Python 3.11 (included)
    </div>
    """,
    unsafe_allow_html=True
)





st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-left: 350px; margin-top: 0px;">
        <h3 style="margin: 0; white-space: nowrap; font-size: 24px;">By</h3>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-left: 280px; margin-top: 10px;">
        <h3 style="margin: 0; white-space: nowrap; font-size: 30px;">Pragin.T (D.CE) </h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-left: 160px; margin-top: 80px;">
        <h3 style="margin: 0; white-space: nowrap; font-size: 24px;">Contact :</h3>
        <h3 style="margin: 0; white-space: nowrap; font-size: 24px;">pragin.t.developer@gmail.com</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Hide the Deploy button, header, and footer using CSS
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}  /* Hide the menu */
        footer {visibility: hidden;}      /* Hide the footer */
        header {visibility: hidden;}      /* Hide the header */
    </style>
    """,
    unsafe_allow_html=True
)

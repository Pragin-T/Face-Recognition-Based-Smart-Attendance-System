import streamlit as st
# A library for building custom web applications for data science and machine learning projects.
# Hide the Deploy button, header, and footer using CSS
st.set_page_config(page_title="Face recognition attendance system", page_icon="🔒")

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


st.markdown("""
 <style>
  div {    
 }  
 img{  
 height: 250px;  
 width: 250px;  
 }  
#left {    
 text-align: left;  
 }  
 #center {    
 text-align: center;
 backgroundColor = "#000000"  
 }  
 #right{    
 text-align: right; }
  </style>
  <div id ="ceter">  
  <h2> Click the button below to redirect to local webpage </h2>
  </div>
  """,
              unsafe_allow_html= True )



st.markdown('''
    <div style="text-align: center;padding-top: 100px;">
        <a href="http://127.0.0.1:5000" target="_blank">
            <button style="background-color: GreenYellow; padding: 10px 20px; font-size: 16px;">
                Database
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)
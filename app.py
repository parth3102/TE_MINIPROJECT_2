import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.markdown("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Navigation</title>
    <style>
        * {box-sizing: border-box;}

        body{
            margin: 0;
            padding: 0;
            font-family: Arial;
            text-transform: uppercase;
            font-weight: bold;
        }
        .topnav {
          overflow: hidden;
          background-color: #2f3a4a;
          line-height: 40px;
        }

        .topnav a {
          float: left;
          display: block;
          width:device-width;
          color: black;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
          font-size: 13px;
          color:#fff;
        }

        .topnav a:hover {
          background-color: #ddd;
          color: black;
        }

        .topnav a.active {
          background-color: #2196F3;
          color: white;
        }

    </style>
</head>

<body>
    <div class="topnav">
        <a class="active" href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact Us</a>
    </div>
</body>

</html>
""", unsafe_allow_html=True)


st.markdown('''# **Water Quality Predictor**
A simple web app predicting water quality of Indian States.
''')


names = ["Admin", "User"]
usernames = ["Admin", "User"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "app_home", "auth", cookie_expiry_days=30)

name, authentication_status,username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("User credentials are incorrect")
elif authentication_status == True and username == "User":
    from predict_page import show_predict_page
    show_predict_page()
    authenticator.logout("Logout", "sidebar")

elif authentication_status == True and username == "Admin":
    from admin_predict_page import show_predict_page1 
    from predict_page import show_predict_page
    def page1():
        st.title('Model-1')
        show_predict_page()
    def page2():
       st.title('Model-2')
       show_predict_page1()
    pages = {
           'Model-1': page1,
           'Model-2': page2
       }
       # Define function to run app
    def run_app():
           #st.sidebar.title('Navigation')
           page = st.sidebar.radio('Go to', list(pages.keys()))
           # Call function associated with selected page
           pages[page]()
       # Run the app
    if __name__ == '__main__':
           run_app()
    authenticator.logout("Logout", "sidebar")

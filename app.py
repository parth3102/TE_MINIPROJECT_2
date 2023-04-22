import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

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

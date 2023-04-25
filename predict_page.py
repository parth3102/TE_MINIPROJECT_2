import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_state = data["le_state"]
le_temp = data["le_temp"]

def show_predict_page():
    st.title("Water Quality Prediction")

    st.write("""### We built a model to predict the average water quality of your state's water reservoirs""")
    states = (
            "RAJASTHAN",      
            "GUJARAT",         
            "BIHAR",          
            "ASSAM",           
            "ODISHA",          
            "WEST BENGAL",     
            "MADHYA PRADESH",  
            "Other",           
            "TRIPURA",         
            "PUNJAB",          
            "MAHARASHTRA",     
            "KERALA",          
            "TELANGANA",       
            "HIMACHAL PRADESH",
            "UTTAR PRADESH",   
            "ANDHRA PRADESH",  
            "LAKSHADWEEP",     
            "DELHI",           
            "MIZORAM",         
            "PUDUCHERRY",      
            "UTTARAKHAND",     
            "NAGALAND",        
            "TAMIL NADU",      
            "GOA",            
            "MEGHALAYA",       
            "CHHATTISGARH"  
        )
    

    state = st.selectbox("State",states)
    temp = st.slider("Temperature in celcius", 10, 35)

    ok = st.button("Predict Quality")
    if ok:
        X = np.array([[state, temp]])
        X[:,0] = le_state.transform(X[:,0])
        X[:,1] = le_temp.transform(X[:,1])
        X = X.astype(float)

        quality = regressor.predict(X)
        if quality == 0:
            st.subheader(f"The predicted quality is VERY POOR! You are strongly adviced not to consume it")
        if quality>0 and quality<=1:
            st.subheader(f"The predicted quality is Poor but can be drinkable if you follow the following steps:\n"
                                "1. Boiling and Filtering by filter paper\n"
                                "2. Bleach Disinfection\n"
                                "3. Disinfect through chlorine dioxide tablets")
        if quality>1 and quality<=1.5:
            st.subheader(f"The predicted quality is Good and you can drink it by simply boiling it")
        if quality>1.5:
            st.subheader(f"The predicted quality is Excellent and you can drink it directly")
        

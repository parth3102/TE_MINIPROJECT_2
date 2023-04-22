import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps1.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
le_state = data["le_state"]
le_temp = data["le_temp"]
le_do = data["le_do"]
le_ph = data["le_ph"]
le_bod = data["le_bod"]
le_ni = data["le_ni"]

def show_predict_page1():
    st.title("Water Quality Prediction")

    st.write("""### We built a model to predict the average water quality of your state's water reservoirs""")
    states = ("KERALA",         
          "MAHARASHTRA",    
          "Other",          
          "GOA",            
          "MEGHALAYA",     
          "MANIPUR",        
          "PUNJAB",         
          "TAMILNADU",      
          "GUJARAT",        
          "MIZORAM",        
          "ODISHA",         
          "KARNATAKA",      
          "RAJASTHAN"     
        )

    state = st.selectbox("State",states)
    temp = st.slider("Temperature in celcius", 10, 35)
    do = st.number_input("DO (mg/l)", 0.0,10.0,5.0,step=1.0)
    ph = st.number_input("PH", 6.0,8.0,7.0,step=0.1)
    bod = st.number_input("BOD", 0.0,10.0,5.0,step=1.0)
    ni = st.number_input("NI", 0.0,2.0,1.0,step=0.2)
    

    ok = st.button("Predict Quality")
    if ok:
        X = np.array([[state, temp, do, ph, bod, ni]])
        X[:,0] = le_state.transform(X[:,0])
        X[:,1] = le_temp.transform(X[:,1])
        X[:,2] = le_do.transform(X[:,2])
        X[:,3] = le_ph.transform(X[:,3])
        X[:,4] = le_bod.transform(X[:,4])
        X[:,5] = le_ni.transform(X[:,5])
        X = X.astype(float)

        quality = model.predict(X)
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
import streamlit as st

st.set_page_config(
    page_title="Predicting and Classifying Water Quality, Treatment, and Usage",
    page_icon="💧",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

st.sidebar.success("Home Page")

# st.title("Predicting and Classifying Water Quality, Treatment, and Usage")
st.markdown("<h1 style='text-align: center;'>Predicting and Classifying Water Quality, Treatment, and Usage</h1>",
            unsafe_allow_html=True)

st.write("### Is there a Scarcity of Water",)
st.image('./images/pie_chart-waterless.jpg',
         caption='Info on Waterless Countries', use_column_width=True)

st.image('./images/world-chart_unsafeWater.jpeg',
         caption='Unsafe Water Usage in the World', use_column_width=True)

st.write("### Aim of Our Project: ")
st.write("* ensuring efficient and sustainable use of water resources ")
st.write("* valuable contribution to the ongoing efforts to manage water resources")
st.write("* address the challenges posed by water scarcity and contamination")


st.write("### Features of Our Project: ")
st.write("* recognize the water quality from its parameters")
st.write("* forecast the most effective water treatment")
st.write("* best use case classification or suitability prediction")


st.write("## Proposed Solution: ")
st.image("./images/Pro_Solution.jpg")

st.write("## System Architecture: ")
st.image("./images/System_Arch.jpg")

st.write("### To know more in detail, refer to:")
st.write("* IEEE formatted : ")
st.markdown('[Reasearch Paper](https://docs.google.com/document/d/1lI6uH-sgxe1CFGpqxSQlLc6d2d_elyPA/edit?usp=share_link&ouid=108355014328738916370&rtpof=true&sd=true)')

st.write("* Full Detailed Report of the Project:")
st.markdown('[Report](https://docs.google.com/document/d/1t6xHNdRDl_D5_Cptp_WSsoK0Elw8X-68/edit?usp=share_link&ouid=108355014328738916370&rtpof=true&sd=true)')

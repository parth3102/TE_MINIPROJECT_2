# T.E.-Mini-Project

# Water Quality Predictor
Predicting water quality based on a dataset using ML algorithms like Linear Regression and XGBoost. Deployed using streamlit on Python.
## Note- This app is for regular users as well as officials who have access to authorized data like PH, Nitrogen, BOD content of the water bodies

Here is how the web app looks like:
![Screenshot 2023-04-25 065854](https://user-images.githubusercontent.com/121672287/234153198-3f023791-3243-4dd6-9866-3bd44da90122.png)
![Screenshot 2023-04-25 070237](https://user-images.githubusercontent.com/121672287/234153222-52606637-bed9-43d6-a4cd-0437daa24240.png)
![Screenshot 2023-04-25 065954](https://user-images.githubusercontent.com/121672287/234153236-339e3fce-8d0a-4a4a-95ef-aff9c8b38051.png)
![Screenshot 2023-04-25 070201](https://user-images.githubusercontent.com/121672287/234153211-9c0c1843-f971-4d27-9d24-66c4d4de7b46.png)
![Screenshot 2023-04-25 070315](https://user-images.githubusercontent.com/121672287/234153256-b2df527e-6c68-4a2b-9aa2-ee3ae6163981.png)
![Screenshot 2023-04-25 070348](https://user-images.githubusercontent.com/121672287/234153264-c4c5bca1-5a89-4d94-a225-42fa0611c722.png)

## The user is required to enter the water quality parameters of the water body of their state.</li>


Steps to run the Project:

### Create a Virtual environment for the project
FIrst make sure to add conda to your env variables

conda create -n ml python=3.9

conda activate ml

pip install streamlit
pip install numpy pandas matplotlib scikit-learn

streamlit run admin_predict_page.py


## Data on the project
### Final Paper : 
https://docs.google.com/document/d/1lI6uH-sgxe1CFGpqxSQlLc6d2d_elyPA/edit?usp=share_link&ouid=108355014328738916370&rtpof=true&sd=true
### Project Report:
https://docs.google.com/document/d/1t6xHNdRDl_D5_Cptp_WSsoK0Elw8X-68/edit?usp=share_link&ouid=108355014328738916370&rtpof=true&sd=true 


## IoT to get Water Data

1. Aqua TROLL 500 Multiparameter Sonde:
Sensor options include temperature, conductivity, pH/ORP, Rugged Dissolved Oxygen (RDO®), turbidity, chlorophyll a, Phycocyanin (BGA-PC), Phycoerythrin (BGA-PE), FDOM, Crude Oil, Rhodamine WT, Fluorescein WT, ammonium (ISE), chloride (ISE) and nitrate (ISE).
https://in-situ.com/en/aqua-troll-500-multiparameter-sonde
https://in-situ.com/pub/media/catalog/product/cache/b032d51d6db336cfdc218e0b3a460463/a/q/aquatroll500-1024x768_1.jpg 

2. Hydrolab HL4 Multiparameter Sonde:
Parameters measured:Temperature, Conductivity, Depth, pH, Dissolved Oxygen (LDO), Turbidity, ORP, Clorophyll a, Blue-green algae, Rhodamine, Ammonium, Nitrate, Chloride.
https://www.ott.com/typo3temp/assets/_processed_/9/c/csm_Waterquality-multiparameter-sonde-Hydroalb-HL4-w-surveyor_68ec4b1b93.jpg?1682371147039
https://www.ott.com/products/water-quality-2/hydrolab-hl4-multiparameter-sonde-54/

3. ColorQ® 2x PRO 7:
https://lamotte.com/colorq-2x-pro-7-2086
https://lamotte.com/media/catalog/product/cache/67e61709e5fe001f9a6f50a73fe244ef/2/0/2086_1.png
measures Free Chlorine (DPD), Total Chlorine (DPD), Bromine (DPD), pH, Alkalinity, Calcium Hardness and Cyanuric Acid (Stabilizer) directly on a digital display

4. WaterGuru SENSE
measures the Free Chlorine (FC), acidity (pH), temperature
https://waterguru.com/products/waterguru-sense 
https://cdn.shopify.com/s/files/1/0583/3513/3904/products/water_guru_sense_plus_app_2x_fc474df2-5d25-4d2f-bc60-f0c425abe4c1.webp?crop=center&height=1000&v=1678811632&width=1000 

## Potential users of a water quality predictor website and their use cases:
* Homeowners: Homeowners may use a water quality predictor website to check the quality of their drinking water and determine if any treatment is necessary. They may also use the website to identify potential sources of water contamination in their area.
* Industrial facilities: Industrial facilities may use a water quality predictor website to ensure that the water they use in their processes is of sufficient quality. They may also use the website to identify potential sources of water contamination in their area.
* Agricultural producers: Agricultural producers may use a water quality predictor website to check the quality of the water they use for irrigation and to ensure that it is safe for use on their crops.
* Municipalities: Municipalities may use a water quality predictor website to monitor the quality of the water in their distribution systems and to identify potential sources of contamination.
* Environmental organizations: Environmental organizations may use a water quality predictor website to monitor the quality of water in rivers, lakes, and other bodies of water. They may also use the website to identify potential sources of pollution and to advocate for stronger environmental regulations.
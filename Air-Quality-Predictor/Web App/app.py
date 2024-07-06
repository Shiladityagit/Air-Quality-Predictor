import streamlit as st
import pickle
import numpy as np

# Import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Mapping for city names
city_map = {0:'Ahmedabad', 1:'Aizawl', 2:'Amaravati', 3:'Amritsar', 4:'Bengaluru', 
            5:'Bhopal', 6:'Brajrajnagar', 7:'Chandigarh', 8:'Chennai', 9:'Coimbatore', 
            10:'Delhi', 11:'Ernakulam', 12:'Gurugram', 13:'Guwahati', 14:'Hyderabad', 
            15:'Jaipur', 16:'Jorapokhar', 17:'Kochi', 18:'Kolkata', 19:'Lucknow', 
            20:'Mumbai', 21:'Patna', 22:'Shillong', 23:'Talcher', 24:'Thiruvananthapuram', 
            25:'Visakhapatnam'}

# Title of the app
st.title("Air Quality Predictor")

# User input for city selection
city = st.selectbox('Select City', list(city_map.keys()), format_func=lambda x: city_map[x])

# User inputs for various pollutants
pm25 = st.number_input('Enter PM2.5 value:')
pm10 = st.number_input('Enter PM10 value:')
no = st.number_input('Enter NO value:')
no2 = st.number_input('Enter NO2 value:')
nox = st.number_input('Enter NOx value:')
nh3 = st.number_input('Enter NH3 value:')
co = st.number_input('Enter CO value:')
so2 = st.number_input('Enter SO2 value:')
o3 = st.number_input('Enter O3 value:')
benzene = st.number_input('Enter Benzene value:')
toluene = st.number_input('Enter Toluene value:')
xylene = st.number_input('Enter Xylene value:')
aqi = st.number_input('Enter AQI value', min_value=0, step=1)

# Prediction button
if st.button('Predict Air Quality'):
    # Prepare the input data as a numpy array
    input_data = np.array([[city, pm25, pm10, no, no2,nox, nh3, co, so2, o3, benzene, toluene, xylene,aqi]])
    
    # Make prediction
    prediction = pipe.predict(input_data)
    
    # Map prediction to air quality category
    aqi_categories = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
    predicted_category = aqi_categories[prediction[0]]
    
    # Display the prediction
    st.write(f"The predicted air quality category is: {predicted_category}")

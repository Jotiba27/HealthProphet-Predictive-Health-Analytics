import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="HealthProphet Predictive Health Analysis",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load saved models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open('D:\CodeClause\multiple-disease-prediction-streamlit-app-main\saved_models\diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('D:\CodeClause\multiple-disease-prediction-streamlit-app-main\saved_models\heart_disease_model.sav' ,'rb'))
parkinsons_model = pickle.load(open('D:\CodeClause\multiple-disease-prediction-streamlit-app-main\saved_models\parkinsons_model.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('HealthProphet Predictive Health Analysis',
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://img.freepik.com/free-photo/close-up-doctor-with-stethoscope_23-2149191355.jpg?w=996&t=st=1714894114~exp=1714894714~hmac=6270edf80e7d875a81b8560c80fe8bafcf19b7bf23adc22071a0d6bfb80b89eb") center center;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
if selected == 'Diabetes Prediction':
    # Diabetes prediction page
    st.title('Diabetes Prediction using Machine Learning')
    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        Age = st.text_input('Age of the Person')
    # Prediction button
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    # Heart disease prediction page
    st.title('Heart Disease Prediction using Machine Learning')
    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        exang = st.text_input('Exercise Induced Angina')
        slope = st.text_input('Slope of the peak exercise ST segment')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        oldpeak = st.text_input('ST depression induced by exercise')
        ca = st.text_input('Major vessels colored by flourosopy')
    # Prediction button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(heart_diagnosis)

elif selected == "Parkinson's Prediction":
    # Parkinson's prediction page
    st.title("Parkinson's Disease Prediction using Machine Learning")
    # Input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        APQ = st.text_input('MDVP:APQ')
        RPDE = st.text_input('RPDE')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        PPQ = st.text_input('MDVP:PPQ')
        APQ5 = st.text_input('Shimmer:APQ5')
        DDA = st.text_input('Shimmer:DDA')
        DFA = st.text_input('DFA')
        PPE = st.text_input('PPE')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        DDP = st.text_input('Jitter:DDP')
        APQ = st.text_input('MDVP:APQ')
        NHR = st.text_input('NHR')
        spread1 = st.text_input('spread1')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        Shimmer = st.text_input('MDVP:Shimmer')
        HNR = st.text_input('HNR')
        spread2 = st.text_input('spread2')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    # Prediction button
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

import numpy as np
import streamlit as st
from PIL import Image
import pickle

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def run():
    img1 = Image.open('images.jpg')
    st.image(img1, use_column_width=False)
    st.title("Credit Card Approval Prediction using Machine Learning")



# declaring all variables

AMT_INCOME_TOTAL = 0
FLAG_WORK_PHONE	= 0
FLAG_LAND_PHONE = 0
YEARS_OF_EMPLOYMENT = 0
CODE_GENDER_F = False
FLAG_OWN_REALTY_NO = False
INCOME_TYPE_COMM_ASSOCIATE  = False
INCOME_TYPE_PENSIONER = False
INCOME_TYPE_STATE_SERVANT = False
INCOME_TYPE_STUDENT = False
EDUCATION_TYPE_HIGHER_EDU = False
EDUCATION_TYPE_ACADEMIC_DEGREE = False
EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU = False
EDUCATION_TYPE_LOWER_SECONDARY = False
FAMILY_STATUS_CIVIL_MARRIAGE = False
FAMILY_STATUS_MARRIED = False
FAMILY_STATUS_SINGLE = False
FAMILY_STATUS_SEPARATED = False
HOUSING_TYPE_SHARE_APT = False
HOUSING_TYPE_HOUSE_APT = False
HOUSING_TYPE_MUNICIPAL_APT = False
HOUSING_TYPE_OFFICE_APT = False
HOUSING_TYPE_RENTED_APT = False

approved_message = ", your Credit card application is approved"
declined_message = ", your Credit card application not approved"
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Full Name
full_name = st.text_input('Full Name')

# AMT_INCOME_TOTAL(3)
AMT_INCOME_TOTAL = st.number_input("Applicant's Monthly Income($)", value=0)

# FLAG_WORK_PHONE(22)
own_workphone = ('Yes', 'No')
options = list(range(len(own_workphone)))
FLAG_WORK_PHONE = st.selectbox("Do you have work phone", options, format_func=lambda x: own_workphone[x])



run()
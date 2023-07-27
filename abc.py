import numpy as np
import streamlit as st
from PIL import Image
import pickle


def run():
    img1 = Image.open('images.jpg')
    st.image(img1, use_column_width=False)
    st.title("Credit card Prediction using Machine Learning")

#declaring all variables
AMT_INCOME_TOTAL = 0
FLAG_WORK_PHONE	= 0
FLAG_LAND_PHONE = 0
YEARS_OF_EMPLOYMENT = 0
CODE_GENDER_F = False
FLAG_OWN_REALTY = False
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

# FLAG_PHONE(23)
own_phone = ('Yes', 'No')
options = list(range(len(own_phone)))
FLAG_LAND_PHONE = st.selectbox("Do you have land phone", options, format_func=lambda x: own_phone[x])

# YEARS_EMPLOYED(21)
YEARS_OF_EMPLOYMENT = st.number_input("Years of employment", value=0)

# For CODE_GENDER(1)
gen_display = ('Male', 'Female')
options = list(range(len(gen_display)))
gen = st.selectbox("Gender", options, format_func=lambda x: gen_display[x])

# for FLAG_OWN_REALTY(2)
own_realty = ('Yes', 'No')
options = list(range(len(own_realty)))
realty = st.selectbox("Do you own realty", options, format_func=lambda x: own_realty[x])

# INCOME_TYPE(4-7)
income_type = ('Commercial associate', 'Pensioner', 'State servant', 'Student')
options = list(range(len(income_type)))
income = st.selectbox("Type of Income", options, format_func=lambda x: income_type[x])

# EDUCATION_TYPE(8-11)
education_type = ('Higher education', 'Academic degree', 'Incomplete higher education','Lower secondary')
options = list(range(len(education_type)))
education = st.selectbox("Type of Education", options, format_func=lambda x: education_type[x])

# FAMILY_STATUS(12-15)
family_status = ('Civil marriage', 'Married', 'Single / not married', 'Separated')
options = list(range(len(family_status)))
family = st.selectbox("Family Status", options, format_func=lambda x: family_status[x])

# HOUSING_TYPE(16-20)
housing_type = ('Share Apt.', 'House Apt.', 'Municipal Apt.', 'Office Apt.', 'Rented Apt.')
options = list(range(len(housing_type)))
housing = st.selectbox("Housing Type", options, format_func=lambda x: housing_type[x])


if st.button("Submit"):

    if(FLAG_WORK_PHONE == 0):
       FLAG_WORK_PHONE = 1
    else:
       FLAG_WORK_PHONE = 0
####################################
    if(FLAG_LAND_PHONE == 0):
       FLAG_LAND_PHONE = 1
    else:
       FLAG_LAND_PHONE = 0
####################################
    if(gen == 0):
       CODE_GENDER_F = False
    else:
       CODE_GENDER_F = True
####################################
    if(realty == 0):
       FLAG_OWN_REALTY = True
    else:
       CODE_GENDER_F = False
####################################
    if(income == 0):
       INCOME_TYPE_COMM_ASSOCIATE = True
    elif(income == 1):
       INCOME_TYPE_PENSIONER = True
    elif(income == 2):
       INCOME_TYPE_STATE_SERVANT = True
    else:
       INCOME_TYPE_STUDENT = True
####################################
    if(education == 0):
       EDUCATION_TYPE_HIGHER_EDU = True
    elif(education == 1):
       EDUCATION_TYPE_ACADEMIC_DEGREE = True
    elif(education == 2):
       EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU = True
    else:
       EDUCATION_TYPE_LOWER_SECONDARY = True
####################################
    if(family == 0):
       FAMILY_STATUS_CIVIL_MARRIAGE = True
    elif(family == 1):
       FAMILY_STATUS_MARRIED = True
    elif(family == 2):
       FAMILY_STATUS_SINGLE = True
    else:
       FAMILY_STATUS_SEPARATED = True
####################################
    if(housing == 0):
       HOUSING_TYPE_SHARE_APT = True
    elif(housing == 1):
       HOUSING_TYPE_HOUSE_APT = True
    elif(housing == 2):
       HOUSING_TYPE_MUNICIPAL_APT = True
    elif(housing == 3):
       HOUSING_TYPE_OFFICE_APT = True
    else:
       HOUSING_TYPE_RENTED_APT = True



    input_data =(AMT_INCOME_TOTAL, FLAG_WORK_PHONE, FLAG_LAND_PHONE, YEARS_OF_EMPLOYMENT, CODE_GENDER_F, FLAG_OWN_REALTY, INCOME_TYPE_COMM_ASSOCIATE, INCOME_TYPE_PENSIONER, INCOME_TYPE_STATE_SERVANT, INCOME_TYPE_STUDENT, EDUCATION_TYPE_HIGHER_EDU, EDUCATION_TYPE_ACADEMIC_DEGREE, EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU, EDUCATION_TYPE_LOWER_SECONDARY, FAMILY_STATUS_CIVIL_MARRIAGE, FAMILY_STATUS_MARRIED, FAMILY_STATUS_SINGLE, FAMILY_STATUS_SEPARATED, HOUSING_TYPE_SHARE_APT, HOUSING_TYPE_HOUSE_APT, HOUSING_TYPE_MUNICIPAL_APT, HOUSING_TYPE_OFFICE_APT, HOUSING_TYPE_RENTED_APT)    
    #input_data =(315000.0, 0, 0, 2, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
    #input_data =(157500.0, 0, 1, 3, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
      st.success(full_name+approved_message)
    else:
      st.success(full_name+declined_message)

   
run()
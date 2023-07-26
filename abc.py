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
FLAG_PHONE = 0
WORKTERM = 0
CODE_GENDER_F = False
FLAG_OWN_REALTY_N = False
NAME_INCOME_TYPE_COMM_ASSOCIATE  = False
NAME_INCOME_TYPE_PENSIONER = False
NAME_INCOME_TYPE_STATE_SERVANT = False
NAME_INCOME_TYPE_Student = False
NAME_EDUCATION_TYPE_ACADEMIC_DEGREE = False
NAME_EDUCATION_TYPE_HIGHER_EDU = False
NAME_EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU = False
NAME_EDUCATION_TYPE_LOWER_SECONDARY = False
NAME_FAMILY_STATUS_CIVIL_MARRIAGE = False
NAME_FAMILY_STATUS_MARRIED = False
NAME_FAMILY_STATUS_SEPARATED = False
NAME_FAMILY_STATUS_SINGLE = False
NAME_HOUSING_TYPE_SHARE_APT = False
NAME_HOUSING_TYPE_HOUSE_APT = False
NAME_HOUSING_TYPE_MUNICIPAL_APT = False
NAME_HOUSING_TYPE_OFFICE_APT = False
NAME_HOUSING_TYPE_RENTED_APT = False

approved_message = ", your Credit card application is approved"
declined_message = ", your Credit card application not approved"
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# Full Name
full_name = st.text_input('Full Name')

# For CODE_GENDER(1)
gen_display = ('Female', 'Male')
options = list(range(len(gen_display)))
gen = st.selectbox("Gender", options, format_func=lambda x: gen_display[x])


# for FLAG_OWN_REALTY(2)
own_realty = ('Y', 'N')
options = list(range(len(own_realty)))
realty = st.selectbox("Own_Realty", options, format_func=lambda x: own_realty[x])

# AMT_INCOME_TOTAL(3)
AMT_INCOME_TOTAL = st.number_input("Applicant's Monthly Income($)", value=0)

# NAME_INCOME_TYPE(4-7)
income_type = ('Working', 'Commercial associate', 'Pensioner', 'State servant')
options = list(range(len(income_type)))
income = st.selectbox("Type of Income", options, format_func=lambda x: income_type[x])

# NAME_EDUCATION_TYPE(8-11)
education_type = ('Higher education', 'Secondary / secondary special', 'Incomplete higher')
options = list(range(len(education_type)))
education = st.selectbox("Type of Education", options, format_func=lambda x: education_type[x])

# NAME_FAMILY_STATUS(12-15)
family_status = ('Civil marriage', 'Married', 'Single / not married', 'Separated', 'Widow')
options = list(range(len(family_status)))
family = st.selectbox("Family Status", options, format_func=lambda x: family_status[x])

# NAME_HOUSING_TYPE(16-20)
housing_type = ('Rented apartment', 'House / apartment', 'Municipal apartment')
options = list(range(len(housing_type)))
housing = st.selectbox("Housing Type", options, format_func=lambda x: housing_type[x])


# YEARS_EMPLOYED(21)
days_employed = st.number_input("Days of Employed", value=0)


# FLAG_WORK_PHONE(22)
own_workphone = ('0', '1')
options = list(range(len(own_workphone)))
workphone = st.selectbox("Own_WorkPhone", options, format_func=lambda x: own_workphone[x])

# FLAG_PHONE(23)
own_phone = ('0', '1')
options = list(range(len(own_phone)))
phone = st.selectbox("Own_Phone", options, format_func=lambda x: own_phone[x])


if st.button("Submit"):

    #input_data =(315000.0, 0, 0, 2, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
    input_data =(157500.0, 0, 1, 3, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
      st.success(full_name+approved_message)
    else:
      st.success(full_name+declined_message)

    st.success(AMT_INCOME_TOTAL)

   
run()

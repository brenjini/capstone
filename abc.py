import streamlit as st
from PIL import Image
import pickle


def run():
    img1 = Image.open('images.jpg')
    st.image(img1, use_column_width=False)
    st.title("Credit card Prediction using Machine Learning")

    #loaded_model = pickle.load(open('trained_model.sav', 'rb'))
    #input_data =(315000.0, 0, 0, 2, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)


# Account No
account_no = st.text_input('Account Number')

# Full Name
full_name = st.text_input('Full Name')

# For CODE_GENDER
gen_display = ('Female', 'Male')
options = list(range(len(gen_display)))
gen = st.selectbox("Gender", options, format_func=lambda x: gen_display[x])

# for FLAG_OWN_CAR
own_car = ('Y', 'N')
options = list(range(len(own_car)))
car = st.selectbox("Own_Car", options, format_func=lambda x: own_car[x])

# for FLAG_OWN_REALTY
own_realty = ('Y', 'N')
options = list(range(len(own_realty)))
realty = st.selectbox("Own_Realty", options, format_func=lambda x: own_realty[x])

# for CNT_CHILDREN
cnt_children = ('1', '2', '3', '4', '5')
options = list(range(len(cnt_children)))
children = st.selectbox("No.of Children", options, format_func=lambda x: cnt_children[x])

# AMT_INCOME_TOTAL
mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

# NAME_INCOME_TYPE
income_type = ('Working', 'Commercial associate', 'Pensioner', 'State servant')
options = list(range(len(income_type)))
income = st.selectbox("Type of Income", options, format_func=lambda x: income_type[x])

# NAME_EDUCATION_TYPE
education_type = ('Higher education', 'Secondary / secondary special', 'Incomplete higher')
options = list(range(len(education_type)))
education = st.selectbox("Type of Education", options, format_func=lambda x: education_type[x])

# NAME_FAMILY_STATUS
family_status = ('Civil marriage', 'Married', 'Single / not married', 'Separated', 'Widow')
options = list(range(len(family_status)))
family = st.selectbox("Family Status", options, format_func=lambda x: family_status[x])

# NAME_HOUSING_TYPE
housing_type = ('Rented apartment', 'House / apartment', 'Municipal apartment')
options = list(range(len(housing_type)))
housing = st.selectbox("Housing Type", options, format_func=lambda x: housing_type[x])

# DAYS_BIRTH
days_birth = st.number_input("Days of Birth", value=0)

# DAYS_EMPLOYED
days_employed = st.number_input("Days of Employed", value=0)

# FLAG_MOBIL
own_mobile = ('0', '1')
options = list(range(len(own_mobile)))
mobile = st.selectbox("Own_Mobile", options, format_func=lambda x: own_mobile[x])

# FLAG_WORK_PHONE
own_workphone = ('0', '1')
options = list(range(len(own_workphone)))
workphone = st.selectbox("Own_WorkPhone", options, format_func=lambda x: own_workphone[x])

# FLAG_PHONE
own_phone = ('0', '1')
options = list(range(len(own_phone)))
phone = st.selectbox("Own_Phone", options, format_func=lambda x: own_phone[x])

# FLAG_EMAIL
own_email = ('0', '1')
options = list(range(len(own_email)))
email = st.selectbox("Own_Email", options, format_func=lambda x: own_email[x])

# OCCUPATION_TYPE
occupation_type = (
    '   ', 'Security staff', 'Sales staff', 'Accountants', 'Laborers', 'Managers', 'Drivers', 'Core staff')
options = list(range(len(occupation_type)))
occupation = st.selectbox("Occupation Type", options, format_func=lambda x: occupation_type[x])

# CNT_FAM_MEMBERS
cnt_fammembers = ('1', '2', '3', '4', '5')
options = list(range(len(cnt_fammembers)))
family = st.selectbox("No.of Family Members", options, format_func=lambda x: cnt_fammembers[x])

if st.button("Submit"):
   
    st.success("Success")

run()

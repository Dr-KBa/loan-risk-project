import streamlit as st
import requests
from datetime import datetime
import pytz  # timezone

url = 'https://app-model-1-main-specnhyoxq-lm.a.run.app/predict'

timezone = pytz.timezone("Europe/Vilnius")
current_time = datetime.now(timezone)
current_weekday = current_time.strftime("%A").upper()
current_hour = current_time.hour

weekday_mapping = {
    "MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3,
    "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6, "SUNDAY": 0
}

st.title("Loan application risk assessment")
st.markdown("**This app allows you to interact with ML model and predict weather the given credit application is risky or not.**")
st.markdown("**Survey your potential client and enter basic info in the fields below in order to get a prediction.**")
st.markdown("**Fields are pre-filled with default values; date and time related information is filled automatically at the start of an application.**")
st.markdown("**DISCLAIMER: This is a test application as part of Turing College Capstone project submission by Kazimieras B.; model is trained on financial data of  Home Credit Default Risk Kaggle Competition**")
st.markdown("** **")


#Inputs
NAME_CONTRACT_TYPE = st.selectbox("Contract type", ['Cash loans', 'Revolving loans'])
st.caption("Identification if loan is cash or revolving")
CODE_GENDER = st.selectbox("Gender", ['Male', 'Female', 'Unknown/Non-binary'])
st.caption("Gender of the client")
FLAG_OWN_CAR = st.selectbox("Owns a car", ['Yes', 'No'], index=1)
st.caption("Flag if client owns a car")
FLAG_OWN_REALTY = st.selectbox("Owns realty", ['Yes', 'No'], index=1)
st.caption("Flag if client owns a house or flat")
CNT_CHILDREN = st.number_input("Number of children", min_value=0, value=0, step=1)
st.caption("Number of children the client has")
AMT_INCOME_TOTAL = st.number_input("Total income", min_value=0.0, step=1.0, value=15000.0)
st.caption("Number of total anual income of the client")
AMT_CREDIT = st.number_input("Credit amount", min_value=0.0, step=1.0, value=5000.0)
st.caption("Credit amount of the loan")
AMT_ANNUITY = st.number_input("Annuity amount", min_value=0.0, step=1.0, value=5000.0)
st.caption("Fixed payments made over the term of a loan")
AMT_GOODS_PRICE = st.number_input("Goods price", min_value=0.0, step=1.0, value=5000.0)
st.caption("For consumer loans it is the price of the goods for which the loan is given")
NAME_TYPE_SUITE = st.selectbox("Type of suite", ['Unaccompanied', 'Family', 'Spouse, partner', 'Children', 'Group of people', 'Other_A', 'Other_B', 'Unknown'], index=0)
st.caption("Who was accompanying client when he was applying for the loan")
NAME_INCOME_TYPE = st.selectbox("Income type", ['Working', 'State servant', 'Commercial associate', 'Pensioner', 'Unemployed', 'Student', 'Businessman', 'Maternity leave'], index=0)
st.caption("Clients income type (businessman, working, maternity leave, ...)")
NAME_EDUCATION_TYPE = st.selectbox("Education type", ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree'], index=1)
st.caption("Level of highest education the client achieved")
NAME_FAMILY_STATUS = st.selectbox("Family status", ['Single / not married', 'Married', 'Civil marriage', 'Widow', 'Separated'], index=0)
st.caption("Family status of the client")
NAME_HOUSING_TYPE = st.selectbox("Housing type", ['House / apartment', 'Rented apartment', 'With parents', 'Municipal apartment', 'Office apartment', 'Co-op apartment'], index=0)
st.caption("What is the housing situation of the client (renting, living with parents, ...)")
REGION_POPULATION_RELATIVE = st.number_input("Region population relative", min_value=0.0, step=0.1, value=0.0)
st.caption("Normalized population of region where client lives (higher number means the client lives in more populated region)")
DAYS_BIRTH = st.number_input("Days since birth", max_value=0, step=1, value=0)
st.caption("Client's age in days at the time of application (enter negative)")
DAYS_EMPLOYED = st.number_input("Days employed", max_value=0, step=1, value=0)
st.caption("How many days before the application the person started current employment (enter negative)")
DAYS_REGISTRATION = st.number_input("Days registration", max_value=0.0, step=1.0, value=0.0)
st.caption("How many days before the application did client change his registration")
DAYS_ID_PUBLISH = st.number_input("Days ID published", max_value=0, step=1, value=0)
st.caption("How many days before the application did client change the identity document with which he applied for the loan (enter negative)")
OWN_CAR_AGE = st.number_input("Own car age", min_value=0.0, step=1.0, value=0.0)
st.caption("Age of client's car")
FLAG_MOBIL = st.selectbox("Has mobile", ['Yes', 'No'], index=1)
st.caption("Did client provide mobile phone")
FLAG_EMP_PHONE = st.selectbox("Has employment phone", ['Yes', 'No'], index=1)
st.caption("Did client provide work phone")
FLAG_WORK_PHONE = st.selectbox("Has work phone", ['Yes', 'No'], index=1)
st.caption("Did client provide home phone")
FLAG_CONT_MOBILE = st.selectbox("Has continuous mobile", ['Yes', 'No'], index=1)
st.caption("Was mobile phone reachable")
FLAG_PHONE = st.selectbox("Has phone", ['Yes', 'No'], index=1)
st.caption("Did client provide home phone")
FLAG_EMAIL = st.selectbox("Has email", ['Yes', 'No'], index=1)
st.caption("Did client provide email ")
OCCUPATION_TYPE = st.selectbox("Occupation type", ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Unknown', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff', 'Private service staff', 'Medicine staff', 'Security staff','High skill tech staff', 'Waiters/barmen staff', 'Low-skill Laborers', 'Realty agents', 'Secretaries', 'IT staff','HR staff'], index=1)
st.caption("What kind of occupation does the client have	")
CNT_FAM_MEMBERS = st.number_input("Count of family members", min_value=0.0, step=1.0)
st.caption("How many family members does client have")
REGION_RATING_CLIENT = st.number_input("Region rating client", min_value=0, step=1)
st.caption("Our rating of the region where client lives (1,2,3)")
REGION_RATING_CLIENT_W_CITY = st.number_input("Region rating client with city", min_value=0, step=1)
st.caption("Our rating of the region where client lives with taking city into account (1,2,3)")
WEEKDAY_APPR_PROCESS_START = st.selectbox(
    "Weekday of application process start",
    ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'],
    index=weekday_mapping[current_weekday]
)
st.caption("On which day of the week did the client apply for the loan (auto-filled with current weekday)")
HOUR_APPR_PROCESS_START = st.number_input(
    "Hour of application process start",
    min_value=0, max_value=23, step=1, value=current_hour
)
st.caption("Approximately at what hour did the client apply for the loan (auto-filled with current hour)")
REG_REGION_NOT_LIVE_REGION = st.selectbox("Not living in registration region", ['Yes', 'No'], index=1)
st.caption("Flag if client's permanent address does not match contact address")
REG_REGION_NOT_WORK_REGION = st.selectbox("Not working in registration region", ['Yes', 'No'], index=1)
st.caption("Flag if client's permanent address does not match work address")
LIVE_REGION_NOT_WORK_REGION = st.selectbox("Living region not work region", ['Yes', 'No'], index=1)
st.caption("Flag if client's contact address does not match work address")
REG_CITY_NOT_LIVE_CITY = st.selectbox("Not living in registration city", ['Yes', 'No'], index=1)
st.caption("Flag if client's permanent address does not match contact address")
REG_CITY_NOT_WORK_CITY = st.selectbox("Not working in registration city", ['Yes', 'No'], index=1)
st.caption("Flag if client's permanent address does not match work address")
LIVE_CITY_NOT_WORK_CITY = st.selectbox("Living city not work city", ['Yes', 'No'], index=1)
st.caption("Flag if client's contact address does not match work address")
ORGANIZATION_TYPE = st.selectbox("Organization type", [
    'Self-employed',
    'School', 'University', 'Kindergarten',
    'Government', 'Military', 'Police', 'Security Ministries', 'Emergency', 'Postal',
    'Electricity', 'Water Supply', 'Telecom',
    'Bank', 'Insurance', 'Legal Services', 'Accounting',
    'Construction', 'Housing', 'Realtor',
    'Agriculture', 'Restaurant', 'Hotel', 'Tourism',
    'Industry: type 1', 'Industry: type 2', 'Industry: type 3', 'Industry: type 4', 
    'Industry: type 5', 'Industry: type 6', 'Industry: type 7', 'Industry: type 8',
    'Industry: type 9', 'Industry: type 10', 'Industry: type 11', 'Industry: type 12', 'Industry: type 13',
    'Trade: type 1', 'Trade: type 2', 'Trade: type 3', 'Trade: type 4', 
    'Trade: type 5', 'Trade: type 6', 'Trade: type 7',
    'Transport: type 1', 'Transport: type 2', 'Transport: type 3', 'Transport: type 4',
    'Business Entity Type 1', 'Business Entity Type 2', 'Business Entity Type 3',
    'Culture', 'Advertising', 'Publishing', 'Media',
    'Cleaning', 'Security', 'Maintenance',
    'Health Care', 'Social Work', 'NGO', 'Religion',
    'Other', 'XNA'
], index=0)
st.caption("Type of organization where client works")
Income_Class = st.selectbox("Income class", ['Upper middle income', 'Middle income', 'Lower middle income', 'High income', 'Very high income', 'Ultra high income'], index=0)
st.caption("Income class of the client")
DTI_PROC = st.number_input("DTI process", min_value=0.0, step=0.01, value=5.0)
st.caption("Calculate and enter debt to income ratio for the client")



if st.button('Predict'):
    # Yes/No to 1/0 and Male/Female to M/F
    if CODE_GENDER == 'Male':
        CODE_GENDER = 'M'
    elif CODE_GENDER == 'Female':
        CODE_GENDER = 'F'
    else:
        CODE_GENDER = 'Unknown/Non-binary'
    FLAG_OWN_CAR = 1 if FLAG_OWN_CAR == 'Yes' else 0
    FLAG_OWN_REALTY = 1 if FLAG_OWN_REALTY == 'Yes' else 0
    FLAG_MOBIL = 1 if FLAG_MOBIL == 'Yes' else 0
    FLAG_EMP_PHONE = 1 if FLAG_EMP_PHONE == 'Yes' else 0
    FLAG_WORK_PHONE = 1 if FLAG_WORK_PHONE == 'Yes' else 0
    FLAG_CONT_MOBILE = 1 if FLAG_CONT_MOBILE == 'Yes' else 0
    FLAG_PHONE = 1 if FLAG_PHONE == 'Yes' else 0
    FLAG_EMAIL = 1 if FLAG_EMAIL == 'Yes' else 0
    REG_REGION_NOT_LIVE_REGION = 1 if REG_REGION_NOT_LIVE_REGION == 'Yes' else 0
    REG_REGION_NOT_WORK_REGION = 1 if REG_REGION_NOT_WORK_REGION == 'Yes' else 0
    LIVE_REGION_NOT_WORK_REGION = 1 if LIVE_REGION_NOT_WORK_REGION == 'Yes' else 0
    REG_CITY_NOT_LIVE_CITY = 1 if REG_CITY_NOT_LIVE_CITY == 'Yes' else 0
    REG_CITY_NOT_WORK_CITY = 1 if REG_CITY_NOT_WORK_CITY == 'Yes' else 0
    LIVE_CITY_NOT_WORK_CITY = 1 if LIVE_CITY_NOT_WORK_CITY == 'Yes' else 0

    data = {
        "NAME_CONTRACT_TYPE": NAME_CONTRACT_TYPE,
        "CODE_GENDER": CODE_GENDER,
        "FLAG_OWN_CAR": FLAG_OWN_CAR,
        "FLAG_OWN_REALTY": FLAG_OWN_REALTY,
        "CNT_CHILDREN": CNT_CHILDREN,
        "AMT_INCOME_TOTAL": AMT_INCOME_TOTAL,
        "AMT_CREDIT": AMT_CREDIT,
        "AMT_ANNUITY": AMT_ANNUITY,
        "AMT_GOODS_PRICE": AMT_GOODS_PRICE,
        "NAME_TYPE_SUITE": NAME_TYPE_SUITE,
        "NAME_INCOME_TYPE": NAME_INCOME_TYPE,
        "NAME_EDUCATION_TYPE": NAME_EDUCATION_TYPE,
        "NAME_FAMILY_STATUS": NAME_FAMILY_STATUS,
        "NAME_HOUSING_TYPE": NAME_HOUSING_TYPE,
        "REGION_POPULATION_RELATIVE": REGION_POPULATION_RELATIVE,
        "DAYS_BIRTH": DAYS_BIRTH,
        "DAYS_EMPLOYED": DAYS_EMPLOYED,
        "DAYS_REGISTRATION": DAYS_REGISTRATION,
        "DAYS_ID_PUBLISH": DAYS_ID_PUBLISH,
        "OWN_CAR_AGE": OWN_CAR_AGE,
        "FLAG_MOBIL": FLAG_MOBIL,
        "FLAG_EMP_PHONE": FLAG_EMP_PHONE,
        "FLAG_WORK_PHONE": FLAG_WORK_PHONE,
        "FLAG_CONT_MOBILE": FLAG_CONT_MOBILE,
        "FLAG_PHONE": FLAG_PHONE,
        "FLAG_EMAIL": FLAG_EMAIL,
        "OCCUPATION_TYPE": OCCUPATION_TYPE,
        "CNT_FAM_MEMBERS": CNT_FAM_MEMBERS,
        "REGION_RATING_CLIENT": REGION_RATING_CLIENT,
        "REGION_RATING_CLIENT_W_CITY": REGION_RATING_CLIENT_W_CITY,
        "WEEKDAY_APPR_PROCESS_START": WEEKDAY_APPR_PROCESS_START,
        "HOUR_APPR_PROCESS_START": HOUR_APPR_PROCESS_START,
        "REG_REGION_NOT_LIVE_REGION": REG_REGION_NOT_LIVE_REGION,
        "REG_REGION_NOT_WORK_REGION": REG_REGION_NOT_WORK_REGION,
        "LIVE_REGION_NOT_WORK_REGION": LIVE_REGION_NOT_WORK_REGION,
        "REG_CITY_NOT_LIVE_CITY": REG_CITY_NOT_LIVE_CITY,
        "REG_CITY_NOT_WORK_CITY": REG_CITY_NOT_WORK_CITY,
        "LIVE_CITY_NOT_WORK_CITY": LIVE_CITY_NOT_WORK_CITY,
        "ORGANIZATION_TYPE": ORGANIZATION_TYPE,
        "Income_Class": Income_Class,
        "DTI_PROC": DTI_PROC
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        prediction = response.json()['prediction'][0]
        prob_repay_on_time = prediction[0]
        prob_have_problems = prediction[1]

        if prob_repay_on_time > prob_have_problems:
            st.markdown(f"<h2 style='color: green;'>Client is likely to repay on time</h2>", unsafe_allow_html=True)
            certainty = prob_repay_on_time
        else:
            st.markdown(f"<h2 style='color: red;'>Client is likely to have problems</h2>", unsafe_allow_html=True)
            certainty = prob_have_problems

        st.write(f"Model certainty: {certainty:.0%}")
    else:
        st.error("Failed to get prediction...")






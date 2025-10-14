import streamlit as st
import pandas as pd
import pickle

with open("Employee_attrition_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Employee Attrition Prediction App 💼")
st.write("Enter employee details below to predict if they are likely to leave or stay:")

age = st.slider("Age", 18, 65, 30)
daily_rate = st.number_input("Daily Rate", 100, 1500, 800)
distance_from_home = st.slider("Distance From Home (km)", 1, 50, 5)
education = st.slider("Education Level (1 = Below College, 5 = Doctor)", 1, 5, 3)
environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
gender = st.selectbox("Gender", ["Male", "Female"])
hourly_rate = st.number_input("Hourly Rate", 10, 100, 60)
job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 3)
job_level = st.slider("Job Level (1-5)", 1, 5, 2)
job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
monthly_rate = st.number_input("Monthly Rate", 1000, 50000, 5000)
num_companies_worked = st.slider("Number of Companies Worked", 0, 10, 2)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_salary_hike = st.slider("Percent Salary Hike", 0, 50, 10)
performance_rating = st.slider("Performance Rating (1-4)", 1, 4, 3)
relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", 1, 4, 3)
stock_option_level = st.slider("Stock Option Level (0-3)", 0, 3, 1)
total_working_years = st.slider("Total Working Years", 0, 40, 10)
training_times_last_year = st.slider("Training Times Last Year", 0, 10, 3)
work_life_balance = st.slider("Work Life Balance (1-4)", 1, 4, 3)
years_at_company = st.slider("Years At Company", 0, 40, 5)
years_in_current_role = st.slider("Years In Current Role", 0, 20, 4)
years_since_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 2)
years_with_curr_manager = st.slider("Years With Current Manager", 0, 15, 3)

job_role = st.selectbox("Job Role", [
    "Healthcare Representative", "Human Resources", "Laboratory Technician", 
    "Manager", "Manufacturing Director", "Research Director", 
    "Research Scientist", "Sales Executive", "Sales Representative"
])
marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Frequently", "Travel_Rarely"])
department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
education_field = st.selectbox("Education Field", [
    "Human Resources", "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"
])

columns = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EmployeeCount',
    'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
    'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike',
    'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager',
    'JobRole_Healthcare Representative', 'JobRole_Human Resources',
    'JobRole_Laboratory Technician', 'JobRole_Manager',
    'JobRole_Manufacturing Director', 'JobRole_Research Director',
    'JobRole_Research Scientist', 'JobRole_Sales Executive',
    'JobRole_Sales Representative', 'MaritalStatus_Divorced',
    'MaritalStatus_Married', 'MaritalStatus_Single',
    'BusinessTravel_Non-Travel', 'BusinessTravel_Travel_Frequently',
    'BusinessTravel_Travel_Rarely', 'Department_Human Resources',
    'Department_Research & Development', 'Department_Sales',
    'EducationField_Human Resources', 'EducationField_Life Sciences',
    'EducationField_Marketing', 'EducationField_Medical',
    'EducationField_Other', 'EducationField_Technical Degree'
]

data = pd.DataFrame([[0]*len(columns)], columns=columns)

data['Age'] = age
data['DailyRate'] = daily_rate
data['DistanceFromHome'] = distance_from_home
data['Education'] = education
data['EnvironmentSatisfaction'] = environment_satisfaction
data['Gender'] = 1 if gender == "Male" else 0
data['HourlyRate'] = hourly_rate
data['JobInvolvement'] = job_involvement
data['JobLevel'] = job_level
data['JobSatisfaction'] = job_satisfaction
data['MonthlyIncome'] = monthly_income
data['NumCompaniesWorked'] = num_companies_worked
data['OverTime'] = 1 if overtime == "Yes" else 0
data['PercentSalaryHike'] = percent_salary_hike
data['PerformanceRating'] = performance_rating
data['RelationshipSatisfaction'] = relationship_satisfaction
data['StockOptionLevel'] = stock_option_level
data['TotalWorkingYears'] = total_working_years
data['TrainingTimesLastYear'] = training_times_last_year
data['WorkLifeBalance'] = work_life_balance
data['YearsAtCompany'] = years_at_company
data['YearsInCurrentRole'] = years_in_current_role
data['YearsSinceLastPromotion'] = years_since_last_promotion
data['YearsWithCurrManager'] = years_with_curr_manager

data['EmployeeCount'] = 1
data['StandardHours'] = 80
data['EmployeeNumber'] = 1
data['MonthlyRate'] = monthly_rate

data[f'JobRole_{job_role}'] = 1
data[f'MaritalStatus_{marital_status}'] = 1
data[f'BusinessTravel_{business_travel}'] = 1
data[f'Department_{department}'] = 1
data[f'EducationField_{education_field}'] = 1


if st.button("Predict Attrition"):
    prediction = model.predict(data)[0]
    proba = model.predict_proba(data)[0]

    if prediction == 0:
        result = "Likely to Leave ❌"
        confidence = proba[0] * 100
        st.markdown(f"### Prediction Result: {result}")
        st.markdown(f"**Attrition Probability:** {confidence:.2f}%")
        st.warning("This employee may be at risk of leaving. Consider reviewing workload, satisfaction, and incentives.")
    else:
        result = "Likely to Stay ✅"
        confidence = proba[1] * 100
        st.markdown(f"### Prediction Result: {result}")
        st.markdown(f"**Retention Probability:** {confidence:.2f}%")
        st.success("This employee is likely to stay. Maintain current engagement strategies.")
import streamlit as st 

css= """
<style>
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
       background: rgb(170,100,255);
       background: linear-gradient(148deg, rgba(170,100,255,1) 0%, rgba(42,1,164,1) 48%, rgba(37,1,86,1) 100%);
    }
    
    h1{
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        font-style: normal;
        color: #ffffff;
    }
    
    h3{
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-style: normal;
        color:#ffffff;
    }
    
    p{
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-style: normal;
        color:#ffffff;
    }
</style>
"""

st.markdown(css,unsafe_allow_html=True)
st.title("Student Evaluation for GDS Exam")

content = """
# Gram Daak Sevak Candidates Selection Page

Welcome to the Gram Daak Sevak Candidates Selection Page! This web application is designed to streamline the selection process for candidates applying for Gram Daak Sevak positions.

## Key Features:

1. **Upload CSV File:** Upload a CSV file containing candidate data, including student names, roll numbers, marks in different subjects, board names, primary languages, sports played, difficulty levels, number of previous year questions (PYQs), and the year of examination.

2. **Calculate Results:**
   - **With Normalization:** Determine candidate results based on normalized scores calculated using total marks, mean, and standard deviation.
   - **Without Normalization:** Calculate candidate results based on the total percentage of marks, marking candidates scoring above a threshold (e.g., 90%) as "Passed."

3. **Visualize Results:**
   - **Histogram:** View the distribution of normalized scores for passed and failed candidates.
   - **Line Chart:** Explore the trend of normalized scores for passed candidates against their candidate index.
   - **Bar Chart:** Visualize the number of PYQs for different difficulty levels across different years.

4. **Filter Candidates:** Filter candidates based on their primary language and sports played.

5. **Summary and Insights:** Gain insights into candidate counts before and after normalization, identify candidates not selected after normalization, and explore the number of PYQs across different difficulty levels and years.

## Conclusion:

The Gram Daak Sevak Candidates Selection Page enhances efficiency and transparency in the candidate selection process. It automates calculations, provides visualizations for performance analysis, and offers filtering options to facilitate informed decision-making in candidate evaluation.

"""

st.markdown(content,unsafe_allow_html=True)
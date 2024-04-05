import streamlit as st 

st.title("Our Algorithm")

cscc ="""
<style>
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
        background: rgb(100,255,253);
        background: linear-gradient(148deg, rgba(100,255,253,1) 0%, rgba(1,92,164,1) 48%, rgba(37,1,86,1) 100%);
    }
    
     h1{
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-style: normal;
        color:#ffffff;
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
st.markdown(cscc,unsafe_allow_html=True)

cont = """
### Calculation Algorithm:

1. **Calculate Total Marks:**
   - Add the marks obtained in Maths, English, and Social Studies for each candidate to get their total marks.

2. **Calculate Mean and Standard Deviation of Total Marks:**
   - Compute the mean and standard deviation of the total marks across all candidates.

3. **Calculate Z-Score of Total Marks:**
   - Calculate the Z-score for each candidate's total marks using the formula:
     ```
     Z = (X - μ) / σ
     ```
     where:
     - X is the total marks of the candidate,
     - μ is the mean of total marks,
     - σ is the standard deviation of total marks.

4. **Determine Difficulty Factors:**
   - Group candidates by their board names and find the maximum total marks achieved by any candidate in each board.

5. **Calculate Normalized Score:**
   - For each candidate, multiply their Z-score by the difficulty factor corresponding to their board.
   
6. **Determine Pass or Fail:**
   - If the normalized score is greater than 0, mark the candidate as "Passed"; otherwise, mark them as "Failed."

### Streamlit Display:

```python
# Function to calculate results
def calculate_results(df):
    if df.empty:
        return None, None
    
    # Perform calculations
    df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
    mean_total_marks = df['Total_Marks'].mean()
    std_total_marks = df['Total_Marks'].std()
    df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

    top_scores = df.groupby('Board_Name')['Total_Marks'].max()

    difficulty_factors = {}
    for board, top_score in top_scores.items():
        difficulty_factors[board] = top_score

    for board in df['Board_Name'].unique():
        board_mask = df['Board_Name'] == board
        df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

    # Determine pass or fail
    df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')

    return df


"""

st.markdown(cont,unsafe_allow_html=True)


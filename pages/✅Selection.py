# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Function to calculate results
# def calculate_results(df):
#     if df.empty:
#         return None, None
    
#     # Perform calculations
#     df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
#     mean_total_marks = df['Total_Marks'].mean()
#     std_total_marks = df['Total_Marks'].std()
#     df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

#     top_scores = df.groupby('Board_Name')['Total_Marks'].max()

#     difficulty_factors = {}
#     for board, top_score in top_scores.items():
#         difficulty_factors[board] = top_score

#     for board in df['Board_Name'].unique():
#         board_mask = df['Board_Name'] == board
#         df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

#     # Determine pass or fail
#     df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')
    
#     return df

# # Main function to run the Streamlit app
# def main():
#     st.title('Normalized Scores Calculator')

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Read CSV file into DataFrame
#         df = pd.read_csv(uploaded_file)
        
#         # Display DataFrame
#         st.subheader('Uploaded DataFrame')
#         st.write(df)

#         # Calculate results
#         df = calculate_results(df)
        
#         if df is not None:
#             # Display calculated results
#             st.subheader('Calculated Results')
#             st.dataframe(df)

#             # Display pass or fail result
#             st.subheader('Pass or Fail Result')
#             passed_candidates = df[df['Result'] == 'Passed']
#             failed_candidates = df[df['Result'] == 'Failed']
#             st.write("Passed Candidates:")
#             st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
#             st.write("Failed Candidates:")
#             st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

# if __name__ == '__main__':
#     main()
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Function to calculate results
# def calculate_results(df):
#     if df.empty:
#         return None, None
    
#     # Perform calculations
#     df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
#     mean_total_marks = df['Total_Marks'].mean()
#     std_total_marks = df['Total_Marks'].std()
#     df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

#     top_scores = df.groupby('Board_Name')['Total_Marks'].max()

#     difficulty_factors = {}
#     for board, top_score in top_scores.items():
#         difficulty_factors[board] = top_score

#     for board in df['Board_Name'].unique():
#         board_mask = df['Board_Name'] == board
#         df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

#     # Determine pass or fail
#     df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')
    
#     return df

# # Main function to run the Streamlit app
# def main():
#     st.title('Normalized Scores Calculator')

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Read CSV file into DataFrame
#         df = pd.read_csv(uploaded_file)
        
#         # Display DataFrame
#         st.subheader('Uploaded DataFrame')
#         st.write(df)

#         # Calculate results
#         df = calculate_results(df)
        
#         if df is not None:
#             # Display calculated results
#             st.subheader('Calculated Results')
#             st.dataframe(df)

#             # Display pass or fail result
#             st.subheader('Pass or Fail Result')
#             passed_candidates = df[df['Result'] == 'Passed']
#             failed_candidates = df[df['Result'] == 'Failed']
#             st.write("Passed Candidates:")
#             st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
#             st.write("Failed Candidates:")
#             st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

#             # Histogram plot for passed candidates
#             st.subheader('Histogram Plot for Passed Candidates')
#             passed_hist = plt.hist(passed_candidates['Normalized_Score'], bins=20, color='green')
#             st.pyplot()

#             # Histogram plot for failed candidates
#             st.subheader('Histogram Plot for Failed Candidates')
#             failed_hist = plt.hist(failed_candidates['Normalized_Score'], bins=20, color='red')
#             st.pyplot()

# if __name__ == '__main__':
#     main()
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Function to calculate results
# def calculate_results(df):
#     if df.empty:
#         return None, None
    
#     # Perform calculations
#     df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
#     mean_total_marks = df['Total_Marks'].mean()
#     std_total_marks = df['Total_Marks'].std()
#     df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

#     top_scores = df.groupby('Board_Name')['Total_Marks'].max()

#     difficulty_factors = {}
#     for board, top_score in top_scores.items():
#         difficulty_factors[board] = top_score

#     for board in df['Board_Name'].unique():
#         board_mask = df['Board_Name'] == board
#         df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

#     # Determine pass or fail
#     df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')
    
#     return df

# # Main function to run the Streamlit app
# def main():
#     st.title('Normalized Scores Calculator')

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Read CSV file into DataFrame
#         df = pd.read_csv(uploaded_file)
        
#         # Display DataFrame
#         st.subheader('Uploaded DataFrame')
#         st.write(df)

#         # Calculate results
#         df = calculate_results(df)
        
#         if df is not None:
#             # Display calculated results
#             st.subheader('Calculated Results')
#             st.dataframe(df)

#             # Display pass or fail result
#             st.subheader('Pass or Fail Result')
#             passed_candidates = df[df['Result'] == 'Passed']
#             failed_candidates = df[df['Result'] == 'Failed']
#             st.write("Passed Candidates:")
#             st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
#             st.write("Failed Candidates:")
#             st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

#             # Plot histograms
#             plt.figure(figsize=(10, 6))
#             sns.histplot(passed_candidates['Normalized_Score'], bins=20, color='green', edgecolor='black', label='Passed')
#             sns.histplot(failed_candidates['Normalized_Score'], bins=20, color='red', edgecolor='black', label='Failed')
#             plt.xlabel('Normalized Score')
#             plt.ylabel('Frequency')
#             plt.title('Histogram of Normalized Scores')
#             plt.legend()
#             plt.grid(axis='y')
#             plt.tight_layout()

#             # Show plot
#             st.pyplot(plt)

# if __name__ == '__main__':
#     main()
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# css= """
# <style>
#     .main{
#         background: rgb(177,34,195);
#         background: linear-gradient(0deg, rgba(177,34,195,1) 0%, rgba(253,187,45,1) 100%);
#     }
# </style>
# """

# st.markdown(css,unsafe_allow_html=True)
# # Function to calculate results
# def calculate_results(df):
#     if df.empty:
#         return None, None
    
#     # Perform calculations
#     df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
#     mean_total_marks = df['Total_Marks'].mean()
#     std_total_marks = df['Total_Marks'].std()
#     df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

#     top_scores = df.groupby('Board_Name')['Total_Marks'].max()

#     difficulty_factors = {}
#     for board, top_score in top_scores.items():
#         difficulty_factors[board] = top_score

#     for board in df['Board_Name'].unique():
#         board_mask = df['Board_Name'] == board
#         df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

#     # Determine pass or fail
#     df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')
    
#     return df

# # Main function to run the Streamlit app
# def main():
#     st.title('Normalized Scores Calculator')

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Read CSV file into DataFrame
#         df = pd.read_csv(uploaded_file)
        
#         # Display DataFrame
#         st.subheader('Uploaded DataFrame')
#         st.write(df)

#         # Calculate results
#         df = calculate_results(df)
        
#         if df is not None:
#             # Display calculated results
#             st.subheader('Calculated Results')
#             st.dataframe(df)

#             # Display pass or fail result
#             st.subheader('Pass or Fail Result')
#             passed_candidates = df[df['Result'] == 'Passed']
#             failed_candidates = df[df['Result'] == 'Failed']
#             st.write("Passed Candidates:")
#             st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
#             st.write("Failed Candidates:")
#             st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

#             # Plot histograms
#             plt.figure(figsize=(10, 6))
#             sns.histplot(passed_candidates['Normalized_Score'], bins=20, color='green', edgecolor='black', label='Passed')
#             sns.histplot(failed_candidates['Normalized_Score'], bins=20, color='red', edgecolor='black', label='Failed')
#             plt.xlabel('Normalized Score')
#             plt.ylabel('Frequency')
#             plt.title('Histogram of Normalized Scores')
#             plt.legend()
#             plt.grid(axis='y')
#             plt.tight_layout()
#             st.pyplot(plt)

#             # Plot line graph of normalized score for passed candidates
#             plt.figure(figsize=(10, 6))
#             plt.plot(passed_candidates.index, passed_candidates['Normalized_Score'], marker='o', linestyle='-')
#             plt.xlabel('Candidate Index')
#             plt.ylabel('Normalized Score')
#             plt.title('Normalized Score of Passed Candidates')
#             plt.grid(True)
#             plt.tight_layout()
#             st.pyplot(plt)

# if __name__ == '__main__':
#     main()
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# css= """
# <style>
#     @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
#     .main{
#         background: rgb(255,106,0);
#         background: linear-gradient(148deg, rgba(255,106,0,1) 0%, rgba(255,255,255,1) 49%, rgba(0,221,14,1) 100%);
#     }
    
#      h1{
#         font-family: "Poppins", sans-serif;
#         font-weight: 400;
#         font-style: normal;
#         color:#ffffff;
#     }
    
#     h3{
#         font-family: "Poppins", sans-serif;
#         font-weight: 400;
#         font-style: normal;
#         color:#ffffff;
#     }
    
#     p{
#         font-family: "Poppins", sans-serif;
#         font-weight: 400;
#         font-style: normal;
#         color:#ffffff;
#     }
# </style>
# """

# st.markdown(css,unsafe_allow_html=True)


# st.image("https://cracku.in/latest-govt-jobs/wp-content/uploads/2019/06/Delhi-Gramin-dak-sevak-logo.jpg", width=40) 
    
# # Function to calculate results
# def calculate_results(df):
#     if df.empty:
#         return None, None
    
#     # Perform calculations
#     df['Total_Marks'] = df['Maths_Marks'] + df['English_Marks'] + df['Social_Studies_Marks']
#     mean_total_marks = df['Total_Marks'].mean()
#     std_total_marks = df['Total_Marks'].std()
#     df['Total_Marks_Z_Score'] = (df['Total_Marks'] - mean_total_marks) / std_total_marks

#     top_scores = df.groupby('Board_Name')['Total_Marks'].max()

#     difficulty_factors = {}
#     for board, top_score in top_scores.items():
#         difficulty_factors[board] = top_score

#     for board in df['Board_Name'].unique():
#         board_mask = df['Board_Name'] == board
#         df.loc[board_mask, 'Normalized_Score'] = df.loc[board_mask, 'Total_Marks_Z_Score'] * difficulty_factors[board]

#     # Determine pass or fail
#     df['Result'] = np.where(df['Normalized_Score'] > 0, 'Passed', 'Failed')
    
#     return df

# # Main function to run the Streamlit app
# def main():
#     st.title('Gram Daak Sevak Candidates Selection Page')

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Read CSV file into DataFrame
#         df = pd.read_csv(uploaded_file)
        
#         # Display DataFrame
#         st.subheader('Uploaded DataFrame')
#         st.write(df)

#         # Calculate results
#         df = calculate_results(df)
        
#         if df is not None:
#             # Display calculated results
#             st.subheader('Calculated Results')
#             st.dataframe(df)

#             # Display pass or fail result
#             st.subheader('Pass or Fail Result')

#             # Sort candidates by normalized score
#             passed_candidates = df[df['Result'] == 'Passed'].sort_values(by='Normalized_Score', ascending=False)
#             failed_candidates = df[df['Result'] == 'Failed'].sort_values(by='Normalized_Score', ascending=False)
#             st.write("Passed Candidates:")
#             st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
#             st.write("Failed Candidates:")
#             st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

#             # Plot histograms
#             plt.figure(figsize=(10, 6))
#             sns.histplot(passed_candidates['Normalized_Score'], bins=20, color='green', edgecolor='black', label='Passed')
#             sns.histplot(failed_candidates['Normalized_Score'], bins=20, color='red', edgecolor='black', label='Failed')
#             plt.xlabel('Normalized Score')
#             plt.ylabel('Frequency')
#             plt.title('Histogram of Normalized Scores')
#             plt.legend()
#             plt.grid(axis='y')
#             plt.tight_layout()
#             st.pyplot(plt)

#             # Plot line graph of normalized score for passed candidates
#             plt.figure(figsize=(10, 6))
#             plt.plot(passed_candidates.index, passed_candidates['Normalized_Score'], marker='o', linestyle='-')
#             plt.xlabel('Candidate Index')
#             plt.ylabel('Normalized Score')
#             plt.title('Normalized Score of Passed Candidates')
#             plt.grid(True)
#             plt.tight_layout()
#             st.pyplot(plt)
            
#            # Show counts of candidates against total marks and normalized scores
#             total_marks_counts = df[['Student_Name', 'Total_Marks']].reset_index(drop=True)
#             normalized_scores_counts = passed_candidates[['Student_Name', 'Normalized_Score']].reset_index(drop=True)

#             st.subheader('Counts of Candidates')
#             st.write("Before Normalization:")
#             st.dataframe(total_marks_counts)
#             st.write("After Normalization:")
#             st.dataframe(normalized_scores_counts)


# # Create a selectbox for primary languages
#             selected_language = st.selectbox("Select Primary Language:", df['Primary_Language'].unique())

# # Create a selectbox for sports played
#             selected_sport = st.selectbox("Select Sport Played:", df['Sports_Played'].unique())

# # Filter the DataFrame based on selected language and sport
#             filtered_df = df[(df['Primary_Language'] == selected_language) & (df['Sports_Played'] == selected_sport)]

# # Display the filtered DataFrame
#             st.subheader("Filtered Candidates:")
#             st.dataframe(filtered_df)

# if __name__ == '__main__':
#     main()
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

css= """
<style>
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
    .main{
        background: rgb(170,100,255);
        background: linear-gradient(148deg, rgba(170,100,255,1) 0%, rgba(42,1,164,1) 48%, rgba(37,1,86,1) 100%);
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

st.markdown(css,unsafe_allow_html=True)


st.image("https://cracku.in/latest-govt-jobs/wp-content/uploads/2019/06/Delhi-Gramin-dak-sevak-logo.jpg", width=60) 
    
def calculation_without_normalization(df):
    if df.empty:
        return None
    
    # Determine pass or fail based on total percentage
    df['Results'] = np.where(df['Total_Marks']/5 > 90, 'Passed', 'Failed')
    
    return df


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

# Main function to run the Streamlit app
def main():
    st.title('Gram Daak Sevak Candidates Selection Page')

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display DataFrame
        st.subheader('Uploaded DataFrame')
        st.write(df)

        # Calculate results
        df = calculate_results(df)
        
        
        if df is not None:
            # Display calculated results
            st.subheader('Calculated Results')
            st.dataframe(df)

            # Display pass or fail result
            st.subheader('Pass or Fail Result')

            # Sort candidates by normalized score
            passed_candidates = df[df['Result'] == 'Passed'].sort_values(by='Normalized_Score', ascending=False)
            failed_candidates = df[df['Result'] == 'Failed'].sort_values(by='Normalized_Score', ascending=False)
            st.write("Passed Candidates:")
            st.dataframe(passed_candidates.style.applymap(lambda x: 'background-color: green', subset=pd.IndexSlice[:, ['Result']]))
            st.write("Failed Candidates:")
            st.dataframe(failed_candidates.style.applymap(lambda x: 'background-color: red', subset=pd.IndexSlice[:, ['Result']]))

            # Plot histograms
            st.write("Normalized score distribution Passed Candidates and Failed Candidates vs Frequency on Histogram")
            plt.figure(figsize=(10, 6))
            sns.histplot(passed_candidates['Normalized_Score'], bins=20, color='green', edgecolor='black', label='Passed')
            sns.histplot(failed_candidates['Normalized_Score'], bins=20, color='red', edgecolor='black', label='Failed')
            plt.xlabel('Normalized Score')
            plt.ylabel('Frequency')
            plt.title('Histogram of Normalized Scores')
            plt.legend()
            plt.grid(axis='y')
            plt.tight_layout()
            st.pyplot(plt)

            # Plot line graph of normalized score for passed candidates
            st.write("Normalized score distribution Passed Candidates vs Candidate Index on Line Chart")
            plt.figure(figsize=(10, 6))
            plt.plot(passed_candidates.index, passed_candidates['Normalized_Score'], marker='o', linestyle='-')
            plt.xlabel('Candidate Index')
            plt.ylabel('Normalized Score')
            plt.title('Normalized Score of Passed Candidates')
            plt.grid(True)
            plt.tight_layout()
            st.pyplot(plt)
            
           # Show counts of candidates against total marks and normalized scores
            total_marks_counts = df[['Student_Name','Roll_Number', 'Total_Marks']].reset_index(drop=True)
            normalized_scores_counts = passed_candidates[['Student_Name','Roll_Number','Normalized_Score']].reset_index(drop=True)

            st.subheader('Counts of Candidates')

# Create a column layout for side-by-side display
            col1, col2 = st.columns(2)

# Display counts before normalization in the first column
            with col1:
                st.write("Before Normalization:")
                st.dataframe(total_marks_counts)

# Display counts after normalization in the second column
            with col2:
                st.write("After Normalization:")
                st.dataframe(normalized_scores_counts)
    
    # Find missing Roll_Numbers
                st.write("Name of Candidates didn't got selected after Normalization")
                missing_roll_numbers = total_marks_counts[~total_marks_counts['Roll_Number'].isin(normalized_scores_counts['Roll_Number'])]
                st.dataframe(missing_roll_numbers.style.apply(lambda x: ['color: red' if x.name in missing_roll_numbers.index else '' for i in x], axis=1))
                


            st.write("Number of PYQs in three different years vs Difficulty of Question Paper")
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x='Difficulty_Level', y='No_PYQs', hue='Year')
            plt.xlabel('Difficulty Level')
            plt.ylabel('Number of PYQs')
            plt.title('Difficulty Level vs Number of PYQs')
            plt.grid(True)
            plt.legend(title='Year')
            st.pyplot(plt)

            # Create a selectbox for primary languages
            st.write("Filtering candidates based on their primary language")
            selected_language = st.selectbox("Select Primary Language:", df['Primary_Language'].unique())

            # Create a selectbox for sports played
            st.write("Filtering candidates based on the sports played")
            selected_sport = st.selectbox("Select Sport Played:", df['Sports_Played'].unique())

            # Filter the DataFrame based on selected language and sport
            filtered_df = df[(df['Primary_Language'] == selected_language) & (df['Sports_Played'] == selected_sport)]

            # Display the filtered DataFrame
            st.subheader("Filtered Candidates:")
            st.dataframe(filtered_df)

if __name__ == '__main__':
    main()

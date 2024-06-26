# Gram Daak Sevak Candidates Selection Page

Gram Daak Sevak Candidates Selection Page is a *Web Application* designed to facilitate the selection process for candidates applying for "Gram Daak Sevak" positions. The application allows users to upload a CSV file containing candidate data, perform calculations to determine candidate results, visualize candidate performance, and filter candidates based on various criteria.

Website URL - https://gramdaakseva.streamlit.app/
PPT_Link - https://drive.google.com/file/d/1ffNVRB2-hPQPh6F00H6m8NOI_FRB_Uhn/view?usp=sharing
## Key Features

- **Upload CSV File:** Users can upload a CSV file containing candidate data, including information such as student names, roll numbers, marks in different subjects, board names, primary languages, sports played, difficulty levels, number of previous year questions (PYQs), and the year of examination.

- **Calculate Results:**
  - **With Normalization:** Calculates normalized scores based on total marks, mean, and standard deviation. Then calculates the difficulty factor of respective board exam based on the TOP SCORES. 
  Normalized marks = difficulty scale factor *  standard marks
  Candidates are categorized as "Passed" or "Failed" based on their normalized scores.
  [Passed - above mean,
   Failed - below mean]
  - **Without Normalization:** Determines candidate results based on the total percentage of marks. Candidates scoring above a threshold (e.g., 90%) are marked as "Passed."

- **USP (Unique Selling Product):**
  - A comparison is shown between the previous method and new method for selection.
  - List of deserving candidates based on their total score is displayed before normalization.
  - List of deserving candidates based on their normalized score is displayed after normalization.
  - Then a table is displayed containing those undeserved candidates that were first selected(before normalization) but are rejected on the basis of their normalized score which is a fair and uniform criteria for selection.


- **Visualize Results:**
  - **Histogram:** Displays the distribution of normalized scores for passed and failed candidates on a histogram.
  - **Line Chart:** Shows the trend of normalized scores for passed candidates against their candidate index.
  - **Bar Chart:** Illustrates the number of PYQs for different difficulty levels across different years.

- **Filter Candidates:** Users can filter candidates based on their primary language and sports played.

- **Summary and Insights:** The application provides a summary of candidate counts before and after normalization, identifies candidates who were not selected after normalization, and offers insights into the number of PYQs across different difficulty levels and years.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yash182023/Gram_Daak_Seva__Recruitment_HackHound_2.0.git

2. Navigate to the project directory:
   ```bash
    cd Gram_Daak_Seva__Recruitment_HackHound_2.0

3. Install the required dependencies:
   ```python
   pip install -r requirements.txt
## Usage

1. Run the Streamlit application:
    ```python
        streamlit run app.py

2. Open the provided URL in your web browser to access the application.

3. Upload a CSV file containing candidate data and explore the features of the application.

## LICENSE
This project is licensed under the MIT License


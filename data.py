import csv
import random

def create_csv(file_name, data):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['Board_Name', 'Student_Name', 'Roll_Number', 'Maths_Marks', 'Science_Marks', 'English_Marks', 'Social_Studies_Marks', 'Extra_Language_Marks']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Example data
student_names = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Brown', 'William Davis', 'Olivia Wilson', 'James Martinez', 'Sophia Anderson', 'Daniel Taylor', 'Isabella Thomas', 'Alexander Hernandez', 'Emma Moore', 'Joseph Martin', 'Ava Jackson', 'David White', 'Mia Harris', 'Christopher Nelson', 'Abigail Thompson', 'Matthew Garcia', 'Sofia Clark']
board_names = [
    'CBSE_Board',
    'West_Bengal_Board',
    'Bihar_Board',
    'Karnataka_Board',
    'Arunachal_Pradesh_Board',
    'Assam_Board',
    'Chhattisgarh_Board',
    'Goa_Board',
    'Gujarat_Board',
    'Haryana_Board',
    'Himachal_Pradesh_Board',
    'Jharkhand_Board',
    'Kerala_Board',
    'Madhya_Pradesh_Board',
    'Maharashtra_Board',
    'Manipur_Board',
    'Meghalaya_Board',
    'Mizoram_Board',
    'Nagaland_Board',
    'Odisha_Board',
    'Punjab_Board',
    'Rajasthan_Board',
    'Sikkim_Board',
    'Tamil_Nadu_Board',
    'Telangana_Board',
    'Tripura_Board',
    'Uttar_Pradesh_Board',
    'Uttarakhand_Board',
    'Andhra_Pradesh_Board'
]

data = []
for i in range(100):
    student_data = {
        'Board_Name': random.choice(board_names),
        'Student_Name': random.choice(student_names),
        'Roll_Number': f'RA10{i+1}',
        'Maths_Marks': random.randint(0, 100),
        'Science_Marks': random.randint(0, 100),
        'English_Marks': random.randint(0, 100),
        'Social_Studies_Marks': random.randint(0, 100),
        'Extra_Language_Marks': random.randint(0, 100)
    }
    data.append(student_data)

# Name of the CSV file to be created
file_name = 'student_marks_extended.csv'

# Call function to create CSV file
create_csv(file_name, data)

print(f"CSV file '{file_name}' with 100 rows has been created successfully.")



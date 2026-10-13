import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/student-mat.csv")

print("-------------------------------------------------------------------------------")
print("Student Performance Analyzer")
print("-------------------------------------------------------------------------------")
print("--------------- Main Menu ------------------")

print ("1. View All Student \n" 
       "2. View Top 10 Student \n"
       "3. Student below 75% Attendance \n"
       "4. View Subject-wise Average Marks \n"
       "5. Analyze Study hour vs Marks \n"
       "6. View passing and failing students \n" 
       "7. Identify students at academic risk \n" 
       "8. Export analysis reports \n" 
       "9. View Charts \n"
       "10. Exit \n")

df["average_Marks"] = df[["Programming","Mathematics","Database","English","Physics"]].mean(axis=1)








def View_all_students():
    print(df[["student_id","name"]])

def View_top_10_student():
    top_10 = df.nlargest(10,"average_Marks")
    print(top_10[["student_id","name","average_Marks"]])

def Student_below_75_att():
    sb75 = df[df["attendance_percent"] <75] 
    print(sb75[["student_id","name","attendance_percent"]])

def View_Subject_wise_Average():
    print("Programming =", df["Programming"].mean(axis=0))
    print("Mathemetics =", df["Mathematics"].mean(axis=0))
    print("English =", df["English"].mean(axis=0))
    print("Physics =", df["Physics"].mean(axis=0))














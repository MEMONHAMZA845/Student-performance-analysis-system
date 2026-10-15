import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/student-mat.csv")


df["average_marks"] = df[["Programming","Mathematics","Database","English","Physics"]].mean(axis=1)


def View_all_students():
    print(df[["student_id","name"]])

def View_top_10_student():
    top_10 = df.nlargest(10,"average_marks")
    print(top_10[["student_id","name","average_marks"]])

def Student_below_75_att():
    sb75 = df[df["attendance_percent"] <75] 
    print(sb75[["student_id","name","attendance_percent"]])

def View_Subject_wise_Average():
    print("Programming =", df["Programming"].mean(axis=0))
    print("Mathemetics =", df["Mathematics"].mean(axis=0))
    print("English =", df["English"].mean(axis=0))
    print("Physics =", df["Physics"].mean(axis=0))
    print("Database =",df["Database"].mean(axis=0))

def Study_hour_vs_marks():
    print("Average Study Time per week =",df["study_hours_per_week"].mean(axis=0))
    print("Average Marks =",df["average_marks"].mean(axis=0))

    correlation = df["study_hours_per_week"].corr(df["average_marks"])
    print("Correlation =", correlation)

    if correlation > 0:
        print("There is a positive relationship between study time and marks.\n" \
               " Students who study more tend to score higher")
    elif correlation < 0:
        print("There is a negative relationship between study time and marks.\n" \
        "students who study more tends to score less ")
    else:
        print("No linear correlation between study time and score ")

def Passing_failing_students_menu():

    print("Select Course\n" 
    "1. Programming\n" 
    "2. Mathematics\n" 
    "3. Database\n" 
    "4. English\n" 
    "5. Physics\n" \
    "6. pass or fail by average marks\n")
    Passing_failing_students()



def Passing_failing_students():

    while True:

        try:
            user_input = int(input("Enter A number From the following Menu "))
        except ValueError:
            print("Enter a Valid Input :")
            continue

        if user_input == 1:

            passed = df.loc[df["Programming"] >= 50,"student_id"].tolist()
            failed = df.loc[df["Programming"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break

        if user_input == 2:

            passed = df.loc[df["Mathematics"] >= 50,"student_id"].tolist()
            failed = df.loc[df["Mathematics"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break

        if user_input == 3:

            passed = df.loc[df["Database"] >= 50,"student_id"].tolist()
            failed = df.loc[df["Database"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break

        if user_input == 4:

            passed = df.loc[df["English"] >= 50,"student_id"].tolist()
            failed = df.loc[df["English"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break

        if user_input == 5:

            passed = df.loc[df["Physics"] >= 50,"student_id"].tolist()
            failed = df.loc[df["Physics"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break

        if user_input == 6:

            passed = df.loc[df["average_marks"] >= 50,"student_id"].tolist()
            failed = df.loc[df["average_marks"] < 50,"student_id"].tolist()
            result = pd.DataFrame({
                "Passed" : pd.Series(passed),
                "Failed" : pd.Series(failed)
            })
            print(result)
            break
        else:
            print("enter a valid input ")
            break

def Identify_student_at_risk():

    flagged = 0
    for _,row in df.iterrows():
        risk = 0
        reasons = []

        if row["average_marks"] <= 50:
            risk += 2
            reasons.append("Average Marks are = or lower then 50 ")
        elif row["average_marks"] <= 60 and row["average_marks"] > 50:
            risk += 1 
            reasons.append("Average marks are =  or lower  then 60 ")

        if row["attendance_percent"] <= 60:
            risk += 2
            reasons.append("Attendance is = or  lower then 60 ")
        elif row["attendance_percent"] <= 75 and row["attendance_percent"] > 60:
            risk += 1
            reasons.append(" Attendance is = or lower then 75")

        if risk >= 3:
            level = "high"
        elif risk == 2:
            level = "medium"
        else:
            continue

        flagged +=1
        print("\nStudent name =", row["name"])
        print("Student id =", row["student_id"])
        print("student risk =", risk)
        print("risk level =", level)
        print("Reasons :")
        for index, r in enumerate(reasons):
            print(f"{index}. {r}\n")

    print(f"Total Students at risk : {flagged}")

def Export_analysis_report():
    pass

def View_Charts():
    pass


while True:

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

    try:
        user_input = int(input("Enter a Number From Menu :\n"))
    except ValueError:
        print("enter a valid input ")
        continue

    if user_input == 1:
        View_all_students()

    elif user_input == 2:
        View_top_10_student()

    elif user_input == 3:
        Student_below_75_att()

    elif user_input == 4:
        View_Subject_wise_Average()

    elif user_input == 5:
        Study_hour_vs_marks()
        
    elif user_input == 6:
        Passing_failing_students_menu()
        
    elif user_input ==7:
        Identify_student_at_risk()
        
    elif user_input ==8:
        Export_analysis_report()
        
    elif user_input == 9 :
        View_Charts()
        
    elif user_input == 10 :
        break
        
    else:
        print("Enter a Number From The Menu ")
        







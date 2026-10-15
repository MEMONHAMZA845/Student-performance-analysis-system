

def Export_analysis_report(df, get_at_risk_students):

    print("\nSelect The Analysis You want to Export :")
    print("1. Top 10 Student\n" \
          "2. Student in Risk \n" \
          "3. All Girls \n" \
          "4. All Boys \n" \
          "5. Exit \n")

    while True:

        try:
            user_input = int(input("Enter a Number from menu"))

        except ValueError:
            print("Enter a Valid Number ")
            continue

        if user_input == 1:
            top_10 = df.nlargest(10,"average_marks")
            top_10.to_excel("outputs/top_10_student.xlsx", index=False)
            print("Top 10 Students Exported SUccesfully ")
            break

        elif user_input == 2:
            at_risk = get_at_risk_students()
            at_risk.to_excel("outputs/student_at_risk.xlsx", index=False)
            print("At-risk students exported to outputs folder")
            break

        elif user_input == 3:
            df[df["gender"] == "Female"].to_excel("outputs/all_female_students.xlsx",index=True)
            print("All Female students file exported to outputs folder :")
            break

        elif user_input == 4:
            df[df["gender"] == "Male"].to_excel("outputs/all_Male_students.xlsx",index=True)
            print("All Male students file exported to outputs folder :")
            break
        elif user_input == 5:
            break
    
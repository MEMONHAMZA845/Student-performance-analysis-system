import matplotlib.pyplot as plt

def View_Charts(df):
    print("\nView and save Charts")
    print(
        "1. Subject-wise average marks\n"
        "2. Study hour vs Average marks\n"
        "3. Distribution of average marks\n"
        "4. Passed vs failed students\n" \
        "5. Exit" 
    )

    while True:
        try:
            user_input = int(input("Enter a number from the menu: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if user_input == 1:
            subjects = [
                "Programming",
                "Mathematics",
                "Database",
                "English",
                "Physics"
            ]

            averages = df[subjects].mean()
            print(averages)

            plt.bar(averages.index, averages.values)
            plt.title("Subject-wise Average Marks")
            plt.xlabel("Subjects")
            plt.ylabel("Average Marks")
            plt.tight_layout()
            plt.savefig("charts/Subject_wise_Average_Marks.png")
            plt.show()
            break

        elif user_input == 2 :

            plt.scatter(df["study_hours_per_week"],df["average_marks"])
            plt.title("Study Hours vs Average Marks")
            plt.xlabel("Study Hours per Week")
            plt.ylabel("Average Marks")

            plt.savefig("charts/StudyHour_VS_averagemarks.png")
            plt.show()
            break

        elif user_input == 3 :

            plt.hist(df["average_marks"],bins=10)
            plt.title("Average Marks Distribution among Students ")
            plt.xlabel("Average Marks")
            plt.ylabel("Number of Students")

            plt.tight_layout()
            plt.savefig("charts/Average_marks_distribution.png")
            plt.show()
            break

        elif user_input == 4:

            passed = df.loc[df["Programming"] >= 50, "student_id"].tolist()
            failed = df.loc[df["Programming"] < 50, "student_id"].tolist()

            categories = ["Passed", "Failed"]
            counts = [len(passed), len(failed)]

            plt.bar(categories, counts)

            plt.title("Passed vs Failed Students")
            plt.xlabel("Result")
            plt.ylabel("Number of Students")

            plt.tight_layout()
            plt.savefig("charts/Passed_VS_failed.png")
            plt.show()
            break

        elif user_input == 5 :
            break
        
        else:
            print("enter a number from menu ")